# Guion de exposición de ColdTrace

El texto de cada diapositiva está preparado para decirse en voz alta. Las indicaciones en «Acción en pantalla» son para quien expone y no se leen. Duración orientativa: 18–22 minutos, incluida la demostración. La diapositiva 36 está oculta y sirve de apoyo para preguntas.

## 1 · Veltis Software y ColdTrace

Buenas tardes. Somos Veltis Software y hoy les presentamos ColdTrace, una plataforma para supervisar la cadena de frío y coordinar la atención cuando ocurre una desviación.

Vamos a explicar el problema que buscamos resolver, cómo lo convertimos en requisitos y cómo esos requisitos orientaron nuestras decisiones de arquitectura. También mostraremos el primer incremento funcionando.

## 2 · Contenido

Para seguir una misma idea durante la presentación, empezaremos por las necesidades del negocio. Después veremos qué priorizamos y cómo lo utiliza una persona en la aplicación. Con ese contexto, explicaremos las decisiones de arquitectura y llegaremos hasta el código que las respalda.

## 3 · Presentación del proyecto

Empecemos entonces por el problema: ¿qué necesita un negocio que conserva productos refrigerados y qué ocurre cuando pierde visibilidad sobre sus condiciones?

## 4 · El problema

Pensemos en una cámara que almacena productos perecibles. Si la temperatura sale de su rango y la revisión se hace más tarde, el encargado podría enterarse cuando los productos ya estuvieron expuestos demasiado tiempo.

Pero detectar la desviación es solo una parte del problema. También hace falta saber quién la atiende, qué se hizo y dónde queda registrado lo ocurrido.

Representamos estas necesidades con dos perfiles: Gustavo, que necesita una supervisión sencilla para su operación, y Sofía, que revisa distintas ubicaciones y da seguimiento a las incidencias.

## 5 · Propuesta de valor

A partir de ese problema, nuestra propuesta conecta la supervisión con la respuesta. El usuario puede revisar una lectura y su rango, identificar una alerta, asignar a alguien y conservar el seguimiento del caso.

Además, distinguimos una cámara dentro del rango de un sensor que dejó de enviar información. Una lectura antigua no debería dar una falsa sensación de seguridad.

El valor que buscamos para los negocios alimentarios está en reunir ese recorrido y facilitar su adopción gradual. Con pilotos tendremos que validar cuánto les ayuda a reducir trabajo manual y responder a tiempo.

## 6 · Evolución de la solución existente

Para construirlo partimos de una aplicación que ya existía. Conservamos las capacidades y los componentes visuales que seguían siendo útiles, y evolucionamos la forma en que se organizan y comunican sus partes.

En este incremento separamos monitoreo, alertas y reportes en servicios e incorporamos un punto de entrada común. La gestión de identidad y de activos todavía permanece en el backend mientras avanza la migración.

Por eso, el avance también se aprecia detrás de las pantallas: en cómo conservamos las lecturas, evitamos duplicarlas y coordinamos la atención de una alerta.

## 7 · Objetivos de negocio

Con esa propuesta definimos nuestros objetivos de negocio. Los principales son reducir las pérdidas asociadas a desviaciones y acortar el tiempo hasta que alguien empieza a atenderlas.

También buscamos facilitar las revisiones de calidad mediante registros trazables y favorecer la adopción del producto. Las cifras que aparecen aquí son metas que orientan el proyecto; todavía no son resultados comerciales medidos.

## 8 · Product Backlog

Ahora bien, para avanzar hacia esos objetivos necesitamos convertirlos en trabajo concreto. Eso es lo que organizamos en el backlog del producto.

## 9 · Backlog funcional

El alcance completo contempla cincuenta y tres historias, estimadas en ciento setenta y dos puntos. Ahí distribuimos las capacidades de configuración, monitoreo, atención y trazabilidad, junto con funciones previstas para etapas posteriores.

Para este primer sprint seleccionamos nueve historias, que suman cuarenta y dos puntos. La selección permite mostrar un recorrido funcional y abordar las decisiones de arquitectura más importantes. Los puntos expresan una estimación relativa del esfuerzo; no equivalen directamente a horas.

