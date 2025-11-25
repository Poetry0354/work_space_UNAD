# Aplicación Climática de Terminal

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python para monitorear datos climáticos y agrícolas. Permite registrar información de estaciones meteorológicas, datos climáticos, análisis de suelo, fuentes de agua y comunidades de agricultores.

## Estructura del Proyecto

El proyecto está organizado en varios módulos de Python, cada uno representando una entidad del sistema:

- **`main.py`**: Es el punto de entrada principal de la aplicación. Contiene un menú interactivo que permite al usuario interactuar con el sistema para realizar operaciones como crear estaciones, registrar datos, etc.

- **`aplicacion_climatica.py`**: Es la clase central que orquesta toda la aplicación. Mantiene listas de todos los objetos creados (estaciones, datos climáticos, etc.) y proporciona métodos para gestionar y presentar la información.

- **`estacion_meteorologica.py`**: Define la clase `EstacionMeteorologica`, que representa una estación física con sus sensores. Cada estación tiene una ubicación, un ID y una capacidad para almacenar registros climáticos.

- **`dato_climatico.py`**: Representa un registro climático individual, con atributos como temperatura, precipitación, humedad y viento. Cada dato está asociado a una `EstacionMeteorologica`.

- **`recurso_natural.py`**: Es una clase base abstracta para los recursos naturales. Define atributos comunes como un ID y la calidad del recurso.

- **`suelo.py`**: Hereda de `RecursoNatural`. Modela una parcela de suelo con propiedades específicas como pH, nutrientes y clasificación.

- **`fuentes_agua.py`**: Hereda de `RecursoNatural`. Modela una fuente de agua (río, pozo, etc.) y su calidad.

- **`comunidad.py`**: Representa a una comunidad de agricultores, asociando a un agricultor con sus parcelas de `Suelo`.

- **`mainV1.py`**: Un script secundario, probablemente utilizado para pruebas iniciales o como una versión de demostración no interactiva.

- **`UMLdiagramaTarea2.png`**: Diagrama UML que probablemente ilustra las relaciones entre las clases del proyecto.

## ¿Cómo funciona?

El flujo de trabajo de la aplicación se gestiona a través del menú en `main.py`. La lógica es la siguiente:

1.  El usuario ejecuta `main.py`.
2.  Se presenta un menú con opciones para crear entidades o visualizar información.
3.  La clase `AplicacionClimatica` actúa como un contenedor central. Cuando el usuario crea una nueva estación, por ejemplo, se instancia un objeto `EstacionMeteorologica` y se añade a una lista dentro del objeto `AplicacionClimatica`.
4.  Los datos como `DatoClimatico`, `Suelo` y `FuentesAgua` se registran de manera similar y se almacenan en sus respectivas listas en `AplicacionClimatica`.
5.  Las clases `Suelo` y `FuentesAgua` son clases hijas de `RecursoNatural`, lo que demuestra el uso de herencia para modelar objetos que comparten características comunes.
6.  El usuario puede solicitar resúmenes o históricos, y la aplicación recupera los datos de las listas para presentarlos en la consola.

## ¿Cómo ejecutar la aplicación?

Para ejecutar la aplicación, simplemente corre el archivo `main.py` desde tu terminal. Asegúrate de tener Python instalado.

```bash
python main.py
```

Aparecerá un menú que te guiará a través de las diferentes funcionalidades.

## Posibles Modificaciones y Mejoras

Si deseas continuar desarrollando este proyecto, aquí tienes algunas ideas:

1.  **Persistencia de Datos**: Actualmente, todos los datos se pierden cuando la aplicación se cierra. Podrías implementar un sistema para guardar y cargar los datos en archivos (como JSON, CSV o una base de datos SQLite).
    -   **Sugerencia**: En `AplicacionClimatica`, podrías añadir métodos `guardar_datos()` y `cargar_datos()` que serialicen las listas de objetos a un archivo JSON.

