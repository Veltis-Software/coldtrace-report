const { chromium } = require('C:/Users/david/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

async function main() {
  const origin = 'https://coldtrace-web-311618880556.us-east1.run.app';
  const cloud = {'X-Serverless-Authorization': 'Bearer ' + process.env.COLDTRACE_TEST_CLOUD_TOKEN};
  const credentials = {email:'operaciones@friopacifico.example', password:process.env.COLDTRACE_FIXTURE_PASSWORD};
  const browser = await chromium.launch({channel:'msedge',headless:true});
  try {
    const context = await browser.newContext({viewport:{width:1450,height:1000},locale:'es-PE',acceptDownloads:true});
    const req = context.request;
    const send = async (method, endpoint, headers, data, expected = 200) => {
      const result = await req.fetch(origin + endpoint,{method,headers,data,timeout:65000});
      assert.equal(result.status(),expected,method+' '+endpoint+' returned '+result.status());
      return expected === 204 ? null : await result.json().catch(() => null);
    };
    const session = await send('POST','/api/v1/authentication/sign-in',cloud,credentials);
    const auth = {...cloud,Authorization:'Bearer '+session.token};
    const from = '2026-11-06T00:00:00Z';
    const to = '2026-11-07T00:00:00Z';
    const query = '/api/v1/incidents/traceability?'+new URLSearchParams({from,to});
    const rows = await send('GET',query,auth);
    const incident = rows.find(row => row.type.toLowerCase().includes('threshold')) ?? rows.find(row => row.state !== 'RESOLVED');
    assert.ok(incident,'No demo incident');
    const detail = '/api/v1/incidents/'+incident.id;
    const action = 'Se trasladaron los lácteos a una cámara de respaldo.';
    if (incident.state !== 'RESOLVED') {
      if (incident.state === 'OPEN') {
        const users = await send('GET','/api/v1/alerts/assignees',auth);
        const assignee = users.find(user => user.userId === session.userId) ?? users[0];
        assert.ok(assignee);
        await send('POST','/api/v1/alerts/'+incident.id+'/acknowledgement',auth,{assigneeUserId:assignee.userId});
      }
      await send('POST',detail+'/resolution',auth,{description:' '},400);
      await send('POST',detail+'/corrective-actions',auth,{description:action},201);
      await send('POST',detail+'/resolution',auth,{description:'La temperatura volvió a 4 °C y se verificó la cámara.'});
    }
    const closed = await send('GET',detail,auth);
    assert.equal(closed.state,'RESOLVED');
    assert.ok(closed.resolvedByUserId && closed.resolvedAt);
    assert.ok(closed.correctiveActions.some(entry => entry.description === action && entry.author_user_id && entry.created_at));
    const params = new URLSearchParams({state:'RESOLVED',assetId:String(closed.asset.assetId),severity:closed.severity,assigneeUserId:String(closed.assignee.userId)});
    const filtered = await send('GET',query+'&'+params,auth);
    assert.ok(filtered.some(item=>item.id===closed.id));
    assert.ok(filtered.every(item=>item.state==='RESOLVED' && item.asset.assetId===closed.asset.assetId && item.assignee.userId===closed.assignee.userId));
    assert.deepEqual(await send('GET',query+'&assetId=99999999',auth),[]);
    await send('GET',query.replace(encodeURIComponent(to),encodeURIComponent(from)),auth,undefined,400);

    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error=>errors.push(error.message));
    await page.route(origin+'/**',route=>route.continue({headers:{...route.request().headers(),...cloud}}));
    await page.goto(origin+'/identity-access/sign-in');
    await page.locator('#email').fill(credentials.email);
    await page.locator('#password').fill(credentials.password);
    await page.locator('form button[type=submit]').click();
    await page.waitForURL(url=>!url.pathname.includes('sign-in'),{timeout:65000});
    await page.goto(origin+'/alerts/incidents');
    await page.getByRole('link',{name:'Historial',exact:true}).click();
    const panel=page.getByRole('region',{name:'Historial de incidencias'});
    await panel.getByLabel('Desde (UTC)').fill('2026-11-06');
    await panel.getByLabel('Hasta (UTC)').fill('2026-11-06');
    await panel.getByLabel('Estado').selectOption('RESOLVED');
    await panel.getByRole('button',{name:'Consultar',exact:true}).click();
    await panel.getByText(action,{exact:false}).waitFor({timeout:65000});
    await page.screenshot({path:path.join(__dirname,'sprint3-cloud-history.png'),fullPage:true});
    const [download]=await Promise.all([page.waitForEvent('download'),panel.getByRole('button',{name:'Exportar CSV'}).click()]);
    const file=path.join(__dirname,'sprint3-history-export.csv');
    await download.saveAs(file);
    assert.match(fs.readFileSync(file,'utf8'),/cámara de respaldo/i);
    assert.equal(download.suggestedFilename(),'historial-2026-11-06-2026-11-06.csv');
    await page.setViewportSize({width:390,height:844});
    const overflow=await panel.evaluate(el => el.scrollWidth > el.clientWidth + 1);
    assert.equal(overflow,false,'History panel overflows at 390px');
    await page.screenshot({path:path.join(__dirname,'sprint3-cloud-history-mobile.png'),fullPage:true});
    assert.deepEqual(errors,[]);
    const evidence={incidentId:closed.id,state:closed.state,author:closed.resolvedByUserId,actionCount:closed.correctiveActions.length,filtered:filtered.length,negativeFilter:0,export:download.suggestedFilename(),pageErrors:errors};
    fs.writeFileSync(path.join(__dirname,'sprint3-runtime.json'),JSON.stringify(evidence,null,2));
    console.log(JSON.stringify(evidence));
  } finally { await browser.close(); }
}
main().catch(error=>{console.error(error.message);process.exitCode=1;});


