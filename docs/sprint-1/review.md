# Revisión del Sprint 1

El incremento funcional comprende US04, US06, US08, US09, US14, US16, US33,
US46 y US47: estado por activo, desviaciones, atención de incidencias, supervisión,
reporte, brechas y recuperación de lecturas. El backend conserva IAM/Asset y las
capacidades extraídas tienen repositorios y despliegues propios.

La revisión del 3 de noviembre ejecutó 46 pruebas Java de servicios/biblioteca,
3 del backend, 23 de Web y las 6 originales de Edge, sin fallos. Los resultados
y nombres de suites se conservan en [verification-summary.json](../sprint-2/evidence/verification-summary.json).
Las [pantallas finales](screens) coinciden por SHA256 con las imágenes de la
presentación de exposición; el informe ahora usa esas mismas capturas.

| Evidencia del enunciado | Estado comprobado |
|---|---|
| Backlog y desarrollo | Nueve historias implementadas; revisión de aceptación en Trello. |
| Pruebas | Suites indicadas satisfactorias; resultados y CI conservados. |
| Ejecución | Capturas de aplicación, Swagger y ensayos previos disponibles. El video de ejecución y la evidencia específica de Postman UI requieren registro. |
| Documentación | Contratos y endpoints del incremento conservados. |
| Despliegue | Entorno local reproducible y CI. La creación del proyecto cloud se registra en Sprint 2. |
| Colaboración | Commits/PR reales disponibles; aceptación y contribuciones individuales deben ser registradas por el equipo. |
| Kanban | Las historias siguen en revisión, sin inventar responsables ni horas. |

La ejecución de pruebas automatizadas no demuestra por sí sola el benchmark
completo de rendimiento ni la aceptación de las historias por usuarios. El cierre
funcional verificable no equivale al cierre de todas las evidencias académicas.
