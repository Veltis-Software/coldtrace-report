# Auditoría de cierre Sprint 2

Fuente normativa: FAS/Trabajo Final_1ASI0657_202620.docx, Sprint 2 → Avance 3. El cierre exige evidencia de las ocho secciones, no solo encabezados completos.

| Requisito | Evidencia disponible | Comprobación de cierre |
|---|---|---|
| Sprint Backlog 2 | US03, US29, US30, QA-03, CON-06; tarjetas S2-01 a S2-06 | Contrastar aceptación funcional con pruebas integradas y estado real del tablero |
| Desarrollo | PR backend7, Web3/4, Edge4, Monitoring5, Infrastructure5 | Verificar commits actuales y contratos entre propietarios |
| Pruebas | Backend21, Web32, Monitoring40, Edge18; Newman y Pub/Sub local | Completar ejecución de conjunto con gateway real y exportar resultados |
| Ejecución | Configuración e historial, recarga Edge y buffer probados | Monitoreo, alertas, reportes y navegación completa con API real y capturas de pantalla completa |
| Documentación de microservicios | OpenAPI y guías en repositorios | Validar endpoints expuestos contra contratos y capturar documentación ejecutada |
| Despliegue | Docker Edge; proyecto GCP verificado | Stack local completo en construcción; cloud pospuesto por usuario, nunca afirmar despliegue no ejecutado |
| Colaboración | PR y commits David-std2 | Referencias verificadas, sin asignaciones u horas inventadas |
| Kanban | Snapshot con funcionalidad en revisión | Verificar estado/conector disponible antes de atribuir actualización o aceptación |
| Continuidad ADD/C4 | workspace.dsl acumulativo y secuencias existentes | Comparar configuración/historial/eventos efectivos con iteración3, conservar vista anterior acumulada |
| Profesor | Interoperabilidad; estructura apropiada por componente | Gateway simple y adaptación por perfiles; no atribuir hexagonal a todos los servicios |
| Calidad visual | Tokens, botones, Material Icons y mapeo sin flechas en panel | Revisar todas las vistas modificadas, escritorio completo y móvil, no solo recortes |
| Documento | 102 tablas,5 secciones,124 entradas índice | Editar último DOCX localizado, conservar estilos y numeración, renderizar y verificar páginas antes de entregar |

## Hallazgos comprobados

- El endpoint /api/v1/assets/states pertenece a Monitoring; enrutarlo al backend legado de pruebas produce401 y cierre de sesión. La prueba aislada anterior no prueba un fallo de Monitoring ni su correcto funcionamiento.
- ReplicaProvisioning valida UUID de gateway y dispositivo. El mock original usa códigos cortos; el importador adapta ambos a UUID deterministas y preserva identidad numérica y relaciones dentro del fixture aislado.
- La importación con adaptación de gateways se ejecutó correctamente:29 activos,16 dispositivos,3255 lecturas. No se cambiaron datos reales8080/3306.
- ReplicaProvisioning aún debe contrastarse con las revisiones de fuente existentes: importar solo dispositivo/rangos no demuestra recuperación de su historial. Cualquier corrección requiere prueba de réplica nueva, entrega duplicada y rollback.
- Build Docker activo sesión61518, log full-stack-build.log. No reiniciar por un timeout de observación: consultar el mismo proceso.

## Estado verificado posterior

| Requisito | Evidencia actual | Resultado |
|---|---|---|
| Recorrido real | integrated-ui-results.json; cuatro rutas vía Gateway | Pasa: sesión, HTTP y JS; sin overflow de página |
| Capturas completas | integrated-*-desktop.png y Monitoreo móvil | Revisadas; Alertas corregida, Monitoreo capturado tras carga |
| Datos del trabajo original | legacy-fixture-import.json | 29 activos,16 dispositivos,3255 lecturas adaptadas; datos aislados |
| Configuración y sustitución | API/Postman y UI; historial MQTT/HTTP | Implementada y probada |
| Recuperación de historial | history-bootstrap-runtime.json | Dos llamadas reales de provisioning conservan exactamente revisiones1/2 |
| Pruebas servicios | source-history-recovery-java21.log |42 Monitoring+2shared pasan;40MySQL/H2 de corte anterior |
| Frontend | ui-review-tests.log; ui-review-build.log |32 pruebas+build pasan; CI41894117893 success |
| CI Monitoring | GitHubActions41894273975 |Success con commit a12388f |
| C4 | DSL validado CLI; tres PNGIt3 regenerados | ExportaciónporStructurizr; rutasajustadas; conservarlayoutfuente |
| Word | current-document-audit.json; PDFfinal |102 tablas,5secciones,124TOC; estilos/fuentes/numeraciónintactos;157p |
| Publicación | Report b4ac7dd; Backend0f7d03d; Web094b4f4; Monitoring a12388f |Solo Veltis-Software |
| Kanban | Lectura real Trello04nov |S2-01/02/03/04/06 en revisión;S2-05 en progreso |

## Trabajo que impide afirmar cierre integral

- La prueba adicional de rollback transaccional sigue en ejecución Java21 (history-rollback-tests.log); no se suma al resultado aprobado de42 hasta observar el resultado.
- Cloud fue pospuesto por el usuario, quien autoriza únicamente recursos gratuitos. El informe describe configuración objetivo y ejecución local; no acredita revisionesCloudRun inexistentes.
- La lectura del tablero no acredita aceptación del equipo. No se inventan responsables, horas, revisiones humanas ni video.
- Verificar las páginas C4 del último PDF al tamaño de lectura y comparar las secuencias con la operación completa de administración de perfiles antes de declarar la revisión final terminada.
