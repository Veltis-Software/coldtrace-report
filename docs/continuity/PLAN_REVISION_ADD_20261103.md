# Plan de continuidad para revisión integral de ColdTrace

## Objetivo y autorización

Revisar y corregir el último informe TP1 con un relato académico coherente: gap y propuesta de valor enfocados en adopción gradual e integración de fuentes heterogéneas; disponibilidad, rendimiento e interoperabilidad como drivers ADD. Mantener usabilidad como requisito y preservar las funcionalidades ya realizadas. Actualizar escenarios, decisiones, iteraciones y diagramas afectados. No implementar Sprint 2 todavía. Repositorios al final; cualquier publicación exclusivamente en Veltis-Software con David-std2.

## Fuentes de verdad

- Informe más reciente entregado por el usuario: `C:/Users/david/Downloads/upc-pre-202602-si657-9199-veltis-report-tp1.docx` (11858757 bytes al iniciar). NO sustituir por el antiguo corregido de Claude.
- Conversación de exposición: `C:/Users/david/.codex/attachments/acfa217d-4cff-4d06-9ef1-8b0f2e150b66/Texto pegado.txt`. Es contexto y propuestas; contrastar hechos y afirmaciones técnicas.
- Materiales oficiales: `C:/Users/david/Downloads/FAS/`; cronograma, enunciado, rúbrica y materiales ADD/tácticas. Extracciones previas en FAS/revision-codex.
- Arquitectura previa y ADR: `C:/Users/david/Downloads/coldtrace-handoff-review-20261009/coldtrace-architecture`.
- Implementación más actual: `C:/Users/david/IdeaProjects/coldtrace-services/sprint1/` y frontend en `C:/Users/david/IdeaProjects/coldtrace-sprint1-repositories/coldtrace-web-app`. Algunas otras copias de repos están atrasadas: comprobar commits y remotos antes de inferir capacidades.

## Reglas editoriales obligatorias

1. Editar una copia del DOCX existente; conservar original intacto. No regenerar documento ni normalizar estilos globales.
2. Preservar fuente, tamaño, color, estilos, sangría, alineación, espaciado, interlineado y formato de cada tabla; clonar propiedades locales cuando se agregue contenido.
3. Texto final autónomo y continuo. Sin explicaciones de corrección, notas defensivas, comparaciones con drivers anteriores o referencias al chat. Justificaciones normales dentro de matrices y ADD sí corresponden.
4. No inventar entrevistas, resultados, dispositivos físicos probados, despliegues, pruebas o porcentajes cumplidos. Describir requisitos con lenguaje normativo y diseño con lenguaje de diseño; describir Sprint 1 con sus evidencias reales. Las limitaciones necesarias se comunican fuera del informe o se expresan como alcance técnico sin muletillas repetidas de pendiente.
5. No borrar usabilidad del producto ni reescribir historia real del Sprint 1: asignación/deshacer/contexto sí se implementaron y probaron.
6. Hexagonal donde aporta separación entre reglas y adaptadores. Gateway de enrutamiento/configuración no requiere un dominio artificial. No llamar monolito a un servicio sencillo para explicar su estructura interna. No reconstruir servicios por esta revisión.
7. Clasificación del curso: explicitar despliegue, estructura interna, dominio y comunicación. Microservicios también es organización global; no afirmar que técnicamente solo puede clasificarse como comunicación. Alinear la presentación de categorías con el material oficial.

## Secuencia y checklist

