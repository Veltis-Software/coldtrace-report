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
