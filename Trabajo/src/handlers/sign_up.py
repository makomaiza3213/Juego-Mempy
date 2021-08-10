import json


def write_json(data, filename):
    """
        Escribe en el json especificado, los datos recibidos por parametro
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def add_user(values):
    """
    Agrega al archivo un nuevo usuario con los datos recibidos del registro y la configuración por defecto

    Args:
        values: Dict, valores de entrada ingresados

    Returns:
        Dict, los datos del jugador
    """
    with open("default_configuration.json") as json_file:
        config = json.load(json_file)
    with open("usuarios.json") as json_file:
        data = json.load(json_file)
        new = {"nombre": values['-USERN-'].upper(), "edad": values['-AGE-'], "genero": values['-GENDER-'],
               "configuracion": config}
        data['usuarios'].append(new)

    write_json(data, "usuarios.json")
    return new


def create_file_users(values):
    """
    Crea el archivo de usuarios,
    agrega un usuario con los datos recibidos del registro y la configuración por defecto,
    y actualiza el archivo

    Args:
        values: Dict, valores de entrada ingresados

    Returns:
        Dict, los datos del jugador
    """
    with open("default_configuration.json") as json_file:
        config = json.load(json_file)
    data = {'usuarios': []}
    new = {"nombre": values['-USERN-'].upper(), "edad": values['-AGE-'], "genero": values['-GENDER-'],
           "configuracion": config}
    data['usuarios'].append(new)
    with open("usuarios.json", "w") as file:
        json.dump(data, file, indent=4)

    return new


def ok(values):
    """
    Se verifica que no hayan campos vacios o datos que no correspondan

    Args:
        values: Dict, valores de entrada ingresados

    Returns:
        True, si los datos son válidos
        False, si son inválidos
    """
    usuario = False
    gens = ["masculino", "femenino", "otros"]
    if values['-USERN-'] != "" or values['-AGE-'] != "":
        if values["-GENDER-"] in gens:
            usuario = True
    return usuario
