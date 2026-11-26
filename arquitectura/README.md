# Arquitectura de ColdTrace

## Modelo C4

[`c4/workspace.dsl`](c4/workspace.dsl) contiene el contexto, las iteraciones ADD 0 a 3 y el despliegue. Las iteraciones son acumulativas:

| Iteración | Refinamiento | Vistas |
| --- | --- | --- |
| 0 | Límites de servicios, propiedad de datos y API Gateway | It0_Contenedores |
| 1 | Edge con almacenamiento local, ingesta idempotente y detección de brechas | It1_Contenedores, It1_Componentes_Monitoring |
| 2 | Réplica de rangos, proyección de estado, Outbox y Pub/Sub | It2_Contenedores, It2_Componentes_Monitoring |
| 3 | Perfiles de fuente, adaptadores y contrato canónico | It3_Contenedores, It3_Componentes_Monitoring, It3_Componentes_Edge |

Para regenerar las vistas se valida `workspace.dsl` con Structurizr CLI y se exportan los PNG desde el renderer de Structurizr.

## UML

[`uml`](uml) contiene las secuencias de recuperación, procesamiento asíncrono e incorporación de fuentes en PlantUML, junto con su versión renderizada.

## Microservicios

[`microservicios/class`](microservicios/class) y [`microservicios/database`](microservicios/database) contienen los diagramas de clases y de base de datos de cada microservicio de la versión 1.0.0. Se regeneran con Graphviz desde los repositorios clonados en un mismo directorio:

```
python microservicios/tools/class_diagrams.py <directorio-de-repositorios> microservicios/class
python microservicios/tools/database_diagrams.py <directorio-de-repositorios> microservicios/database
```

## Nube

[`cloud`](cloud) describe el despliegue en Google Cloud (proyecto `veltis-coldtrace-dev`, región `us-east1`): Cloud Run, Cloud SQL, Pub/Sub, Secret Manager y Artifact Registry.