- [x] Guardar este plan antes de cualquier modificación del informe.
- [x] Copia de trabajo, hash y auditoría de estilos/tablas/imágenes/secciones; extraer mapa de párrafos, tablas, relaciones e imágenes.
- [x] Leer completo el adjunto del chat y los apartados relevantes del informe más reciente; localizar gap, hipótesis, competidores, entrevistas, backlog, principios, estilos, drivers, QA, concerns, tácticas, ADD, figuras, conclusiones y Sprint 1.
- [x] Revisar fuente oficial de tácticas de interoperabilidad y sustento de adaptadores/contratos. Formular escenario de seis partes medible, consistente con fuentes admitidas y sin fingir medición física.
- [x] Mapa de cambios: IDs existentes, referencias cruzadas, tablas y figuras afectadas. Evitar sustituciones globales de palabras.
- [x] Reformular gap como integración y respuesta operacional en pequeños negocios, sin garantizar compatibilidad universal ni ventaja competitiva ya medida. IA como apoyo supervisado según alcance real.
- [x] Revisar matriz de drivers y QA-03: interoperabilidad, formatos/unidades/tiempos/identidades, adaptación MQTT/HTTP y contratos versionados. Determinar valores de aceptación explícitos como requisitos del diseño, no resultados obtenidos.
- [x] Revisar tácticas y tercera iteración ADD (goal, backlog, elementos, conceptos, asignación, interfaces, vistas, decisiones y evaluación) para interoperabilidad. Preservar flujo de atención como capacidad funcional, fuera de la iteración prioritaria si corresponde.
- [x] Corregir sobreafirmaciones existentes: min-instances no es redundancia activa; tópicos separados no garantizan prioridades; OAuth/Stripe no sustituyen autorización; calibración no la garantiza interoperabilidad; no exigir hexagonal a cada ejecutable.
- [x] Extraer y revisar todos los diagramas afectados; localizar fuentes editables. Regenerar solo los necesarios con aspecto consistente y reemplazar medios manteniendo marcos, anclajes, captions y relaciones. No usar imagen generativa para diagramas técnicos.
- [x] Aplicar cambios por lotes conservando runs/propiedades locales; añadir una versión al historial solo si coherente con estructura existente, sin notas narrativas en cuerpo.
- [x] Renderizar con runtime empaquetado y revisar cada página; comparar con línea base para detectar cambios de formato, cortes, tablas, captions, TOC, referencias y figuras. No entregar sin QA visual.
- [x] Auditoría final semántica y estructural: driver consistente en todo informe; ningún resultado inventado; Sprint 1 fiel a código; ningún residuo de usabilidad como tercer driver prioritario; usabilidad funcional preservada.
- [x] Entregar DOCX corregido. Registrar cambios técnicos en este plan, fuera del documento.
- [x] Después: proponer Sprint 2 y evidencias (Avance 3/S10); despliegue incremental según indicación docente. Actualizar repos/documentación después de cerrar revisión, con remotos verificados.

## Herramientas y recuperación

Skill documents leído: `C:/Users/david/.codex/plugins/cache/openai-primary-runtime/documents/26.1030.10813/skills/documents/SKILL.md`. Usar edición localizada python-docx/OOXML según necesidad de conservar formato y render obligatorio.

Resolver runtime con herramienta load_workspace_dependencies; fallback conocido `C:/Users/david/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`. Usar LibreOffice empaquetado, NO el instalado de escritorio. Guardar scripts, mapas y QA en `C:/Users/david/Downloads/veltis-report/revision-add-20261103/`.

## Estado al guardar

2026-11-03: plan creado. No se modificó el informe. Se verificó existencia/tamaño de la fuente y se leyó el contexto aportado; lectura integral y auditoría aún por hacer. Si una cuota interrumpe, continuar por checklist e inspeccionar archivos de trabajo antes de repetir operaciones.

## Progreso 2026-11-03 (edición en curso)

- Fuente auditada: SHA256 92b065afac4ec63490f725d00a0996b04d271f16b82093972af83c99d69b72e1; 94 tablas, 40 imágenes, 5 secciones, 3645 párrafos.
- Trabajo en `revision-add-20261103/`: mapa completo paragraphs.json/txt, medios originales, baseline.pdf (142 páginas), patch_report.py reproducible, change-log.json (203 párrafos), diagrams/ con SVG y PNG de figuras 20 y 21.
- Documento candidato `ColdTrace_informe_revisado_ADD.docx`; NO entregado todavía. Driver QA-03 e Iteración 3 sustituidos coherentemente por interoperabilidad; historias primarias de integración US03/29/30, Sprint 1 conserva sus nueve historias reales/42SP. Tácticas del material Tacticas.pptx: Discover Service, Tailor Interface, Orchestrate. Se mantiene registro explícito, sin inventar descubrimiento automático.
- Auditoría estructural: los 3645 párrafos originales conservan exactamente sus pPr y rPr; ninguna modificación de estilos globales. 94 tablas y 40 medios; fila 3.1 clonada del registro de versiones (+6 párrafos). Solo document.xml y dos imágenes cambian dentro del paquete.
- Renderizador empaquetado no encuentra LibreOffice; NO usar LibreOffice instalado. Alternativa disponible y usada: Word.Application COM, documento ReadOnly, ExportAsFixedFormat PDF, cerrar sin guardar. Baseline y candidato renderizados con Word; candidato 144 páginas. Raster con Python empaquetado/pypdfium2 en curso.
- Falta QA visual completo, índice paginado (cached TOC original desactualizado), referencias de estados ADD revisadas otra vez, y cotejar imágenes con su marco. Algunos diagramas nuevos necesitan verificar legibilidad en Word, no solo SVG. Guías fuente en diagram_sources.py y render_diagrams.cjs.
- No se ha cambiado código ni publicado repositorios. No afirmar cumplimiento de QA-03: es escenario de diseño. No modificar datos de Sprint 1 para aparentar implementación de normalización aún inexistente.

