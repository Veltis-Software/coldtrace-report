# Guion de exposición de ColdTrace

Corresponde a la presentación de 36 diapositivas, con 35 visibles y una de apoyo oculta. Duración sugerida: 18–22 minutos, incluida una demostración de 3 minutos. Si el tiempo asignado es menor, abrevia los separadores y usa las capturas en lugar de cambiar al navegador. Los nombres y registros de la demostración son datos de ejemplo.

## 1 · Veltis Software y ColdTrace

«Somos Veltis Software y presentamos ColdTrace, una solución para supervisar la cadena de frío y organizar la respuesta ante desviaciones. En este parcial explicamos cómo evolucionamos una solución existente y cómo las necesidades del usuario guiaron la arquitectura mediante ADD.»

## 2 · Contenido

«Partiremos del problema y el backlog. Luego mostraremos el flujo de uso, justificaremos los drivers y las tácticas y explicaremos la arquitectura hasta un componente de código.» No leer cada punto.

## 3 · Presentación del proyecto

Transición breve: «Primero, qué problema resolvemos y para quién». Avanzar.

## 4 · El problema

«Un negocio que conserva perecibles puede detectar tarde una desviación si depende de revisiones presenciales o registros aislados. Además de conocer la temperatura, necesita saber quién atiende el problema y conservar evidencia. Gustavo representa al encargado sin personal técnico; Sofía, a quien supervisa varias ubicaciones y prepara revisiones de calidad.»

No afirmar que todos los negocios funcionan así; describir el segmento estudiado.

## 5 · Propuesta de valor

«Nuestra propuesta combina la supervisión del activo con una respuesta trazable: lectura y rango, alerta, responsable y seguimiento. También distingue una lectura normal de una fuente que dejó de reportar. Proponemos una adopción gradual para negocios alimentarios; la simplicidad y la reducción de transcripción son hipótesis que validaremos con pilotos.»

Si preguntan por competidores: «Ya ofrecen monitoreo y alertas. Buscamos validar el ajuste al flujo operativo y al segmento local, no afirmar que inventamos esas capacidades». IA y suscripciones son evolución prevista.

## 6 · Evolución de la solución existente

«Partimos de un sistema brownfield: conservamos dominio, reglas y capacidades previas. El incremento separa Monitoring, Alert y Reports, incorpora el Gateway y fortalece continuidad, eventos e interacción. IAM y Asset todavía permanecen en el backend durante la migración. Reutilizamos también los componentes visuales existentes, adaptándolos a los contratos de los servicios nuevos.»

Si preguntan qué aporta este curso: explicar decisiones, límites y comportamiento ante fallos; no contar repositorios como prueba de microservicios.

## 7 · Objetivos de negocio

«BG01 busca reducir pérdidas y BG02 acortar la primera respuesta. BG03 relaciona trazabilidad con revisiones de calidad; BG04 plantea adopción del producto. Estas cifras son metas del Impact Map, todavía no resultados comerciales demostrados.» Resaltar BG01 y BG02; no leer todas las cifras.

## 8 · Product Backlog

Transición: «Traducimos esos objetivos en capacidades priorizadas». Avanzar.

## 9 · Backlog funcional

«El producto completo contempla 53 historias y 172 puntos. Incluye configuración, monitoreo, atención, trazabilidad y capacidades posteriores. El primer incremento selecciona nueve historias y 42 puntos. Los puntos son estimación relativa, no horas ni porcentaje del producto terminado.»

## 10 · Nueve historias del Sprint 1

«Priorizamos historias que obligan a tomar decisiones arquitectónicas: estado y alertas para responder a tiempo; interrupción y recuperación para continuidad; detalle, asignación e incidencia para facilitar la atención. La implementación está respaldada por pruebas; la aceptación del equipo es una actividad distinta.»

Ejemplo funcional: «Como responsable de operaciones quiero reconocer y asignar una alerta para evitar que dos personas dupliquen la respuesta. El criterio exige conservar responsable, momento y estado». No presentar todas las historias como funcionalidades nuevas respecto al curso anterior.

## 11 · Escenarios no funcionales