## 10 · Nueve historias del Sprint 1

Dentro de esa selección priorizamos lo necesario para seguir una lectura y actuar sobre ella: consultar el estado del activo, detectar una desviación, revisar su contexto y coordinar la atención.

Incluimos también la interrupción y recuperación de datos, porque el monitoreo debe considerar qué pasa cuando se pierde la conexión.

Por ejemplo, al reconocer y asignar una alerta buscamos que el equipo sepa quién la atiende. Para comprobar esa historia debemos conservar el responsable, el momento y el nuevo estado. Así, cada historia se traduce en un comportamiento verificable.

## 11 · Escenarios no funcionales

Hasta aquí hemos explicado qué debe hacer la plataforma. Ahora precisamos cómo debe comportarse en situaciones importantes.

Primero, si una fuente deja de reportar, debemos hacer visible esa interrupción y recuperar sus lecturas sin duplicarlas. Segundo, debemos procesar las lecturas y comunicar las desviaciones dentro de los tiempos definidos, incluso con la carga prevista. Y tercero, una persona debe poder completar las tareas principales con rapidez y sin capacitación previa.

Esto nos permite evaluar decisiones con algo más concreto que decir que el sistema debe ser rápido o fácil de usar. Ya tenemos pruebas de varios mecanismos; la evaluación completa con mil sensores y las sesiones con participantes siguen pendientes.

> Apoyo si preguntan por los tiempos: los treinta segundos para hacer visible la brecha se cuentan después del umbral configurado. Los cinco minutos de recuperación se cuentan desde la reconexión.

## 12 · Restricciones

Además de esos requisitos, tenemos restricciones que delimitan las alternativas: reutilizar Java con Spring, mantener MySQL, documentar las interfaces y orientar el despliegue hacia Google Cloud.

Estas decisiones fijan parte del entorno de trabajo. Después debemos comprobar que la solución construida sobre ese entorno cumple los tiempos y el comportamiento que acabamos de describir.

## 13 · Prototipos de pantalla

Con los requisitos claros, veamos cómo se traduce el flujo a la experiencia del usuario. Evolucionamos las vistas existentes y las conectamos con los servicios extraídos. Vamos a seguir un caso desde el monitoreo hasta su reporte.

## 14 · Monitoreo

En esta primera vista, Sofía puede revisar las dos cámaras del negocio. Ve la temperatura, la humedad, la ubicación y cuándo llegó la última lectura. En este momento ambas están dentro del rango, por eso aparecen en verde.

La gráfica muestra las lecturas recibidas durante la sesión. Si un sensor deja de reportar, la aplicación debe indicar que no tiene datos actuales, aunque conserve la última medición. Así evitamos confundir una lectura anterior con el estado presente de la cámara.

> Acción en pantalla: abrir Monitoreo, elegir Cámaras frías y señalar las cámaras de lácteos y de frutas y verduras. Mostrar lectura, hora y estado verde. Usar los filtros solo si hay tiempo.

## 15 · Contexto y asignación

Ahora pasemos a una desviación registrada anteriormente. Aunque la cámara ya tenga nuevas lecturas dentro del rango, este caso permite revisar lo ocurrido y darle seguimiento.

En el detalle encontramos la lectura que originó la alerta, su rango permitido, el momento y el estado de atención. Con esa información, Sofía puede elegir al responsable y reconocer la alerta en una sola operación.

> Acción en pantalla: entrar a Alertas y abrir la desviación térmica. Señalar los doce grados frente al rango de dos a ocho grados. Revisar el responsable seleccionado y pulsar Reconocer y asignar. Si ya está asignada, usar la captura de la PPT.

## 16 · Confirmación y deshacer

Al confirmar, la aplicación muestra quién quedó a cargo y actualiza el estado. También ofrece diez segundos para deshacer la operación si la asignación fue accidental.

Vamos a usar esa opción para comprobar que el caso vuelve a quedar abierto. El límite también se valida en el servidor, de modo que la regla no depende únicamente del contador que vemos en pantalla.

