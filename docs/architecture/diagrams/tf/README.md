# Diagramas del Trabajo Final

- `class/`: diagramas de clases del dominio de cada microservicio, obtenidos del código de la rama `main` (versión 1.0.0).
- `database/`: diagramas de base de datos de cada esquema, reconstruidos desde las migraciones Flyway de cada repositorio.
- `cloud/`: arquitectura de despliegue de ColdTrace en Google Cloud (`veltis-coldtrace-dev`, `us-east1`).

Regeneración (requiere Graphviz y los repositorios clonados en un mismo directorio):

```
python tools/class_diagrams.py <directorio-de-repositorios> class
python tools/database_diagrams.py <directorio-de-repositorios> database
```