«Aquí definimos cómo debe comportarse el sistema, no solo qué hace. QA-01 exige hacer visible una brecha tras el umbral y recuperar lecturas sin duplicados. QA-02 define carga y percentiles. QA-03 define éxito y tiempos de usuarios sin capacitación. Cada escenario permite diseñar una comprobación concreta.»

Precisar: los 30 segundos se cuentan después del umbral configurado; los cinco minutos, desde la reconexión. La carga completa de 1 000 sensores y el estudio con participantes siguen pendientes.

## 12 · Restricciones

«Las restricciones reducen nuestras alternativas: reutilizar Java/Spring, mantener MySQL, documentar REST y orientar el despliegue a Google Cloud. Se diferencian de un atributo de calidad: seleccionar Cloud Run no prueba rendimiento o disponibilidad.»

## 13 · Prototipos de pantalla

«Mostramos cómo la propuesta de interacción se concreta en el incremento. Las vistas evolucionan el diseño anterior; el valor está en la tarea que permiten completar y en su integración, no en fabricar pantallas adicionales.» Avanzar al recorrido.

## 14 · Monitoreo

«Sofía identifica el activo y revisa la lectura, el rango y la actualización. Si el sensor dejó de reportar, mostramos Sin datos aunque conserve una medición anterior. Esto evita interpretar una lectura histórica como condición actual segura.»

**Navegador:** abrir Monitoreo → elegir Cámaras frías → señalar Cámara de lácteos → revisar lectura y estado → filtrar por estado o ubicación si hace falta. El gráfico muestra lecturas observadas durante la sesión; no afirmar que presenta un histórico completo. Una fuente sin datos conserva su última medición.

## 15 · Contexto y asignación

«Desde Alertas abrimos el caso. En una vista encontramos el activo, la lectura, su rango, el momento y la situación de atención. Elegimos al responsable y reconocemos la alerta en una única operación.»

**Navegador:** Alertas → Abrir alerta de la desviación térmica → señalar lectura y rango → comprobar el responsable preseleccionado → presionar Reconocer y asignar. Usar una alerta abierta; si ya está asignada, mostrar su estado y apoyarse en la captura.

## 16 · Confirmación y deshacer

«La confirmación identifica el responsable y actualiza el estado. Durante diez segundos puede deshacerse una asignación accidental. El límite se valida en backend, no solo en el contador de la interfaz.»

**Navegador:** inmediatamente después de reconocer, presionar Deshacer antes de que el contador llegue a cero → comprobar que regresa a Abierta → reconocer de nuevo. No recargar mientras se demuestra el contador.

Opcional: escribir «Se trasladaron los productos a una cámara de respaldo y se solicitó revisión del equipo» → Guardar acción. No resolver un caso solo para producir una imagen si no se explicó el cierre.

## 17 · Trazabilidad

«El reporte reúne lecturas e incidencias del periodo y conserva quién atiende cada caso. Se solicita como trabajo asíncrono, lo que separa esta consulta del procesamiento de telemetría. La descarga actual es JSON; no prometer PDF o CSV para este flujo si no se muestra.»

**Navegador:** Reportes → Reporte de trazabilidad → título «Control de cámaras — turno tarde» → Desde: 22/10/2026 17:00 → Hasta: 22/10/2026 20:00 en hora de Bogotá/Lima → Generar reporte → esperar el resultado → señalar las incidencias y lecturas → Descargar reporte si el tiempo lo permite. Si el navegador usa otra zona horaria, elegir un intervalo que incluya la hora visible de la lectura. Reporte mensual es una sección distinta que conserva su ruta anterior.

## 18 · Drivers y tácticas

Transición: «Este recorrido explica por qué elegimos los siguientes drivers». Avanzar.

## 19 · Drivers arquitectónicos

«Priorizamos disponibilidad por continuidad de supervisión, rendimiento por oportunidad de respuesta y usabilidad por el contexto del usuario. Los demás atributos siguen siendo necesarios. OIDC y Stripe delegan responsabilidades específicas; la aplicación conserva autorización, aislamiento por organización y protección de sus APIs.»

## 20 · Iteraciones ADD