> Acción en pantalla: pulsar Deshacer antes de que termine el contador. Comprobar que vuelve a Abierta y reconocer de nuevo. No recargar durante la demostración del contador.

## 17 · Trazabilidad

Después de revisar y atender las alertas, necesitamos consultar lo ocurrido durante un periodo. Este reporte reúne las lecturas y las incidencias y permite revisar el responsable registrado en cada caso.

La generación se procesa como una tarea separada. Así, preparar el reporte no forma parte del recorrido que recibe cada lectura. Al terminar, podemos consultar el resultado y descargarlo. En este incremento la descarga está disponible en formato JSON.

> Acción en pantalla: abrir Reportes y Reporte de trazabilidad. Escribir «Control de cámaras — turno tarde». Elegir el 22 de octubre de 2026, desde las 17:00 hasta las 20:00, en hora de Bogotá o Lima. Pulsar Generar reporte y señalar los activos, las lecturas y las incidencias. Ajustar el periodo si se demuestra otro día.

## 18 · Drivers y tácticas

Lo que acabamos de mostrar nos lleva a la siguiente parte: qué decisiones necesitamos para sostener este recorrido cuando hay cortes de conexión, mayor carga o errores de uso.

## 19 · Drivers arquitectónicos

Priorizamos tres necesidades que influyen especialmente en el diseño: mantener la supervisión ante problemas de conexión, responder a tiempo y facilitar la atención de las alertas.

Estas necesidades corresponden a disponibilidad, rendimiento y usabilidad. Las tomamos como guía porque afectan directamente al problema del negocio. La seguridad también sigue siendo necesaria: cada operación debe respetar los permisos y la organización del usuario.

## 20 · Iteraciones ADD

Para trabajar esas prioridades usamos el diseño guiado por atributos. Empezamos estableciendo la estructura general y después profundizamos en continuidad, procesamiento de lecturas y atención de incidencias.

En cada paso relacionamos una necesidad con una decisión, consideramos alternativas y revisamos las consecuencias. Este proceso organiza el diseño; sus iteraciones no representan necesariamente los sprints de implementación.

## 21 · Estructura de microservicios

La primera decisión fue hacer la separación gradualmente. Extraemos capacidades y dejamos que convivan con el backend existente a través del punto de entrada común.

Cada servicio debe tener una responsabilidad clara y ser dueño de sus datos. La arquitectura objetivo contempla ocho microservicios, pero este primer incremento se concentra en las capacidades seleccionadas.

La separación también tiene un costo: hay más despliegues que coordinar y algunos cambios tardan un poco en reflejarse entre servicios. Por eso la justificamos por las responsabilidades y necesidades del sistema.

## 22 · Disponibilidad

Con respecto a la continuidad, combinamos varios mecanismos. Una señal periódica permite saber si la fuente sigue comunicándose. Si se corta la conexión, el agente cercano a los sensores conserva las lecturas y las reenvía al recuperarla.

Aquí es importante evitar duplicados. Por ejemplo, el servidor podría guardar un lote y perderse la respuesta de confirmación. Si el agente vuelve a enviarlo, la plataforma debe reconocerlo y evitar registrar otra vez las mismas lecturas.

Hemos comprobado este comportamiento en el entorno local. La validación del despliegue en la nube todavía es un paso posterior.

## 23 · Rendimiento

Una vez considerada la continuidad, buscamos que cada lectura se procese sin consultas innecesarias. Para evaluar su rango usamos una copia local de la configuración y mantenemos una vista del estado actual, en lugar de recorrer todo el historial cada vez.

Después comunicamos los cambios mediante eventos para que alertas y reportes puedan procesarlos por separado. Guardamos el evento pendiente junto con la lectura en una misma transacción. Así queda registrado que todavía debe publicarse, aunque ocurra un fallo después de guardar los datos.

Estas decisiones respaldan el diseño. Para demostrar los tiempos con toda la carga prevista aún debemos ejecutar la prueba correspondiente.

## 24 · Usabilidad

En cuanto a la facilidad de uso, las decisiones se ven en el recorrido mostrado: el contexto de la alerta está reunido, reconocer y asignar forman una sola tarea y deshacer permite corregir un error rápidamente.