## Cierre de la revisión documental

- Entregable: `C:/Users/david/Downloads/upc-pre-202602-si657-9199-veltis-report-revisado-add.docx`.
- SHA256 final: `9b585b0f002c1e538e596d61fa1c0092d9ed30c69d3a29c8c5e3257ddaab86e1`.
- Se editaron 219 párrafos de forma localizada, más la caché de 115 entradas válidas del índice. Historial con una fila 3.1; Student Outcome mantiene sus criterios y estructura con redacción continua, sin avisos al editor.
- QA final: 144 páginas exportadas con Word y rasterizadas con Poppler empaquetado. Se revisaron todas las hojas de contacto y las páginas clave a escala completa. PDFium produjo anomalías visuales de fuentes en algunos PNG; usar los de `render-poppler`, NO los de `render` para cotejo. PDF y DOCX nativos correctos.
- 94 tablas, 40 imágenes, 5 secciones. Solo cambian `word/document.xml` y `word/media/image30.png`/`image31.png` en el paquete. Fuentes, tamaños, estilos, interlineado, sangrías, justificación y propiedades de runs originales se conservan. Única propiedad de párrafo modificada: nivel de esquema de una frase que estaba incluida por error como encabezado en el índice. Se ajustan cinco colores de selección de drivers usando la paleta existente.
- Se retiraron del índice cuatro entradas obsoletas: una frase de cuerpo y tres referencias a secciones ausentes que producían marcadores indefinidos. Se conservan campos y enlaces internos de las entradas válidas.
- La prioridad ADD es disponibilidad/rendimiento/interoperabilidad. US03, US29 y US30 refinadas para perfiles, sustitución y configuración. El Sprint 1 conserva sus nueve historias, resultados y evidencias históricos; no se acredita la ejecución de la nueva suite QA-03.
- Material gráfico: `diagrams/image30.svg`, `image31.svg` y PNG utilizados. `iteration3.dsl` y `iteration3.puml` son fuentes complementarias para integrar después en el repositorio; las imágenes entregadas se renderizaron de los SVG, no desde Structurizr.
- El original permanece intacto. No se modificó ni publicó código ni se inició Sprint 2. Próxima fase: acordar alcance Sprint 2, incorporar documentación/ADR y fuentes gráficas a repos Veltis-Software, implementar interoperabilidad conforme al escenario y preparar evidencias del Avance 3.

## Nueva fase autorizada 2026-11-03

Solicitud: corregir diagramas como evolución acumulativa de las iteraciones anteriores, recuperar pantallas finales de exposición, auditar/cerrar Sprint 1 y después comenzar Sprint 2 en repos y documentación.

- [x] Localizar fuentes Structurizr originales y cotejar elementos/relaciones de iteraciones 1, 2 y 3; conservar identidad y estilo; renderizar evolución, no reemplazar arquitectura por un esquema aislado.
- [x] Recuperar imágenes finales de pantallas/prototipos de la presentación y reemplazar las antiguas en informe, conservando formato y verificando correspondencia.
- [x] Auditar Sprint 1 contra ocho subsecciones, pruebas, historias y estado real de ramas/remotos. No asumir cierre por texto del informe.
- [ ] Cerrar brechas verificables de Sprint 1 antes de nuevas funcionalidades; registrar bloqueos externos reales sin inventar evidencias.
- [x] Definir e iniciar Sprint 2 conforme cronograma, backlog y ADD actualizado; código, pruebas y documentación trazables en Veltis-Software exclusivamente.
- [x] Renderizar y revisar informe actualizado; registrar commits, pruebas, entregables y siguiente paso aquí.

Orden vigente: revisión gráfica/documental -> auditoría y cierre Sprint 1 -> Sprint 2. La indicación anterior de no iniciar Sprint 2 queda sustituida por esta autorización.

## Checkpoint de continuidad y primer incremento Sprint 2

2026-11-03, 19:25 America/Bogota.

