# Sprint 2

## Objetivo y backlog

Incorporar fuentes compatibles conservando identidad, significado e historial por
activo. El incremento incorpora perfiles y adaptadores Edge, administración y
consulta de asociaciones, y validación de revisiones efectivas en Monitoring.

| Task | Alcance | Estado |
|---|---|---|
| S2-01 | Perfiles MQTT/HTTP y normalización Edge | En revisión |
| S2-02 | Contrato canónico y trazabilidad persistente en Monitoring | En revisión |
| S2-03 | Asociación/sustitución autorizada e historial | En revisión; recorrido local verificado |
| S2-04 | Consulta y vista de configuración de fuente | En revisión |
| S2-05 | Despliegue incremental cloud | En progreso |
| S2-06 | Informe y evidencias | En revisión |

Tarjetas y enlaces verificables: [trello-sprint2.json](evidence/trello-sprint2.json).
Sincronización posterior de asociaciones y consulta:
[trello-source-configuration.json](evidence/trello-source-configuration.json).

## Desarrollo

Edge `db38ac3`: SourceRegistry, normalización, pipeline, adaptadores y contrato.
[PR #3](https://github.com/Veltis-Software/coldtrace-edge-gateway/pull/3).
Infrastructure `e94de98`: configuración de proyecto y preflight.
[PR #4](https://github.com/Veltis-Software/coldtrace-infrastructure/pull/4).
Arquitectura acumulativa y ADR-0016:
[Backend PR #6](https://github.com/Veltis-Software/coldtrace-backend/pull/6).
Monitoring `7492a48`: contrato canónico, migración V8, contexto persistido y
eventos compatibles. [PR #4](https://github.com/Veltis-Software/coldtrace-monitoring-service/pull/4).

Asset Management conserva sus agregados y reglas de organización/ubicación. La
continuación añade configuración versionada de fuentes, sustitución con historial,
control de concurrencia y outbox transaccional, sin reescribir los CRUD existentes.
[Backend PR #7](https://github.com/Veltis-Software/coldtrace-backend/pull/7).
La pantalla restaurada de Activos / Dispositivos IoT integra consulta y edición
de perfiles, unidades, campos e historial, con los mismos permisos de la aplicación.
[Web PR #3](https://github.com/Veltis-Software/coldtrace-web-app/pull/3).

La API publica un documento compatible con SourceRegistry para aprovisionamiento
de Edge. Se cargó la exportación real con el SourceRegistry existente: 39,2 °F
se convirtió a 4 °C y el identificador anterior fue rechazado.
[Verificación](evidence/source-export-edge-verification.json).
Edge `cffe2e0` revalida el archivo de perfiles y aplica la sustitución sin alterar
SQLite ni sus lotes. [PR #4](https://github.com/Veltis-Software/coldtrace-edge-gateway/pull/4).
Monitoring `fac3875` proyecta revisiones consecutivas, deduplica eventos y comprueba
la asociación efectiva en la fecha de captura. [PR #5](https://github.com/Veltis-Software/coldtrace-monitoring-service/pull/5).
Infrastructure `75fc818` configura el tópico y la suscripción local de fuente.
[PR #5](https://github.com/Veltis-Software/coldtrace-infrastructure/pull/5).
La distribución por archivo utiliza reemplazo atómico del perfil exportado en un
directorio de configuración montado en solo lectura. El despliegue cloud conserva
su autenticación y aprovisionamiento específicos.

## Pruebas

16 pruebas Python satisfactorias, incluidas seis regresiones y 100 mediciones por
perfil. Se verifican unidades y UTC, identidad configurada, rechazo sin secuencia
ni escritura, HTTP autenticado y estabilidad del lote tras reiniciar. Los contratos
se prueban con datos simulados; no se atribuyen resultados de dispositivos físicos.

La continuación S2-02 ejecuta 31 pruebas de Monitoring sin fallos sobre H2 y sobre
una instancia aislada MySQL 8.0.40. Se aplicaron las ocho migraciones, incluida V8.
Las pruebas verifican persistencia de origen/perfil, contexto en eventos, rechazo
atómico, reintentos con hashes del Sprint 1 y evaluación equivalente de cien
lecturas por perfil. La última validación REST estricta también rechaza versiones
decimales, cadenas, booleanos y desbordamientos. Resultados:
[monitoring-canonical-verification.json](evidence/monitoring-canonical-verification.json).

La continuación de asociaciones ejecuta 21 pruebas backend sobre MySQL 8.0.40:
historial, bloqueo de ediciones concurrentes, rollback conjunto de dispositivo,
configuración, historial y outbox, permisos, organización y contrato REST estricto.
El cliente ejecuta 28 pruebas y compila para producción. La colección Postman de
configuración ejecuta cinco peticiones y ocho aserciones sin fallos contra la API
real autenticada; verifica consulta, historial, conflicto, aislamiento y exportación.
[Resultado Newman](evidence/newman-source-configuration.json).
Auditoría de dependencias del cliente: cero vulnerabilidades altas/críticas y
16 moderadas; Vite y Undici se fijan en parches compatibles mediante overrides.
[Auditoría](evidence/source-web-audit.txt).

## Ejecución

El recorrido real por el emulador de Google Pub/Sub entregó dos revisiones a
Monitoring ejecutado contra MySQL 8.0.40. Reenviar el primer evento no creó otra
revisión. La ingesta aceptó dos lecturas, incluida una capturada antes del cambio;
un lote que incluía la fuente retirada devolvió 409 sin alterar lecturas, lotes ni
Outbox. El reintento del lote válido confirmó dos duplicados.
[Resultado del recorrido](evidence/source-flow-pubsub-verification.json).

La recarga de Edge se ejecutó también en su imagen Docker: lectura inicial con
secuencia 1, reemplazo HTTP en °F con secuencia 2 y rechazo 400 del identificador
retirado. Ambas lecturas quedaron en SQLite y el lote inicial mantuvo su payload.
[Resultado Docker](evidence/source-reload-docker-verification.json).

La suite de Monitoring alcanza 40 pruebas sin fallos sobre H2 y sobre MySQL,
incluida la recepción por el adaptador push local; se aplicaron nueve migraciones.
Edge ejecuta 18 pruebas en Python 3.12/Linux y el bootstrap de infraestructura
dos pruebas de contrato. Las ejecuciones anteriores se conservan como evidencia
histórica del incremento; los resultados actuales están en `source-sync-*`,
`source-reload-linux-tests.txt` y `source-routing-tests.txt`.

La colección Postman del repositorio Edge ejecutó cuatro peticiones y seis
aserciones con Newman, sin fallos. Ver [resultado](evidence/newman-source-input.json).
39,2 °F se normaliza a 4 °C y los rechazos no consumen secuencias. El HTTP 202 de
ingreso confirma almacenamiento en Edge; el envío cloud tiene confirmación propia.

## Documentación

Capturas reales del flujo de reemplazo en escritorio y móvil, con datos de prueba
de una organización frigorífica en una base aislada:
[escritorio](evidence/source-configuration-desktop.png),
[móvil](evidence/source-configuration-mobile.png).
Se verificó MQTT/°C → HTTP/°F con identidad de dispositivo y activo conservadas.
El backend documenta API, esquema aditivo y límites de integración en
`docs/source-configuration.md` y conserva su colección Postman bajo `tests/`.

Edge contiene `contracts/source-input.openapi.json`,
`tests/source-input.postman_collection.json` y `docs/source-integration.md`.
El diseño del recorrido completo aparece en las vistas C4 y secuencias del informe.
Monitoring documenta el contrato aditivo y la compatibilidad de reintentos en
`docs/canonical-readings.md`; OpenAPI se genera desde la aplicación y sus campos
canónicos se comprueban en la suite de integración.

## Despliegue

La imagen Docker de Edge compila y CI pasa. El proyecto `veltis-coldtrace-dev`
(`311618880556`) está activo, con facturación vinculada. La región objetivo es
`southamerica-west1`. Ver [preflight](evidence/gcp-project-preflight.json).
La preparación del proyecto no constituye un servicio desplegado en Cloud Run.
La integración requiere publicación autenticada, push OIDC, secretos y una base
MySQL dimensionada. Edge conserva SQLite persistente en el local del cliente.

## Colaboración

Los commits del incremento están registrados a nombre de David Joel Morales
Venegas y publicados mediante David-std2. Las PR separan las revisiones por
repositorio. Las contribuciones y aceptación del resto del equipo se registran
cuando se producen; no se asignan retroactivamente.

## Kanban

[Tablero del equipo](https://trello.com/b/3tf7nnux/fundamentos). Los incrementos
funcionales y el informe están en revisión; el despliegue está en progreso.
El archivo de evidencia conserva la consulta del corte y sus enlaces de tarjeta.
El 4 de noviembre se sincronizaron S2-02, S2-03 y S2-04 a revisión, sin asignar
responsables ni horas. S2-05 continúa en progreso. El informe del Avance 3 incorpora
el recorrido local, las ocho subsecciones del sprint, pruebas y capturas. Conserva
102 tablas y cinco secciones; su índice contiene 124 entradas actualizadas.
La auditoría de preservación verifica que los estilos, fuentes, numeración,
capturas anteriores y contenido previo al Sprint 2 se mantienen, salvo la fila
de versión y los números de página del índice.
[Auditoría](evidence/sprint2-document-preservation-final.json).

## Verificación integrada del incremento

El recorrido por Gateway18080 verificó Activos, Monitoreo, Alertas y Reportes sin
errores de sesión, servidor o JavaScript y sin desbordamiento horizontal:
[informe del navegador](evidence/integrated-ui-results.json). Las capturas completas
están en `integrated-*-desktop.png`; Monitoreo incluye su captura móvil.
El fixture reutiliza `server/db.json`: 29 activos, 16 dispositivos y 3255 lecturas,
con adaptación de relaciones, UUID, unidades admitidas y fechas para el entorno
local. No se importaron credenciales ni aprobaciones del conjunto anterior.
[Procedencia y transformaciones](evidence/legacy-fixture-import.json).

La ingesta real aceptó 12 lecturas y el aprovisionamiento repetido recuperó las dos
revisiones de una fuente sin duplicarlas:
[ingesta](evidence/integrated-telemetry-seed.json),
[recuperación](evidence/history-bootstrap-runtime.json).
La suite Java21 pasó 42 pruebas Monitoring y dos de biblioteca compartida;
Web pasó32 pruebas y build. Estos resultados complementan la ejecución previa
de40 pruebas Monitoring en MySQL8.0.40; no representan una prueba cloud.
El documento conserva102 tablas,5 secciones y124 entradas de índice:
[auditoría](evidence/current-document-audit.json).