La interfaz se apoya en reglas del servidor para mantener coherentes el responsable y el estado. Buscamos reducir búsquedas y pasos innecesarios. Para confirmar que las personas completan la tarea en los tiempos planteados, necesitamos realizar la evaluación con participantes.

## 25 · Arquitectura C4

Ya explicamos las decisiones principales. Ahora vamos a ubicarlas en la arquitectura, empezando por la relación del producto con su entorno y acercándonos hasta una operación implementada en código.

## 26 · Contexto

En esta primera vista encontramos a las personas que utilizan ColdTrace, las fuentes que envían las lecturas y los proveedores externos con los que se integra el producto.

Este nivel delimita qué responsabilidad tiene ColdTrace y con quién se comunica. En las siguientes vistas veremos cómo se organiza por dentro.

> Acción en pantalla: señalar el sistema central, los perfiles de usuario y las fuentes de datos. Mencionar solo las integraciones externas más relevantes.

## 27 · Contenedores de la estructura inicial

Al acercarnos un nivel, vemos la aplicación web, el punto de entrada y los servicios que separan las capacidades del producto.

También vemos el almacenamiento. Aunque la infraestructura pueda agruparse en una misma plataforma de base de datos, cada servicio conserva la propiedad de su esquema. Si necesita información de otro servicio, debe obtenerla mediante los contratos definidos, sin consultar directamente sus tablas.

## 28 · Contenedores con Edge

Sobre esa estructura incorporamos el agente de borde, que funciona cerca de los sensores. Su papel es conservar las lecturas localmente cuando no puede comunicarse con la plataforma y enviarlas al restablecer la conexión.

Esto concreta la decisión de continuidad que explicamos antes. En el incremento actual trabajamos con una fuente simulada; la integración con sensores físicos requiere su propia validación.

## 29 · Contenedores con Pub/Sub

La siguiente vista incorpora la mensajería. Una vez recibida una lectura, otros servicios pueden reaccionar a sus eventos sin que todo tenga que completarse dentro de la misma petición.

Como un mensaje puede llegar más de una vez, los consumidores también deben evitar procesarlo por duplicado. En local utilizamos el emulador; la integración desplegada en Google Cloud queda pendiente de validación.

## 30 · Componentes de Monitoring

Si ahora nos acercamos al servicio de monitoreo, encontramos las responsabilidades de recibir lecturas, evaluar sus rangos, actualizar el estado y detectar interrupciones.

Esta división permite entender qué hace cada parte y cómo colabora con las demás. Al llevarla a código, algunas responsabilidades pueden agruparse en una misma clase; el diagrama expresa la organización del diseño.

## 31 · Ruta crítica de una lectura

Sigamos entonces una lectura concreta. Primero se recibe y se evalúa. Después se guarda, se actualiza el estado del activo y se registra el evento pendiente de publicación dentro de la misma transacción.

Otro proceso publica ese evento para que los demás servicios lo consuman. Esto evita perder la intención de comunicar el cambio, aunque implica que una alerta o un reporte pueden tardar un breve momento en reflejarlo.

## 32 · Componentes de Alert

Cuando el evento llega al servicio de alertas, se genera la incidencia correspondiente. A partir de ahí podemos consultar su contexto y ejecutar las operaciones de atención, como reconocerla y asignar un responsable.

El servidor comprueba los permisos y la organización del usuario. En el incremento mostramos la notificación dentro de la aplicación; los otros canales forman parte de las integraciones previstas.

## 33 · C4 código

Para conectar estas vistas con la implementación, aquí mostramos las clases que participan en la ingesta. El servicio de aplicación coordina la operación y utiliza un contrato de almacenamiento. Una implementación concreta de ese contrato se encarga del acceso a la base de datos.

La lectura y el rango seguro representan los conceptos con los que evaluamos los límites. Esta separación permite probar las reglas y cambiar detalles de persistencia sin mezclar todas esas responsabilidades.

> Acción en pantalla: señalar TelemetryService, después el contrato TelemetryStore y su implementación JdbcTelemetryStore. Terminar con Reading y SafeRange. No es necesario leer todos los métodos.