- Base vigente localizada: Downloads/upc-pre-202602-si657-9199-veltis-report-av3.docx, con ajustes de formato del usuario. La copia revisado-add fue retirada de Downloads; el candidato anterior sigue conservado. No sobrescribir av3 abierto por el usuario. Trabajo actual: revision-continuidad-20261103/ColdTrace_avance3.docx.
- Fuentes originales C4 encontradas en coldtrace-services/docs/architecture/diagrams/c4/workspace.dsl. Se mantienen vistas It0, It1 e It2 y sus identificadores DSL; se agregan It3_Contenedores, It3_Componentes_Monitoring e It3_Componentes_Edge. Renderer real Structurizr CLI v2025.11.09 -> sitio estático -> API del renderer browser; no SVG manual. render_c4.cjs usa Chrome local headless y runtime Node empaquetado. Dos secuencias PlantUML separadas conservan estilo Arial/azul/verde/notas amarillas y permiten leer la continuidad durable/asíncrona. PlantUML v1.2026.9. Archivos nuevos en revision-continuidad-20261103/.
- Capturas restauradas verificadas byte a byte contra PPT final: monitoreo y tres pantallas operativas. verification-summary.json conserva hashes y rutas de medios PPT. Se reemplazan pantallas antiguas y se añade monitoreo; captions ajustados a los datos reales (reporte con 80 lecturas, dos activos, dos incidencias).
- QA documental inicial mostró caption separado y secuencia muy ancha; corregidos mediante keepNext de imagen/caption y dos secuencias. Falta render/QA final e índice paginado tras añadir el avance Sprint 2. Conservar 94 tablas originales; solo clonar estilos al agregar tablas.
- Sprint 1 auditado: Java reactor 46 pruebas (shared 2, Monitoring 25, Alert 10, Gateway 5, Reports 4), backend 3, Web 23, Edge anterior 6; cero fallos. Maven necesitó reintento con IPv4 y comillas en -D; logs finales SUCCESS. No repetir la falsa afirmación de cierre académico completo: video de ejecución, evidencia Postman UI y aceptación/contribuciones del equipo siguen requiriendo evidencia real. Benchmark QA02 y estudio UX no se acreditan por pruebas unitarias. Trello conserva historias en revisión.
- Inicio Sprint 2 acotado y publicado: edge db38ac3, rama feature/us03-source-profile-integration, PR https://github.com/Veltis-Software/coldtrace-edge-gateway/pull/3 . 16 pruebas pasan; 100 medidas por perfil MQTT/HTTP, conversión C/F, UTC, identidad de configuración, rechazo previo a SQLite/secuencia, autenticación HTTP loopback, durabilidad. Newman real: cuatro peticiones, seis aserciones, cero fallos. Docker construido, CI https://github.com/Veltis-Software/coldtrace-edge-gateway/actions/runs/41746216466 SUCCESS. El registro API multi-organización, reemplazo histórico y persistencia canónica Monitoring NO están implementados todavía.
- Infraestructura: e94de98, rama chore/cloud-project-configuration, PR https://github.com/Veltis-Software/coldtrace-infrastructure/pull/4 . gcp/preflight.ps1 ejecutado contra proyecto real ACTIVO con facturación vinculada. Compose valida. No se crearon servicios cloud ni instancias facturables.
- Proyecto creado por usuario y verificado tras gcloud auth login: veltis-coldtrace-dev / 311618880556, nombre Coldtrace v2, región objetivo southamerica-west1. Usar siempre --project explícito; NO cambiar ni tocar tf-complejidad-api. gcloud-project-preflight.json y gcp-project-preflight.json solo metadatos públicos; no tokens.
- Trello accesible por conector. Se crearon S2-01 a S2-06 (IDs/URLs en trello-sprint2.json); S2-01 en revisión, S2-02/03/04 backlog, S2-05/06 progreso. Sin asignar responsables ni horas. S1-Q02 se renombra UX-01 como validación de atención funcional, sin atribuirle QA03 del ADD actual. No marcar aceptación sin equipo.
- Backend: rama docs/architecture-interoperability desde feature/add-stories-completion (3c2cac1). Solo documentación actualizada, ADR0016 y punteros submódulo previstos. ATENCIÓN: origin/develop contiene otras funcionalidades de IA de otros trabajos/colaboradores; no resetear, no mezclar ni reescribir. PR documental sobre feature/add-stories-completion para aislar cambios; la PR5 de Sprint1 hacia main sigue abierta.
- Report repo: rama feature/architecture-continuity desde feature/tp1-evidence, sin cambios publicados todavía. Falta agregar informe final, diagramas editables, evidencia y Sprint2, crear PR y actualizar este cierre.

