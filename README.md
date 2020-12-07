# Fast-API-Intro
Getting into the world of Fast API

### Creating the environment:

```python -m venv "name-of-the venv"```

### Activating the environment:

```"name-of-the-venv"\Scripts\activate```

### Setting up the environment:

```pip install fastapi```

```pip install uvicorn (or hypercorn)```

### running an app:

```uvicorn app:app --reload```

- here first **app** is the name of the file.

### FastAPI Swagger:

- http://127.0.0.1:8000/docs will open an interactive GUI for testing the API.

### FastAPI Redoc:

- http://127.0.0.1:8000/redoc another GUI for testing and explaining endpoints.
