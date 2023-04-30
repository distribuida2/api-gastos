#!/usr/bin/env python3

import requests


def post_expenditure(username, expenditure_dict):

    # armamos un diccionario con los campos del objeto JSON a transmitir en el request body
    data = {}
    data["username"] = username
    data["amount"] = expenditure_dict["amount"]
    data["category"] = expenditure_dict["category"]
    data["description"] = expenditure_dict["description"]

    # suponiendo que tenemos el servidor escuchando en el puerto 8000 del localhost
    response = requests.post("http://localhost:8000/expenditure", json=data)

    if response.status_code == 422:
        raise ValueError("Datos errónos para la API")

    if response.status_code != 201:
        raise ConnectionError("Error de conexión con la API")

    return response


def create_user(username):
    data = {}
    data["username"] = username

    # suponiendo que tenemos el servidor escuchando en el puerto 8000 del localhost
    response = requests.post("http://localhost:8000/user", json=data)

    if response.status_code == 201:
        print(f"Usuario {username} creado")
    else:
        print("Error")


create_user("Juan")
post_expenditure(
    "Juan", {"amount": 100, "category": "ocio", "description": "entrada al cine"}
)