Siguiente orden: completar sección 5.3.2 con hechos actuales y backlog real, sincronizar fuentes/ADR y evidencias, actualizar TOC sin estilos globales, render Word COM read-only + Poppler, inspección de todas las páginas y auditoría de formato, publicar documentos/PRs solo Veltis-Software, entregar DOCX. Continuación técnica después: S2-02 canónico Monitoring -> S2-03 asociaciones -> S2-04 UI -> integración cloud con OIDC y presupuesto MySQL definido; no fingir que 16 pruebas cierran las historias ni el SLA.

## Cierre del corte documental y arranque Sprint 2

- DOCX de entrega: `C:/Users/david/Downloads/upc-pre-202602-si657-9199-veltis-report-av3-actualizado.docx`.
- SHA256: `0363b64beca2524f852c1452f6d88b80e23bceb84e246d87643a19dc5c0c3f5f`.
- Fuente av3 intacta; portada idéntica. Una fila 3.2 añadida al registro de versiones, identificado por su encabezado (no por posición de tabla). El QA intermedio detectó una inserción en tabla equivocada y se corrigió antes de entregar; la auditoría final exige igualdad de todas las tablas originales excepto ese registro, con exactamente una fila adicional.
- Informe final: 154 páginas, 102 tablas (94 originales + 8 de Sprint 2), cinco secciones. 124 entradas enlazadas del índice actualizadas; se reparó un marcador existente de una sección real. Sin marcadores indefinidos. Párrafos y runs originales con propiedades idénticas; cuatro párrafos de imagen sustituidos para mantener la relación de aspecto de las nuevas capturas/vistas. Archivo preservation-audit.json es el resultado vigente, no los hashes de renders intermedios.
- Vistas C4 acumulativas: It3_Contenedores y Monitoring contienen todos los elementos de It2. It0, It1 e It2 conservan sus elementos. Auditoría continuity-audit.json. Figura 20a contenedores, 20b Monitoring, 20c Edge; Figura 21a incorporación, 21b continuidad transaccional/asíncrona. Capturas actuales de monitoreo, detalle, asignación y reporte coinciden con el PPT final.
- Se revisó el conjunto de páginas en hojas de contacto y las nuevas vistas, pantallas, tablas, encabezados, portada e índice a escala completa. Se corrigieron encabezados clonados desde TOC y encabezados de tabla aislados antes del corte final. Word COM read-only + Poppler; no se reescribió el paquete mediante Word.
- Verificación ejecutada: 46 tests de servicios/biblioteca Java + 3 backend + 23 Web + 16 Edge (incluyen las seis regresiones originales), todos satisfactorios. Colección Postman repetida sobre contenedor Docker real: cuatro peticiones, seis aserciones, cero fallos. Perfil montado read-only, SQLite en volumen persistente y proceso sin privilegios. Tras dos lecturas válidas y dos rechazos, pending=2/generated=2; no se simula entrega cloud. Contenedor y volumen exclusivos de verificación retirados tras conservar resultados.
- CI Edge e Infrastructure satisfactorios; Backend PR6 verifica código y tres imágenes con éxito. Backend docs commit 104cc9e, PR https://github.com/Veltis-Software/coldtrace-backend/pull/6, base feature/add-stories-completion. La PR5 de migración anterior sigue separada.
- Trello: 61 tarjetas tras agregar seis de Sprint 2. S2-01 y S2-06 en revisión; S2-02/03/04 por hacer; S2-05 en progreso. S1-D01 pasa a revisión documental. S1-D03 pasa a progreso con proyecto real registrado. Las nueve historias funcionales del Sprint 1 siguen en revisión de aceptación; no se atribuyen horas, usuarios o contribuciones ficticias.
- El cierre académico completo de Sprint 1 NO se acredita todavía: el equipo debe registrar el video, la evidencia específica de Postman UI y su aceptación/contribuciones. Las pruebas disponibles no sustituyen esos requisitos. El incremento técnico está probado y se conserva mientras comienza la base de interoperabilidad del Sprint 2.
- Proyecto GCP verificado, cuenta autenticada por el usuario. No se han creado Cloud Run, Cloud SQL ni recursos de cómputo facturables. Preparación real e instrucciones en Infrastructure/gcp. No usar tf-complejidad-api ni cambiar su configuración global.
- Documentación Sprint2 inicial completa como corte de avance en las ocho subsecciones de 5.3.2, sin presentar US03/29/30 como terminadas. Fuentes, contratos, resultados y backlog acompañan a los repositorios. Los scripts temporales de edición/render y herramientas descargadas permanecen fuera de los repositorios.

