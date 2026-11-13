# Repositorios y despliegue AV4

Comprobación del 12 de noviembre de 2026.

| Repositorio | Participación verificada |
|---|---|
| coldtrace-web-app | Interfaz Angular, historial y CSV en Cloud Run |
| coldtrace-api-gateway | Enrutamiento y autenticación hacia servicios privados en Cloud Run |
| coldtrace-identity-service | Sesiones, organizaciones y permisos en Cloud Run |
| coldtrace-asset-service | Activos, rangos y asociaciones versionadas en Cloud Run |
| coldtrace-monitoring-service | Ingesta, proyección, detección y Outbox en Cloud Run |
| coldtrace-alert-service | Incidencias, acciones, cierre e historial en Cloud Run |
| coldtrace-report-service | Proyecciones y generación de reportes en Cloud Run |
| coldtrace-subscription-service | Permisos del plan consumidos por los servicios en Cloud Run |
| coldtrace-edge-gateway | Agente en el local del cliente, con SQLite y adaptación de fuentes |
| coldtrace-shared | Biblioteca de contratos y utilidades, consumida por las compilaciones |
| coldtrace-infrastructure | Compose, configuración de servicios y aprovisionamiento |
| coldtrace-report | Informe académico y evidencia de ejecución |
| coldtrace-maintenance-service | Código extraído, ejecución local previa; sin servicio cloud en AV4 |
| coldtrace-ai-assistance-service | Código extraído, ejecución local previa; sin servicio cloud en AV4 |
| coldtrace-backend | Referencia histórica y documentación arquitectónica; sin servicio cloud en AV4 |

El repositorio del informe se distingue de report-service, que es una aplicación.
Las ocho aplicaciones desplegadas proceden de sus repositorios propietarios.
La extracción completa de capacidades y su despliegue no se deducen de la existencia de un repositorio.

## Biblioteca compartida

Se identificó que cuatro compilaciones consumían una copia en Infrastructure.
El contrato IdentitySession se publicó en coldtrace-shared, commit
3e791b547df753d0a091da67e60df51a87793abd.
La integración continua de Monitoring, Alert, Report y Gateway consume esa revisión.
Compose usa el repositorio hermano como contexto shared. Se validó su configuración.

## Evidencia técnica

Los resultados y capturas del recorrido se guardan en docs/sprint-3/evidence.
El informe incluye los ocho apartados del Sprint 3 y el registro AV4.
El índice nativo de Word se regeneró con 142 entradas y la exportación tiene 167 páginas.
La prueba cloud aprobada comprende cierre, autor, acciones, filtros, consulta vacía y CSV.
Las sesiones de evaluación de uso con participantes no se han realizado.
