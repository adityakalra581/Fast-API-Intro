# Fast-API-Intro
Getting into the world of Fast API


### Creating the environment:

```python -m venv "name-of-the venv"```

### Activating the environment:

```"name-of-the-venv"\Scripts\activate```  **[for windows]**

```~/Projects/FastAPI$ "name-of-the-venv"\bin\activate```    **[for Ubuntu]**

- if there's an error of permission denied in case of Ubuntu use: 

```~/Projects/FastAPI$ . "name-of-the-venv"\bin\activate```    **[for Ubuntu]**


### Setting up the environment:

```pip install fastapi```

```pip install uvicorn (or hypercorn)```

```pip install tortoise-orm```

### running an app:

```uvicorn app:app --reload```

- here first **app** is the name of the file.

### FastAPI Swagger:

- http://127.0.0.1:8000/docs will open an interactive GUI for testing the API.

### FastAPI Redoc:

- http://127.0.0.1:8000/redoc another GUI for testing and explaining endpoints.

### Important references:

- 1. [FLask v/s Django v/s FastAPI](https://youtu.be/9YBAOYQOzWs)

- 2. [FastAPI DOCS](https://fastapi.tiangolo.com/)

- 3. [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/)