### Próxima continuidad técnica

1. S2-02: validar contrato canónico, conservar sourceId/profileVersion/unidades en Monitoring y probar equivalencia con su evaluación real; no alterar el comportamiento de versiones anteriores sin migración compatible.
2. S2-03: aprovechar Asset Management; asociaciones activas autorizadas por organización, sustitución e historial. Revisar estado actual de otros branches antes de editar; no reemplazar trabajo de otros integrantes.
3. S2-04: consulta de configuración y evolución de la interfaz existente, conservando diseño restaurado y fuentes de datos.
4. S2-05: publicar/recibir Pub/Sub con autenticación real, identidades/Secret Manager, base MySQL y despliegue funcional. Preparar costos concretos y límite autorizado antes de aprovisionar Cloud SQL/instancias continuas; no prometer que Cloud SQL pertenece al free tier.
5. Registrar evidencia real de equipo/video/aceptación y actualizar el informe sobre la copia vigente con el mismo procedimiento localizado y QA. Mantener plan, Trello y commits trazables.


## Publicación verificada

- Informe y evidencias publicados en `feature/architecture-continuity`, commit inicial `0701ba2`, PR https://github.com/Veltis-Software/coldtrace-report/pull/2 sobre `feature/tp1-evidence` (PR1 previa conservada). Documento del repositorio y copia Downloads tienen el mismo SHA256 final.
- Revisiones publicadas: Edge PR3, Infrastructure PR4, Backend PR6 y Report PR2. Ninguna subida a la organización anterior. Autenticación GitHub David-std2.
- Las verificaciones de CI de Edge, Infrastructure y Backend concluyeron satisfactoriamente. El repositorio del informe conserva auditorías de formato, índice, continuidad, hashes de capturas y ejecuciones verificadas.
- Las PR quedan abiertas para revisión; no se forzó ninguna mezcla de ramas ni se reescribió historial. El cierre pendiente del checklist se refiere a evidencias académicas de Sprint1 que requieren registro y aceptación reales del equipo.

## Continuación S2-02
Inicio: validar metadatos canónicos completos o legado sin metadatos; migración V8 nullable, persistencia y eventos, rechazo atómico, fingerprint legado compatible. Rama Monitoring feature/canonical-reading-contract. No modificar evaluación de rango ni afirmar cierre de asociaciones/US29/US30.

### S2-02 implementado y verificado

2026-11-03: Monitoring commit 7492a48, rama feature/canonical-reading-contract, PR https://github.com/Veltis-Software/coldtrace-monitoring-service/pull/4 (base feature/add-stories-completion; la PR3 anterior sigue separada).

- Se aceptan lecturas legado sin contexto o contexto canónico completo: sourceId, profileVersion, schemaVersion=1, C y %RH. Validación en dominio sin dependencias de infraestructura. Versiones REST estrictas: rechaza decimales, cadenas, booleanos y overflow. Rechazo de todo el lote antes de reclamar clave/escribir lecturas o eventos.
- V8 agrega cinco columnas nullable; no reescribe historia. Contexto persistido junto con mediciones y propagado en readings.ingested/threshold.breached. Payload de evento aditivo, sin cambiar nombres/envelope.
- Fingerprint legado conserva exactamente siete campos, orden y nulls de record anterior. Los metadatos canónicos sí participan de la huella; cambiar perfil bajo la misma clave devuelve 409.
- Verificación: 31 tests Monitoring y 2 de biblioteca compartida pasan en H2; 31 Monitoring sobre MySQL 8.0.40 aislado y ocho migraciones aplicadas. El endurecimiento final de versión REST se verificó sobre H2 después de la corrida MySQL; es lógica de parseo sin cambios SQL. Prueba de equivalencia integrada: cien lecturas por fuente, cincuenta normales y cincuenta fuera de rango para cada una, mismas reglas. Se conservan cinco escenarios Gherkin anteriores y regla ArchUnit.
- MySQL local de prueba retirado; no datos ni recursos cloud afectados. Logs originales en revision-continuidad-20261103; resumen de suites y logs sin credenciales en report/docs/sprint-2/evidence/monitoring-canonical-*.
- sourceId es trazabilidad, no identidad autenticada ni asociación validada contra registro remoto. Organización/activo siguen determinados por credencial gateway y device_replica. Asociación/versionado autorizado corresponde a S2-03/S2-04, que siguen pendientes.
- Documentación de servicio README + docs/canonical-readings.md actualizada; Report/docs/sprint-2 registra continuación. Word av3-actualizado conserva el corte previo de 154 páginas; no afirmar que se actualizó con S2-02 en esta continuación.
- Conector Trello retirado durante la sesión; no actualizar por vías no autorizadas ni afirmar sincronización. S2-02 en revisión GitHub; sincronizar estado Trello cuando el conector vuelva.