«La iteración cero establece la estructura. Las siguientes refinan continuidad, rendimiento y atención. Cada decisión se vincula a un escenario, compara alternativas y registra consecuencias. Las iteraciones de diseño no equivalen a sprints de implementación.»

## 21 · Estructura de microservicios

«Elegimos Strangler Fig para extraer capacidades gradualmente. Cada contexto tiene responsabilidad y datos propios; el Gateway permite convivir con el backend restante. Ocho microservicios es la arquitectura objetivo. Su costo es mayor coordinación, despliegue y consistencia eventual; no se justifica por sí sola por tener más repositorios.»

## 22 · Disponibilidad

«El heartbeat permite detectar una fuente silenciosa. El buffer local conserva lecturas durante un corte; el reenvío necesita idempotencia para no duplicarlas. La transacción mantiene consistencia de lo que se guarda. Una instancia mínima reduce arranques en frío, pero no constituye redundancia activa por sí sola.»

Ejemplo de fallo: «Si la respuesta de confirmación se pierde, Edge puede repetir el lote y Monitoring lo reconoce sin insertar las mismas lecturas otra vez». La recuperación local está comprobada; la validación cloud permanece pendiente.

## 23 · Rendimiento

«Evaluamos el rango con una copia local y mantenemos el estado actual para evitar consultar todo el historial. Los eventos desacoplan consumidores y Reports mantiene su modelo de lectura. Separar tópicos aísla flujos; para garantizar prioridad y tiempos hace falta dimensionar capacidad y medir. Outbox conserva lectura y evento en una transacción, con el costo de un relay adicional.»

No afirmar que las pruebas funcionales validaron los percentiles de 1 000 sensores.

## 24 · Usabilidad

«Reconocer y asignar juntos concentra una tarea; deshacer facilita corregir errores; presentar contexto y acciones por rol reduce búsqueda. El backend y las actualizaciones de estado sostienen ese flujo. Para afirmar 90 % de éxito en menos de un minuto todavía necesitamos participantes.»

## 25 · Arquitectura C4

Transición: «Ahora hacemos zoom desde el entorno del producto hasta la implementación de una operación». Avanzar.

## 26 · Contexto

«ColdTrace se relaciona con el encargado, operaciones/calidad, las fuentes IoT y proveedores externos. Este nivel delimita el sistema y su entorno; todavía no muestra los detalles internos de implementación.» Señalar actores y sistema central; no leer cada proveedor.

## 27 · Contenedores de la estructura inicial

«La aplicación web consume el Gateway. Los contextos separan monitoreo, alertas, reportes y las otras capacidades previstas. Cloud SQL representa infraestructura: la propiedad sigue siendo un esquema por servicio, sin consultas directas a las tablas de otro propietario.»

## 28 · Contenedores con Edge

«El agente de borde introduce persistencia local. Así podemos conservar lecturas cuando falla la conexión con la plataforma. En el alcance actual se utiliza un simulador; sensores físicos y despliegue real requieren validación adicional.»

## 29 · Contenedores con Pub/Sub

«La mensajería permite que alertas y reportes reaccionen a los datos sin bloquear la ingesta. La entrega repetida obliga a consumidores idempotentes. En local usamos el emulador; no lo presentamos como Pub/Sub ya desplegado en Google Cloud.»

## 30 · Componentes de Monitoring

«Separamos ingesta, evaluación, proyección y detección de brechas por responsabilidad. El modelo de componentes explica el diseño; la implementación agrupa algunas responsabilidades en clases concretas. No implica una clase por cada caja.»

## 31 · Ruta crítica de una lectura

«La ingesta evalúa y persiste la lectura, actualiza el estado y registra el evento en outbox. Después el relay publica. El compromiso es consistencia eventual: una consulta de otro servicio puede tardar un poco en reflejar el cambio.»

## 32 · Componentes de Alert

«El consumidor genera la incidencia a partir del evento; la consulta reúne su contexto; el comando reconoce y asigna, y la actualización informa al usuario. Se valida organización y permisos en servidor. Los canales externos se mantienen como integraciones previstas; la evidencia actual incluye notificación dentro de la aplicación.»

## 33 · C4 código

