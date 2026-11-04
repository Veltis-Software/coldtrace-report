# Sprint 2

## Objetivo y backlog

Incorporar fuentes compatibles conservando identidad, significado e historial por
activo. El primer incremento implementa perfiles y adaptadores de Edge; US03,
US29 y US30 continúan hasta integrar administración y consulta de asociaciones.

| Task | Alcance | Estado |
|---|---|---|
| S2-01 | Perfiles MQTT/HTTP y normalización Edge | En revisión |
| S2-02 | Contrato canónico y trazabilidad persistente en Monitoring | En revisión |
| S2-03 | Asociación/sustitución autorizada e historial | En revisión; distribución integrada en curso |
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
La administración y su outbox están implementados; la distribución remota
y el rechazo de una fuente retirada en el recorrido completo siguen formando parte
de la integración. Registrar una configuración no actualiza un agente en ejecución.

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

[Tablero del equipo](https://trello.com/b/3tf7nnux/fundamentos). S2-01 y el informe
se revisan; las siguientes tareas están en backlog y el despliegue está en progreso.
El archivo de evidencia conserva la consulta del corte y sus enlaces de tarjeta.
El 4 de noviembre se sincronizaron S2-02, S2-03 y S2-04 a revisión, sin asignar
responsables ni horas. S2-05 continúa en progreso. El Word del Avance 3 conserva
su corte documental anterior; estos resultados posteriores se registran aquí y
en el plan para incorporarlos al siguiente corte del informe.
