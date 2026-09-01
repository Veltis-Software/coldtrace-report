<h2 style="text-align: center;"> Universidad Peruana de Ciencias Aplicadas </h2>

<div style="text-align: center;">
  <img src="https://marketingperu.beglobal.biz/wp-content/uploads/2025/01/logo-upc-png-transparente-1.png" alt="UPC Logo" style="width: 250px; height: auto;">
</div>

<h4 style="text-align: center"> Ingeniería de Software </h4>

<h4 style="text-align: center"> Periodo: 202620 </h4>

<h4 style="text-align: center"> 1ASI0657 | Fundamentos de Arquitectura de Software</h4>

<h4 style="text-align: center"> NRC: 9199  </h4>

<h4 style="text-align: center"> Docente: Daniel Enrique Mori Yzaguirre </h4>

<h3 style="text-align: center;"> Informe del Trabajo Final </h3>

<h4 style="text-align: center"> Startup: ICEQ </h4>

<h4 style="text-align: center"> Producto: Cold Trace </h4>

<h4 style="text-align: center">Integrantes:</h4>

<div style="text-align:center; margin-top: 10px; font-size: 90%; line-height: 1.6;">
  <p> — Condori Lozano, Alessandro Ramiro </p>
  <p>U202121579 — Julca Cruz, Renso Anthony</p>
  <p> — Morales Venegas, David Joel</p>
</div>

<br>

<h5 style="text-align: center; font-style: italic;"> Setiembre 2026 </h5>

<hr class="page-break">

# Registro de Versiones del Informe

| Versión | Fecha     | Autor               | Descripción de modificación                              |
|---------|-----------|---------------------|----------------------------------------------------------|
| 1.0     | 1/09/2026 |  Julca Cruz, Renso Anthony        | Creación inicial de la estructura del informe            |

# Contenido

- [Capítulo I: Introducción](#capítulo-i-introducción)
    - [1.1. Startup Profile](#11-startup-profile)
        - [1.1.1. Descripción de la Startup](#111-descripción-de-la-startup)
        - [1.1.2. Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
    - [1.2. Solution Profile](#12-solution-profile)
        - [1.2.1. Nombre del producto](#121-nombre-del-producto)
        - [1.2.2. Antecedentes y problemática](#122-antecedentes-y-problemática)
        - [1.2.3. Lean UX Process](#123-lean-ux-process)
            - [1.2.3.1. Lean UX Problem Statement](#1231-lean-ux-problem-statement)
            - [1.2.3.2. Lean UX Assumptions](#1232-lean-ux-assumptions)
            - [1.2.3.3. Lean UX Hypothesis](#1233-lean-ux-hypothesis)
            - [1.2.3.4. Lean UX Canvas](#1234-lean-ux-canvas)
    - [1.3. Segmentos objetivo](#13-segmentos-objetivo)
- [Capítulo II: Requirements & Analysis](#capítulo-ii-requirements--analysis)
    - [2.1. Competidores](#21-competidores)
    - [2.2. Entrevistas](#22-entrevistas)
    - [2.3. Needfinding](#23-needfinding)
        - [2.3.1. User Personas](#231-user-personas)
        - [2.3.2. User Task Matrix](#232-user-task-matrix)
        - [2.3.3. Empathy Maps](#233-empathy-maps)
        - [2.3.4. As-is Scenario Mapping](#234-as-is-scenario-mapping)
- [Capítulo III: Requirements Specification](#capítulo-iii-requirements-specification)
    - [3.1. To-Be Scenario Mapping](#31-to-be-scenario-mapping)
    - [3.2. User Stories](#32-user-stories)
    - [3.3. Impact Map](#33-impact-map)
    - [3.4. Product Backlog](#34-product-backlog)

# Student Outcome

En el siguiente cuadro se describe las acciones realizadas y enunciadas de conclusiones por parte del equipo, que permiten sustentar el haber alcanzado el logro ABET - EAC - Student Outcome.

<table border="1" style="border-collapse: collapse; width: 100%; font-family: sans-serif; font-size: 14px;">
    <thead>
        <tr style="background-color: #f2f2f2; text-align: left;">
            <th style="padding: 10px; width: 25%;">Criterio específico</th>
            <th style="padding: 10px; width: 50%;">Acciones realizadas</th>
            <th style="padding: 10px; width: 25%;">Conclusiones</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 10px;"><strong> Actualiza conceptos y conocimientos necesarios para su desarrollo profesional y en especial para su proyecto en soluciones de software. </strong></td>
            <td style="padding: 10px;">
                <p><strong>Julca Cruz, Renso Anthony</strong><br> 
                <strong>TB1:</strong><br>
            </td>
            <td style="padding: 10px; vertical-align: top;"> 
                <strong>TB1:</strong><br>
                <br><br>
            </td>
        </tr>
        <tr>
            <td style="padding: 10px;"><strong> Reconoce la necesidad del aprendizaje permanente para el desempeño profesional y el desarrollo de proyectos en soluciones de software. </strong></td>
            <td style="padding: 10px;">
                <p><strong>Julca Cruz, Renso Anthony</strong><br> 
                <strong>TB1:</strong><br>
                <br>
            </td>
            <td style="padding: 10px; vertical-align: top;"> 
                <strong>TB1:</strong><br>
                <br><br>
            </td>
        </tr>
    </tbody>
</table>

<hr class="page-break">

# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup

ICEQ (Ice Quality Monitoring) es una startup tecnológica enfocada en mejorar el control de la cadena de frío dentro del sector alimentario mediante una propuesta SaaS accesible y escalable. Su producto principal es ColdTrace, una plataforma web de monitoreo inteligente que centraliza la supervisión de temperatura y humedad en cámaras frigoríficas, almacenes y unidades de transporte refrigerado.

La solución integra sensores IoT con una aplicación web accesible desde navegador, lo que permite a supermercados, restaurantes, operadores logísticos y centros de distribución visualizar el estado de sus activos en tiempo real, recibir alertas ante desviaciones críticas, consultar reportes históricos y recibir asistencia inteligente para resolver incidencias bajo aprobación humana. A diferencia de esquemas manuales o aislados, ColdTrace se plantea como una solución digital escalable, apoyada en tecnologías open source, con planes de suscripción por nivel de operación para reducir pérdidas, elevar la capacidad de respuesta operativa y reforzar el cumplimiento sanitario.

Misión: Brindar a las empresas del sector alimentario una plataforma confiable, accesible y escalable para vigilar la cadena de frío en tiempo real, anticiparse a fallas de refrigeración, tomar decisiones mejor informadas basadas en datos y adoptar progresivamente funcionalidades avanzadas según su plan.

Visión: Consolidarnos como una referencia regional en monitoreo digital de cadena de frío, impulsando operaciones alimentarias más seguras, eficientes y sostenibles mediante soluciones web modernas, abiertas a integración, con asistencia inteligente supervisada y un modelo SaaS viable para negocios de distintos tamaños.

### 1.1.2. Perfiles de integrantes del equipo