«Este zoom corresponde a código real. TelemetryService orquesta; depende del contrato TelemetryStore; JdbcTelemetryStore implementa persistencia. Reading representa una lectura y SafeRange evalúa sus límites. Esta separación permite probar reglas y cambiar detalles de infraestructura sin llevarlos al dominio.»

Señalar dependencias e implementación, no leer todos los métodos. Evitar afirmar que toda la aplicación ya tiene una arquitectura hexagonal completa.

## 34 · Respaldo en código

«Estos fragmentos vinculan diseño e implementación. Monitoring persiste y proyecta dentro de la transacción; Alert comprueba estado y responsable. Las pruebas complementarias verifican duplicados, recuperación y la ventana de deshacer. Sirven como evidencia de mecanismos, no sustituyen las pruebas de carga ni el estudio de uso.»

**Si piden repositorio:** abrir Veltis-Software/coldtrace-monitoring-service → `src/main/java/com/acme/coldtrace/platform/monitoring/application/TelemetryService.java` → método `ingest`; luego `src/test/resources/features/telemetry.feature`. Para Alert: `src/test/java/com/acme/coldtrace/alerts/AlertWorkflowTest.java` → `recognizesAssignsAndUndoesAtomicallyWithinTenSeconds`. Mostrar 20–30 segundos por archivo; no navegar todos los repositorios.

## 35 · Tecnología y cierre

«Angular mantiene la experiencia de usuario; Java/Spring implementa los servicios; MySQL conserva datos y Pub/Sub desacopla procesos. Docker y CI permiten reproducir el incremento. Distinguimos lo ejecutado localmente de la arquitectura cloud objetivo. El resultado de TP1 es un flujo funcional y verificable que sostiene las decisiones principales, con despliegue cloud y validación completa de calidad como pasos siguientes.»

## 36 · Apoyo de dominio — oculta

Abrir solo si preguntan por entidades funcionales. «Organización, activo, dispositivo, lectura e incidencia representan el dominio general. Esta vista complementa el zoom de código; no representa joins permitidos entre bases de datos de microservicios.»

## Ruta corta de demostración

1. Abrir la aplicación local y comprobar la sesión de Sofía Ramírez / Mercado San Fernando.
2. Monitoreo: Cámara de lácteos y Cámara de frutas y verduras: lecturas, rangos y estado En rango. Explicar que Sin datos se muestra cuando una fuente deja de reportar.
3. Alertas: abrir una desviación térmica, reconocer y asignar, deshacer antes de diez segundos y reconocer otra vez.
4. Reportes: generar trazabilidad para un intervalo que incluya las lecturas visibles.
5. Volver a la PPT para justificar disponibilidad, rendimiento y usabilidad.

Si el entorno deja de responder, usar las capturas incluidas en las diapositivas 14–17. No invertir la exposición en reiniciar servicios. No borrar datos, cambiar roles, contratar planes ni depender de IA o notificaciones externas durante esta demostración.

## Respuestas breves para preguntas previsibles

- **¿Por qué no hicieron pantallas completamente nuevas?** Porque evolucionamos un sistema existente. Reutilizar componentes coherentes evita duplicidad; el incremento añade contratos y comportamiento de arquitectura, no una interfaz paralela.
- **¿Qué es nuevo entonces?** Extracción gradual, ingesta y recuperación idempotentes, Outbox, proyecciones, eventos y el flujo atómico de asignación con deshacer; no todas las capacidades del producto nacieron en este sprint.
- **¿Cumplen los tres QA?** Están abordados por el diseño y existen pruebas de mecanismos. El cumplimiento completo de carga y usabilidad aún requiere sus escenarios y medidas.
- **¿Ya está todo en cloud?** No. Existe configuración objetivo y ejecución local/CI; hay que aprovisionar y validar el proyecto cloud.
- **¿La IA es su diferencial actual?** Es una evolución prevista con aprobación humana. La propuesta que hoy demostramos está en continuidad, atención y trazabilidad.
- **¿Por qué tantos repositorios?** Para responsabilidades y despliegues independientes de la arquitectura objetivo. La independencia se verifica por contratos y propiedad de datos, no por el número de repositorios.