## 34 · Respaldo en código

En estos fragmentos vemos cómo las decisiones anteriores llegan al código. En monitoreo, la lectura, su estado y el evento pendiente se guardan en una misma transacción. En alertas, la prueba comprueba que el reconocimiento actualiza el estado y el responsable, y que puede deshacerse dentro del tiempo permitido.

También hay pruebas para duplicados y recuperación. Esto respalda los mecanismos implementados; la prueba de carga y la evaluación con usuarios siguen siendo comprobaciones distintas.

> Solo si piden el repositorio: abrir coldtrace-monitoring-service en Veltis-Software y buscar TelemetryService.java, método ingest. Para atención, abrir AlertWorkflowTest.java en coldtrace-alert-service y mostrar la prueba de reconocimiento y deshacer. Mantener la revisión breve para conservar el hilo de la exposición.

## 35 · Tecnología y cierre

Para cerrar, las tecnologías responden a las responsabilidades que recorrimos: Angular mantiene la experiencia del usuario, Java con Spring implementa los servicios, MySQL conserva los datos y la mensajería permite comunicar cambios entre procesos. Docker y la integración continua nos ayudan a reproducir y verificar el incremento.

En este primer sprint presentamos un flujo que funciona desde la lectura hasta el seguimiento y el reporte, junto con pruebas que respaldan sus mecanismos principales. Los siguientes pasos son validar el despliegue en la nube y completar las mediciones de carga y de uso.

Con esto cerramos la presentación. Gracias; quedamos atentos a sus preguntas.

## 36 · Apoyo de dominio — oculta

Aquí podemos complementar la explicación con los conceptos del negocio. Una organización administra activos; los dispositivos generan lecturas y las desviaciones dan lugar a incidencias. Esta vista ayuda a entender las relaciones del dominio, mientras que la anterior se concentra en las clases de una operación concreta.

> Uso: mostrar únicamente si preguntan por las entidades o las relaciones funcionales.

## Ruta corta de demostración

1. Iniciar sesión con Sofía Ramírez, de Mercado San Fernando.
2. Abrir Monitoreo y señalar las dos cámaras, sus lecturas y el estado verde.
3. Entrar a Alertas y abrir la desviación térmica registrada anteriormente.
4. Reconocer y asignar; deshacer antes de diez segundos y reconocer de nuevo.
5. Abrir Reporte de trazabilidad y generar un periodo que incluya las lecturas.
6. Regresar a la presentación para explicar las decisiones que sostienen ese recorrido.

Si la aplicación deja de responder, continuar con las capturas de las diapositivas 14 a 17. Los nombres y registros son datos de ejemplo.

## Respuestas para preguntas previsibles

**¿Por qué reutilizaron pantallas?**

Porque partimos de una aplicación existente y tenía componentes útiles. Los adaptamos al comportamiento de los servicios extraídos y conservamos una experiencia coherente para el usuario.

**¿Qué aporta este incremento?**

La separación gradual de responsabilidades y el comportamiento que la sostiene: recuperación sin duplicados, comunicación por eventos y atención con responsable y opción de deshacer.

**¿Ya comprobaron todos los requisitos de calidad?**

Hemos probado varios mecanismos que los respaldan. Para confirmar los tiempos con toda la carga y la facilidad de uso debemos ejecutar los escenarios completos y trabajar con participantes.

**¿Ya está desplegado en Google Cloud?**

Actualmente mostramos ejecución local y configuración preparada para la arquitectura objetivo. El aprovisionamiento y la validación en Google Cloud están pendientes.

**¿Cuál es el diferencial si ya existen plataformas de monitoreo?**

Buscamos adaptar el recorrido de supervisión, atención y trazabilidad a los negocios alimentarios que estudiamos, con una adopción gradual. Ese ajuste y su utilidad deben validarse con pilotos.

**¿Por qué tienen varios repositorios?**

Porque la arquitectura plantea responsabilidades y despliegues separados. Lo importante es sostener esa separación con contratos y propiedad de datos; tener más repositorios por sí solo no demuestra que la arquitectura esté bien resuelta.
