# Proyecto Tus Datos

El proyecto tiene como objetivo realizar web scraping en la página de procesos judiciales para obtener información relevante sobre actores y demandados. Este proyecto está desarrollado en Python utilizando FastAPI y Selenium.

## Paso 1: Configuración del entorno

Antes de comenzar, asegúrate de instalar todas las dependencias necesarias ejecutando el siguiente comando:

- pip install -r requirements.txt

## Paso 2: Obtención de datos

Una vez instaladas las dependencias, puedes iniciar el programa utilizando Uvicorn:

- uvicorn main:app --reload

Una vez que el servidor esté en funcionamiento, puedes acceder a la documentación de FastAPI para explorar los endpoints expuestos, que incluyen:

# Actor/Ofendido

- Obtener Actor/Ofendido: http://127.0.0.1:8000/actors/actors
Este endpoint devuelve una lista de Actor/Ofendido obtenidos mediante web scraping.
- Actores en la Base de Datos: http://127.0.0.1:8000/actors/actors-in-database

# Demandados
- Obtener Demandados: http://127.0.0.1:8000/defendants/defendants

Este endpoint devuelve una lista de demandados obtenidos mediante web scraping.

- Demandados en la Base de Datos: http://127.0.0.1:8000/defendants/defendants-in-database

Este endpoint devuelve una lista de demandados almacenados en la base de datos.






