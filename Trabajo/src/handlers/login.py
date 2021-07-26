import json


def buscar(nom):
    """
        lee y busca en el archivo el nombre que recibe por parametro y retorna dicho usuario si lo encontro , sino retorna False
    """
    existe = False
    with open("usuarios.json") as file:
        data = json.load(file)
    for usuario in data['usuarios']:
        if usuario["nombre"] == nom.upper():
            existe = usuario
    return existe
