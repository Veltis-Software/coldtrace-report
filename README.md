# ColdTrace: informe del proyecto

Repositorio de documentación de **ColdTrace**, plataforma SaaS de monitoreo de la cadena de frío desarrollada por **Veltis Software** para el curso Fundamentos de Arquitectura de Software (1ASI0657), Universidad Peruana de Ciencias Aplicadas, ciclo 202620, sección 9199.

| Dato | Detalle |
| --- | --- |
| Docente | Daniel Enrique Mori Yzaguirre |
| Integrantes | Condori Lozano, Alessandro Ramiro<br>Julca Cruz, Renso Anthony<br>Morales Venegas, David Joel |
| Aplicación desplegada | https://coldtrace-web-3zrmheawya-ue.a.run.app |
| Tablero del equipo | https://trello.com/b/3tf7nnux/fundamentos |

## Informe

[Informe del Trabajo Final (DOCX)](informe/upc-pre-202602-si657-9199-veltis-report-tf.docx)

## Arquitectura

| Carpeta | Contenido |
| --- | --- |
| [`arquitectura/c4`](arquitectura/c4) | Modelo C4 en Structurizr (`workspace.dsl`) y vistas de contexto, contenedores y componentes de las iteraciones ADD 0 a 3 |
| [`arquitectura/uml`](arquitectura/uml) | Diagramas de secuencia en PlantUML de cada iteración |
| [`arquitectura/microservicios`](arquitectura/microservicios) | Diagramas de clases y de base de datos de cada microservicio, generados desde el código y las migraciones Flyway |
| [`arquitectura/cloud`](arquitectura/cloud) | Arquitectura de despliegue en Google Cloud |
| [`arquitectura/decisiones`](arquitectura/decisiones) | Registro de decisiones de arquitectura |

Detalle en [`arquitectura/README.md`](arquitectura/README.md).

## Repositorios de la solución

| Repositorio | Responsabilidad |
| --- | --- |
| [coldtrace-web-app](https://github.com/Veltis-Software/coldtrace-web-app) | Aplicación web en Angular |
| [coldtrace-api-gateway](https://github.com/Veltis-Software/coldtrace-api-gateway) | Punto de entrada único (Spring Cloud Gateway) |
| [coldtrace-identity-service](https://github.com/Veltis-Software/coldtrace-identity-service) | Organizaciones, usuarios, roles y sesiones |
| [coldtrace-asset-service](https://github.com/Veltis-Software/coldtrace-asset-service) | Sedes, activos, gateways, dispositivos y rangos seguros |
| [coldtrace-monitoring-service](https://github.com/Veltis-Software/coldtrace-monitoring-service) | Ingesta de telemetría, estado actual y detección de brechas |
| [coldtrace-alert-service](https://github.com/Veltis-Software/coldtrace-alert-service) | Incidencias, notificaciones y atención |
| [coldtrace-report-service](https://github.com/Veltis-Software/coldtrace-report-service) | Reportes de trazabilidad |
| [coldtrace-subscription-service](https://github.com/Veltis-Software/coldtrace-subscription-service) | Planes, suscripciones y facturación |
| [coldtrace-maintenance-service](https://github.com/Veltis-Software/coldtrace-maintenance-service) | Mantenimiento preventivo y solicitudes técnicas |
| [coldtrace-ai-assistance-service](https://github.com/Veltis-Software/coldtrace-ai-assistance-service) | Asistencia con modelos de lenguaje |
| [coldtrace-edge-gateway](https://github.com/Veltis-Software/coldtrace-edge-gateway) | Agente Edge con almacenamiento local y reenvío |
| [coldtrace-shared](https://github.com/Veltis-Software/coldtrace-shared) | Biblioteca técnica compartida |
| [coldtrace-infrastructure](https://github.com/Veltis-Software/coldtrace-infrastructure) | Entorno local con Docker Compose |
| [coldtrace-backend](https://github.com/Veltis-Software/coldtrace-backend) | Aplicación monolítica de referencia para la migración |