2.  **Lógica de Predicción Real**: El método `predecir_clima()` en `aplicacion_climatica.py` es una simulación. Podrías implementar un algoritmo simple de predicción basado en el historial de datos climáticos (por ejemplo, calcular promedios o tendencias).

3.  **Mejorar la Interfaz de Usuario**: Podrías usar una librería como `rich` o `textual` para hacer la interfaz de línea de comandos más atractiva e interactiva.

4.  **Validación de Datos**: Añadir validaciones más robustas para las entradas del usuario en `main.py` para evitar errores (por ejemplo, asegurar que las fechas tengan el formato correcto o que los valores numéricos estén en un rango lógico).

5.  **Expandir las Decisiones**: El método `tomar_decision()` en la clase `Comunidad` es muy simple. Podría expandirse para dar recomendaciones más complejas, como qué tipo de cultivo es ideal para una parcela basándose en los datos del suelo y el clima histórico.

## Conceptos de Programación Aplicados

Este proyecto es un excelente caso de estudio para varios conceptos fundamentales de la Programación Orientada a Objetos (POO). A continuación se detallan los más importantes:

### 1. Programación Orientada a Objetos (POO)

-   **¿Qué es?**: Es un paradigma que basa la programación en "objetos", los cuales combinan datos (atributos) y comportamiento (métodos) en una sola unidad.
-   **¿Por qué se usó?**: El problema se modela de forma natural usando objetos. Entidades del mundo real como una "Estación Meteorológica", un "Dato Climático" o una "Comunidad" se convierten directamente en clases (`EstacionMeteorologica`, `DatoClimatico`, `Comunidad`). Esto hace que el código sea más intuitivo, organizado y fácil de entender.

### 2. Encapsulamiento

-   **¿Qué es?**: Es el principio de ocultar los detalles internos de un objeto y exponer solo lo necesario. En Python, se logra por convención usando un guion bajo (`_`) o dos (`__`) al inicio de los nombres de los atributos para indicar que son privados.
-   **¿Por qué se usó?**: En todas las clases, los atributos se definen como privados (ej. `self.__lista_estaciones` en `AplicacionClimatica`). El acceso a ellos se controla a través de métodos públicos (Getters y Setters). Esto protege los datos de modificaciones accidentales y permite añadir lógica de validación si fuera necesario (por ejemplo, asegurar que un valor de pH esté siempre entre 0 y 14).

### 3. Herencia

-   **¿Qué es?**: Es un mecanismo que permite a una clase (clase hija) heredar atributos y métodos de otra clase (clase padre).
-   **¿Por qué se usó?**: Las clases `Suelo` y `FuentesAgua` comparten características comunes, ya que ambas son un tipo de "recurso natural". Se creó una clase padre `RecursoNatural` con los atributos comunes (`id_recurso`, `calidad`). `Suelo` y `FuentesAgua` heredan de ella, reutilizando ese código y añadiendo sus propios atributos específicos. Esto evita la duplicación de código y establece una relación lógica ("es un") entre las clases.

### 4. Composición

-   **¿Qué es?**: Es una técnica donde una clase se "compone" de otras clases. Un objeto contiene a otro objeto.
-   **¿Por qué se usó?**: Este concepto se usa extensivamente. Por ejemplo, la clase `AplicacionClimatica` "tiene una" lista de `EstacionMeteorologica`. La clase `Comunidad` "tiene una" lista de `Suelo` (parcelas). Esto modela relaciones complejas donde un objeto está formado por otros, permitiendo construir estructuras de datos jerárquicas y lógicas.

### 5. Modularidad

-   **¿Qué es?**: Es la práctica de dividir un programa grande en módulos o archivos más pequeños y manejables.
-   **¿Por qué se usó?**: Cada clase del proyecto está en su propio archivo (`.py`). Esto mejora enormemente la organización. Si necesitas modificar la lógica de la estación meteorológica, sabes que solo tienes que ir a `estacion_meteorologica.py`. Facilita el mantenimiento, la reutilización de componentes y el trabajo en equipo.
