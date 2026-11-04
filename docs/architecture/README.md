# Arquitectura de ColdTrace

El [modelo Structurizr](diagrams/c4/workspace.dsl) contiene el contexto, las
iteraciones 0 a 3 y el despliegue objetivo. Las iteraciones son acumulativas:

| Iteración | Refinamiento | Vistas |
|---|---|---|
| 0 | Límites de servicios, propiedad de datos y gateway | It0_Contenedores |
| 1 | Edge durable, ingesta idempotente y detección de brechas | It1_Contenedores, It1_Componentes_Monitoring |
| 2 | Réplica de rangos, proyección, Outbox y Pub/Sub | It2_Contenedores, It2_Componentes_Monitoring |
| 3 | Perfiles, adaptadores, normalización y contrato canónico | It3_Contenedores, It3_Componentes_Monitoring, It3_Componentes_Edge |

Los [diagramas renderizados](diagrams/rendered) conservan la notación y estilos
del modelo C4 original. Las [secuencias UML](diagrams/uml) muestran recuperación,
procesamiento asíncrono e incorporación de fuentes. `continuity-audit.json` en
las evidencias del Sprint 2 comprueba que los elementos de las vistas anteriores
permanecen en las nuevas vistas acumulativas.

Para regenerar C4, validar `workspace.dsl` con Structurizr CLI, exportar el sitio
estático y utilizar la exportación PNG/SVG del renderer de Structurizr. Los PNG
de la iteración 3 se exportaron con CLI v2025.11.09 y el renderer browser nativo.
Las secuencias se renderizaron con PlantUML v1.2026.9. Los archivos de fuente son
la referencia editable; no se dibujaron vistas C4 independientes en SVG.

La separación de dominio, aplicación y adaptadores se aplica según reglas e
integraciones del servicio. El API Gateway mantiene rutas, filtros y configuración.
Las decisiones de atención funcional del Sprint 1 permanecen en sus ADR; el
[ADR-0016](decisions/ADR-0016-perfiles-y-adaptadores-de-fuentes.md) detalla los
perfiles y adaptadores de interoperabilidad.

El diseño objetivo y la implementación observada se distinguen en el informe y
en el backlog de cada sprint. El primer incremento de interoperabilidad ejecuta
la normalización y persistencia local del Edge; la administración de asociaciones
y validación persistente en Monitoring son tareas posteriores del Sprint 2.