- Cierre S2-02: CI GitHub https://github.com/Veltis-Software/coldtrace-monitoring-service/actions/runs/41756255025 SUCCESS: Maven verify JDK21, imagen Docker y artefactos de pruebas. El run de push previo fue cancelado automáticamente por la política de concurrencia al abrir PR; no fue fallo de pruebas. Backend fija Monitoring en 7492a48 mediante 037ce0f. Arquitectura y ADR0016 actualizados al estado ejecutado. Siguiente tarea S2-03 asociaciones/historial, seguida de S2-04 consulta y despliegue integrado. Informe Word sigue con el corte anterior; sus fuentes no se alteraron en esta continuación.

## Continuación S2-03 / S2-04

2026-11-03: se amplía Asset Management existente en la rama feature/source-configuration, basada en docs/architecture-interoperability. Asociación vigente por dispositivo y sourceId único por organización; configuración versionada, historial inmutable y outbox en una transacción. La asociación actualiza el activo del dispositivo y valida organización/ubicación del gateway. Los cambios antiguos de identidad/asignación y eliminación se bloquean cuando existe configuración administrada. Se implementará primero API y pruebas; la vista y distribución a Edge/Monitoring se verifican por separado antes de declarar US03/29/30 completas. No se modifica el Word ni se afirma despliegue en este corte.

## Resultado de asociaciones y consulta — 2026-11-04

- Se reutilizan los agregados, puertos/adaptadores JPA, reglas de ubicación y la pantalla de Activos/Dispositivos IoT. Solo son nuevas la configuración versionada de fuente, historial, caso de uso/API y panel incorporado. No se reescriben módulos antiguos.
- Backend feature/source-configuration, commits 7efb325 y d36c1ab, PR https://github.com/Veltis-Software/coldtrace-backend/pull/7 sobre docs/architecture-interoperability. Web misma rama, f74ed71, PR https://github.com/Veltis-Software/coldtrace-web-app/pull/3 sobre feature/restore-operational-ui. David-std2, únicamente Veltis-Software. La autenticación activa había cambiado a David-std; se restableció David-std2 y se verificó publicación. No se subió a la organización anterior.
- API por organización con IAM facade (no controller-to-controller), permisos assets:manage / assets:view / operations:view. PUT exige versión esperada, motivo, perfil MQTT/HTTP, campos distintos, versiones JSON enteras estrictas y unidades C/F + %RH. Mantiene UUID, gateway y activo; también impide mover un dispositivo legado ya asignado. Fuente vigente única por organización; historial no redefine una versión anterior del perfil.
- Una transacción JPA/JDBC guarda asignación, vigente, historial y outbox source.configuration-changed. Bloqueo de fila de dispositivo compartido con CRUD antiguo; constraint único para conflictos entre dispositivos. CRUD antiguo sigue editando metadatos, pero no UUID/gateway/activo ni elimina un dispositivo administrado. No modifica lecturas históricas.
- 21 tests backend sobre MySQL 8.0.40 aislado: incluye concurrencia inicial, rollback, reemplazo, historia, permisos, organización/ubicación, perfil e identidad antigua. Se verificó API real autenticada con Newman: cinco peticiones, ocho aserciones, cero fallos. Se corrigió manejo de ResponseStatusException en el controller para que una denegación 403 no terminara en el error dispatch 401 de la seguridad global existente.
- Frontend: 28 pruebas, build de producción, consulta y reemplazo real por navegador mediante proxy de prueba al API 8088 y MySQL aislado. Escenario ficticio empresarial Frío Pacífico, Lucía Salazar, cámara de lácteos. Reemplazo MQTT/°C a HTTP/°F conserva activo y dos revisiones. Capturas escritorio 1440x1000 y móvil390; panel sin desbordamiento horizontal (330/330). No son sensores físicos ni despliegue cloud.
- Trello volvió disponible: S2-02/03/04 pasaron a revisión con enlaces PR y resultados. Sin asignar usuarios, horas ni marcar aceptación. Se conserva necesidad de distribuir configuración y aplicar fuente retirada en Edge/Monitoring antes de cierre completo de US03/29.
- Export GET gateway/source-profiles coincide con SourceRegistry, aprovisionamiento por operador. No es credencial de dispositivo. Edge no recibe hot reload remoto ni Monitoring consulta aún este registro; no afirmar revocación remota por registrar un cambio. Relay de emulador selecciona evento desde envelope; falta topic/consumidores/autenticación cloud. Proyecto GCP sin nuevos recursos.
- Word av3-actualizado sigue corte anterior de 154 páginas, no se regeneró. Este incremento se registra en Markdown y evidencias del report; integrar al siguiente corte con edición localizada y QA de formato.
- CI backend inicial 41777775974 y reactor/contenedores 41777775791 satisfactorios. CI web detectó dependencias high preexistentes; se actualiza lock compatible y overrides undici7.30.1/vite7.3.7 para pasar auditoría sin saltar major de Angular. Repetir tests/build/audit y registrar runs finales.

