# API Gastos

## Introducción

Es una API REST muy simple, realizada con FastAPI, con fines académicos.

## ¿Cómo ejecutar el servidor?

1. Crear un virtual environment
2. Dentro de ese venv, ejecutar `pip install -r requirements.txt`
3. Y correr el servidor con `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

## Trabajo pendiente

1. Integrarlo con Github Actions


## Tests

Los ejecutamos con [pytest](https://docs.pytest.org). O sea, directamente vamos a la línea de comando y usando el virtual environment correcto ejecutamos `pytest`.

Algo para tener en cuenta al momento de ver cómo están organizados es el uso de [fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)

## ¿Cómo podemos hacer un request desde otro sistema?

Más allá de varias configuraciones y mejoras que se pueden hacer, en el snippet de abajo se ve un ejemplo de integración de cómo crear un gasto desde otro sistema Python mediante la librería [requests](https://requests.readthedocs.io/en/latest/)

```python
import requests


def post_expenditure(username, expenditure_dict):

    # armamos un diccionario con los campos del objeto JSON a transmitir en el request body
    data = {}
    data["username"] = username
    data["amount"] = expenditure_dict["amount"]
    data["category"] = expenditure_dict["category"]
    data["description"] = expenditure_dict["description"]
    data["username"] = username

    # suponiendo que tenemos el servidor escuchando en el puerto 8000 del localhost
    response = requests.post("http://localhost:8000/expenditure", json=data)

    if response.status_code == 422:
        raise ValueError("Datos errónos para la API")

    if response.status_code != 200:
        raise ConnectionError("Error de conexión con la API")

    return response
```
