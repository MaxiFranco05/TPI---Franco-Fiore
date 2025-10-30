# 🌍 Sistema de Gestión de Datos de Países

## 📚 Información Académica

**Materia:** Programación 1  
**Carrera:** Tecnicatura Universitaria en Programación (TUP)  
**Comisión:** 3  
**Integrantes:**
- Maximo Franco
- Octavio Fiore

**Repositorio:** [TPI-Franco-Fiore](https://github.com/MaxiFranco05/TPI---Franco-Fiore)

---

## 📖 Descripción del Proyecto

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar y analizar información de países a nivel mundial. El sistema lee datos desde un archivo CSV y proporciona funcionalidades para realizar búsquedas, aplicar filtros, ordenar datos y calcular estadísticas básicas.

El objetivo principal es aplicar y consolidar conocimientos fundamentales de programación, incluyendo:
- Estructuras de datos (listas y diccionarios)
- Modularización mediante funciones
- Lectura y procesamiento de archivos CSV
- Técnicas de filtrado y ordenamiento
- Cálculo de estadísticas básicas
- Validación de entradas y manejo de errores

El dataset incluye información de más de 200 países con datos sobre población, superficie territorial y continente de pertenencia.

---

## 🚀 Instrucciones de Uso

### Requisitos Previos
- Python 3.x instalado en el sistema
- Terminal o consola de comandos
- Los archivos del proyecto descargados o clonados

### Pasos para Ejecutar

1. **Clonar o descargar el repositorio:**
```bash
git clone https://github.com/MaxiFranco05/TPI---Franco-Fiore.git
cd TPI---Franco-Fiore
```

2. **Verificar que el archivo CSV esté presente:**
Asegúrese de que `paises_mundo.csv` esté en la raíz del proyecto.

3. **Ejecutar el programa:**
```bash
python main.py
```

4. **Navegar por el menú:**
Seleccione la opción deseada ingresando el número correspondiente y siga las instrucciones en pantalla.

---

## 💡 Ejemplos de Uso por Menú

### **Menú Principal**

```
-------------------------- Gestión de Datos de Países --------------------------
1. Buscar país
2. Filtrar países
3. Ordenar países
4. Mostrar estadísticas
5. Opciones de Desarrollador
6. Salir
--------------------------------------------------------------------------------
Ingrese una opcion:
```

---

### **1. Buscar País**

**Entrada:**
```
Ingrese una opcion: 1
Ingrese el nombre del país: argentina
```

**Salida:**
```
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
📍  Argentina
Población: 45,773,884 habitantes
Superficie: 2,780,400 km²
Continente: América del Sur
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
```

---

### **2. Filtrar Países**

#### **2.1 Filtrar por Continente**

**Entrada:**
```
Ingrese una opcion: 2
Selecciona la opción por la cual filtrar (Continente - Poblacion - Superficie): continente
Ingrese el continente (Asia - America Del Sur - America Del Norte - Africa - Europa): europa
```

**Salida:**
```
~~~~~~~~~~~~~~~~~~~~~~~~~~ Paises filtrados por Europa ~~~~~~~~~~~~~~~~~~~~~~~~~~
📍  Rusia
Poblacion: 144444359 habitantes
Superficie: 17098242 km²
📍  Alemania
Poblacion: 83294633 habitantes
Superficie: 357114 km²
📍  Reino Unido
Poblacion: 67736802 habitantes
Superficie: 242495 km²
📍  Francia
Poblacion: 64756584 habitantes
Superficie: 643801 km²
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

#### **2.2 Filtrar por Rango de Población**

**Entrada:**
```
Ingrese una opcion: 2
Selecciona la opción por la cual filtrar (Continente - Poblacion - Superficie): poblacion
Ingrese el valor minimo: 40000000
Ingrese el valor máximo: 50000000
```

**Salida:**
```
~~~~~~~~~~~~~~~~~~~~~~~~~~ Paises filtrados por Poblacion (entre 40,000,000 y 50,000,000) ~~~~~~~~~~~~~~~~~~~~~~~~~~
España - 47,519,628 habitantes
Argentina - 45,773,884 habitantes
Uganda - 48,582,334 habitantes
Argelia - 45,606,480 habitantes
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

### **3. Ordenar Países**

#### **3.1 Ordenar por Población (Descendente)**

**Entrada:**
```
Ingrese una opcion: 3
Selecciona la opción por la cual ordenar ('nombre','poblacion','superficie'): poblacion
Selecciona el orden por el cual ordenar (Asc - Desc): desc
```

**Salida:**
```
~~~~~~~~~~~~~~~~~~~~~~~~~~ Paises ordenados por Poblacion (en orden Desc) ~~~~~~~~~~~~~~~~~~~~~~~~~~
📍  País: India
Población: 1,428,627,663
Superficie: 3,287,263
Continente: Asia
📍  País: China
Población: 1,425,671,352
Superficie: 9,596,961
Continente: Asia
📍  País: Estados Unidos
Población: 339,996,563
Superficie: 9,833,517
Continente: América del Norte
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

#### **3.2 Ordenar por Superficie (Ascendente)**

**Entrada:**
```
Ingrese una opcion: 3
Selecciona la opción por la cual ordenar ('nombre','poblacion','superficie'): superficie
Selecciona el orden por el cual ordenar (Asc - Desc): asc
```

**Salida:**
```
~~~~~~~~~~~~~~~~~~~~~~~~~~ Paises ordenados por Superficie (en orden Asc) ~~~~~~~~~~~~~~~~~~~~~~~~~~
📍  País: Ciudad del Vaticano
Población: 825
Superficie: 0
Continente: Europa
📍  País: Mónaco
Población: 36,469
Superficie: 2
Continente: Europa
📍  País: Nauru
Población: 12,780
Superficie: 21
Continente: Oceanía
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

### **4. Mostrar Estadísticas**

**Entrada:**
```
Ingrese una opcion: 4
```

**Salida:**
```
~~~~~~~~~~~~~~~~~~~~~~~~~~ Estadísticas ~~~~~~~~~~~~~~~~~~~~~~~~~~
🗺️   Promedio de superficie: 674,264.48 km²
👨  Promedio de población: 40,679,819.69 habitantes
👨  País con mayor población: India → 1,428,627,663 habitantes.
👨  País con menor población: Ciudad del Vaticano → 825 habitantes.
🌎  Cantidad de países por continente:
                                    • Asia: 48 paises
                                    • América del Norte: 26 paises
                                    • América del Sur: 12 paises
                                    • África: 52 paises
                                    • Europa: 42 paises
                                    • Oceanía: 16 paises
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

### **6. Salir**

**Entrada:**
```
Ingrese una opcion: 6
```

**Salida:**
```
👋   Gracias por usar el sistema de paises. ¡Hasta pronto!
```

---

## 🛠️ Tecnologías y Funcionalidades

### **Tecnologías Utilizadas**
- **Lenguaje:** Python 3.x
- **Módulos estándar:** `csv` (lectura de archivos)
- **Control de versiones:** Git y GitHub

### **Estructuras de Datos**
- **Listas:** Para almacenar colecciones de países
- **Diccionarios:** Para representar cada país con sus atributos (nombre, población, superficie, continente)

### **Funcionalidades Implementadas**

#### **1. Búsqueda de Países**
- Búsqueda por coincidencia exacta del nombre
- Normalización de texto (eliminación de tildes y conversión a minúsculas)
- Validación de entradas

#### **2. Filtrado de Datos**
- **Por continente:** Asia, América del Norte, América del Sur, África, Europa, Oceanía
- **Por rango de población:** Filtrado entre dos valores numéricos
- **Por rango de superficie:** Filtrado entre dos valores numéricos

#### **3. Ordenamiento de Datos**
- **Por nombre:** Orden alfabético
- **Por población:** Orden ascendente o descendente
- **Por superficie:** Orden ascendente o descendente

#### **4. Estadísticas**
- País con mayor población
- País con menor población
- Promedio de población mundial
- Promedio de superficie territorial
- Cantidad de países por continente

#### **5. Validaciones y Manejo de Errores**
- Control de formato en archivo CSV
- Validación de tipos de datos (enteros para población y superficie)
- Mensajes claros de error cuando no hay resultados
- Manejo de excepciones para entradas inválidas
- Prevención de caídas del programa ante datos incorrectos

### **Estructura Modular**

```
TPI-Franco-Fiore/
│
├── main.py                  # Punto de entrada del programa
├── README.md                # Documentación del proyecto
├── data/
│   └── paises_mundo.csv     # Dataset con información de países
│
└── utils/                   # Módulo de utilidades
    ├── __init__.py
    ├── csv_options.py       # Lectura/creación CSV y CRUD (agregar/editar/eliminar)
    ├── filter.py            # Filtrado de datos
    ├── menu.py              # Gestión del menú principal
    ├── paginator.py         # Paginación en consola
    ├── searcher.py          # Búsqueda de países
    ├── sorter.py            # Ordenamiento de datos
    └── statistics.py        # Cálculo de estadísticas

```

### **Principios de Diseño**
- **Modularización:** Cada función tiene una responsabilidad única
- **Reutilización:** Funciones auxiliares compartidas entre módulos
- **Legibilidad:** Código comentado y con nombres descriptivos
- **Robustez:** Validaciones exhaustivas y manejo de errores

---

## 📝 Conclusión

Este proyecto ha permitido consolidar conocimientos fundamentales de programación estructurada en Python, demostrando la capacidad de:

1. **Gestionar datos complejos:** Mediante el uso eficiente de listas y diccionarios, logramos representar y manipular información de más de 200 países de forma organizada.

2. **Modularizar código:** La separación del proyecto en módulos independientes (`utils/`) facilitó el desarrollo colaborativo, el mantenimiento del código y su escalabilidad.

3. **Implementar algoritmos de búsqueda y ordenamiento:** Aplicamos técnicas de filtrado por múltiples criterios y ordenamiento mediante funciones lambda, permitiendo análisis flexible de los datos.

4. **Procesar archivos CSV:** Desarrollamos habilidades para leer, validar y transformar datos desde archivos externos, una competencia esencial en análisis de datos.

5. **Calcular estadísticas descriptivas:** Implementamos cálculos de máximos, mínimos, promedios y conteos agrupados, fundamentales para el análisis exploratorio de datos.

6. **Validar y manejar errores:** Incorporamos validaciones robustas que mejoran la experiencia del usuario y evitan fallos en la ejecución del programa.

### **Aprendizajes Clave**

- La importancia de la **planificación previa** mediante diagramas de flujo y diseño de funciones antes de comenzar a codificar.
- El valor de la **documentación clara** tanto en el código como en el README para facilitar la comprensión y uso del sistema.
- La necesidad de **testear exhaustivamente** cada funcionalidad con diferentes casos de prueba, incluyendo casos límite.
- El trabajo en equipo requiere **comunicación constante** y **división clara de responsabilidades**.

---

**Desarrollado con 💻 por Maximo Franco y Octavio Fiore | TUP - UTN | 2025**