Trabajo Práctico Integrador — Gestión de Datos de Países (Python)

Cátedra: Programación 1 – TUP (UTN)
Integrantes: Maxi Franco — Octavio Fiore
Repositorio: TPI—Franco-Fiore

🧭 Descripción

Aplicación de consola que gestiona información de países a partir de un dataset CSV y permite realizar búsquedas, filtros, ordenamientos y estadísticas básicas. Está pensada para ejercitar listas, diccionarios, funciones, control de errores y modularización.


🎯 Objetivos de aprendizaje

Practicar estructuras de datos (listas y diccionarios) y modularización con funciones.

Aplicar filtrado y ordenamiento.

Calcular indicadores (máximos/mínimos, promedios, conteos por categoría). 

🗂 Estructura del proyecto

main.py — punto de entrada del programa (consola/menú). 
GitHub

utils/ — funciones auxiliares (lectura de CSV, validaciones, filtros/ordenamientos/estadísticas). 
GitHub

paises_mundo.csv — dataset base con columnas: nombre, poblacion, superficie, continente. 
GitHub

README.md — este documento.

⚙ Requisitos previos

Python 3.x instalado.

Entorno de consola (Windows, Linux o macOS).

🚀 Ejecución

Clonar o descargar el repositorio.

Abrir una consola en la carpeta del proyecto.

Ejecutar el programa (ej.: python main.py).

Seguir el menú interactivo en pantalla.

El programa asume que paises_mundo.csv está en la raíz del proyecto con el formato indicado. 
GitHub
+1

🧩 Funcionalidades (menú)

Búsqueda por nombre (coincidencia parcial o exacta).

Filtros por:

Continente

Rango de población

Rango de superficie

Ordenamientos por:

Nombre

Población

Superficie (asc/desc)

Estadísticas:

País con mayor y menor población

Promedio de población

Promedio de superficie

Cantidad de países por continente

Trabajo Práctico Integrador - P…

🧪 Uso esperado (flujo de usuario)

Cargar el CSV al iniciar.

Elegir una opción del menú (buscar/filtrar/ordenar/estadísticas).

Ingresar los parámetros solicitados (por ejemplo, un continente o un rango).

Ver los resultados en consola (listados o indicadores).

Repetir con otras opciones o salir.

🛡 Validaciones y manejo de errores

Lectura de CSV con control de formato (columnas y tipos).

Mensajes claros cuando no hay resultados o los parámetros del usuario son inválidos.

Evitar que el programa se caiga ante entradas vacías o mal formateadas. 



🏗 Conceptos aplicados

Listas y diccionarios para almacenar y consultar países.

Funciones (una responsabilidad por función) para lectura, filtrado, ordenamiento y estadísticas.

Condicionales y bucles para el flujo del menú.

Ordenamientos por claves específicas.

Estadísticas básicas (máximos, mínimos, promedios, conteos).

Archivos CSV: lectura e interpretación de registros. 



🧾 Dataset

Formato esperado (encabezado + registros):

nombre: texto (ej.: Argentina)

poblacion: entero (ej.: 45376763)

superficie: entero en km² (ej.: 2780400)

continente: texto (ej.: América) 

Trabajo Práctico Integrador - P…

📸 Evidencias sugeridas

Incluí en el repo (carpeta docs/ o raíz):

Capturas de pantalla mostrando:

Búsqueda por nombre

Filtros (continente / rangos)

Ordenamientos (asc/desc)

Todas las estadísticas requeridas

Breve informe/diagrama de flujo del sistema (puede ser imagen o PDF).

Video (10–15 min): explicación, demo funcionando y reflexión final del equipo. 

🧑‍🤝‍🧑 Participación de integrantes

Maxi Franco:

Octavio Fiore:

📚 Marco teórico (breve)

Resumen conceptual de: listas, diccionarios, funciones, condicionales, ordenamientos, estadísticas y manejo de CSV, con fuentes bibliográficas citadas en el informe adjunto. 

Trabajo Práctico Integrador - P…

📝 Licencia

Uso académico — libre para corrección y revisión.

Checklist de la consigna

 Menú con búsqueda / filtros / ordenamientos / estadísticas

 Validaciones de entrada y manejo de errores

 Código modular y comentado

 README claro (este documento)

 CSV incluido

 Marco teórico + diagrama/flujo

 Capturas de ejecución

 Video 10–15 min con explicación, demo y reflexión final

 Participación de integrantes documentada