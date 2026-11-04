# Sprint 2

## Objetivo y backlog

Incorporar fuentes compatibles conservando identidad, significado e historial por
activo. El primer incremento implementa perfiles y adaptadores de Edge; US03,
US29 y US30 continúan hasta integrar administración y consulta de asociaciones.

| Task | Alcance | Estado |
|---|---|---|
| S2-01 | Perfiles MQTT/HTTP y normalización Edge | En revisión |
| S2-02 | Contrato canónico y trazabilidad persistente en Monitoring | Backlog |
| S2-03 | Asociación/sustitución autorizada e historial | Backlog |
| S2-04 | Consulta y vista de configuración de fuente | Backlog |
| S2-05 | Despliegue incremental cloud | En progreso |
| S2-06 | Informe y evidencias | En revisión |

Tarjetas y enlaces verificables: [trello-sprint2.json](evidence/trello-sprint2.json).

## Desarrollo

Edge `db38ac3`: SourceRegistry, normalización, pipeline, adaptadores y contrato.
[PR #3](https://github.com/Veltis-Software/coldtrace-edge-gateway/pull/3).
Infrastructure `e94de98`: configuración de proyecto y preflight.
[PR #4](https://github.com/Veltis-Software/coldtrace-infrastructure/pull/4).
Arquitectura acumulativa y ADR-0016:
[Backend PR #6](https://github.com/Veltis-Software/coldtrace-backend/pull/6).

## Pruebas

16 pruebas Python satisfactorias, incluidas seis regresiones y 100 mediciones por
perfil. Se verifican unidades y UTC, identidad configurada, rechazo sin secuencia
ni escritura, HTTP autenticado y estabilidad del lote tras reiniciar. Los contratos
se prueban con datos simulados; no se atribuyen resultados de dispositivos físicos.

## Ejecución

La colección Postman del repositorio Edge ejecutó cuatro peticiones y seis
aserciones con Newman, sin fallos. Ver [resultado](evidence/newman-source-input.json).
39,2 °F se normaliza a 4 °C y los rechazos no consumen secuencias. El HTTP 202 de
ingreso confirma almacenamiento en Edge; el envío cloud tiene confirmación propia.

## Documentación

Edge contiene `contracts/source-input.openapi.json`,
`tests/source-input.postman_collection.json` y `docs/source-integration.md`.
El diseño del recorrido completo aparece en las vistas C4 y secuencias del informe.

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