### Próxima continuidad

1. Verificar CI de los commits finales y documentar hashes/resultados en report.
2. Integrar distribución/aplicación de configuración a Edge y Monitoring: revocación del origen retirado, identidad conservada, compatibilidad con lotes durables anteriores y outbox reintentable. Añadir prueba vertical real antes de cerrar US03/29.
3. Extracción incremental de Asset Management hacia repo dedicado al habilitar su despliegue; reutilizar este código, no reconstruir dominio. Mantener gateway simple.
4. Cloud S2-05: Pub/Sub/OIDC/secretos y MySQL dimensionado exclusivamente veltis-coldtrace-dev. No aprovisionar Cloud SQL de pago sin límite de gasto concreto. Preparar alternativa mínima real sin llamar gratis a Cloud SQL.
5. Actualizar Word con nuevo corte y evidencias reales, conservando OOXML original, diagramas acumulativos, tablas/fuentes/espaciados. Completar pendientes académicos reales de Sprint1 sin atribución ficticia.

### Validación adicional y publicación final del incremento

- Colección Postman en backend/tests/source-configuration.postman_collection.json; cinco peticiones y ocho aserciones pasan contra runtime autenticado. Se declara assetId como variable de entorno sin incluir credenciales.
- Backend HEAD 4ffeb9e, CI Backend 41778438538 SUCCESS y regresión/reactor/imágenes 41778438467 SUCCESS. Frontend HEAD 240838c: lock reconstruido desde manifest limpio para incluir dependencias opcionales Linux ausentes en el lock generado sobre node_modules de Windows. npm ci --dry-run con Node22 Linux pasa. Angular sigue en21 (core21.2.26/build21.2.29); no major upgrade. Tras instalación limpia Windows:28 tests/18files pasan; build/audit finales en verificación.
- La exportación autenticada real de API se cargó directamente con SourceRegistry existente de Edge;39,2°F→4°C y origen retirado rechazado. source-export-edge-verification.json registra el resultado. Esto prueba aprovisionamiento por archivo, no hot reload remoto ni sincronización cloud.
- Evidencia actual en report/docs/sprint-2/evidence: tests backend/web, build/audit, Newman, OpenAPI filtrado a operaciones de fuente, capturas desktop/móvil, hashes y snapshot de seis tarjetas Trello. Word sigue intacto en corte previo.

- Cierre de verificación: Web 240838c, CI 41778998525 SUCCESS (npm ci, auditoría, 28 tests, build e imagen Docker). Backend 4ffeb9e, CI 41778438538 y 41778438467 SUCCESS. Pasan 21 pruebas backend, 28 Web y Newman con cinco peticiones y ocho aserciones. Build limpio Windows satisfactorio tras regenerar el lock. Quedan 16 vulnerabilidades moderadas y ninguna alta/crítica. Sprint 2 no se presenta como cerrado.
- Se retiraron el runtime 8088 y MySQL coldtrace-source-verification, ambos exclusivos de prueba. Backend 8080, GCP y datos reales no se modificaron. El frontend 4202 de verificación se detuvo después de las capturas. Plan y evidencias publicados en Report PR2; Word sin modificación en esta continuación.
