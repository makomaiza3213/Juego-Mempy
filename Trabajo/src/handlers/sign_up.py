import json
import PySimpleGUI as sg


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
    if values['-USERN-'] != "" and (values['-AGE-'] != "" and values['-AGE-'] in range(2, 101)):
        if values["-GENDER-"] in gens:
            usuario = True
    else:
        if values["-GENDER-"] not in gens and values['-USERN-'] == "" and values['-AGE-'] == "":
            usuario = 1
        elif values['-USERN-'] == "" and values['-AGE-'] != "" and values["-GENDER-"] not in gens:
            usuario = 2
        elif values['-AGE-'] == "" and values['-USERN-'] != "" and values["-GENDER-"] not in gens:
            usuario = 3
        elif values["-GENDER-"] not in gens and values['-USERN-'] != "" and values['-AGE-'] != "":
            usuario = 4
        elif values['-AGE-'] != "" and int(values['-AGE-']) not in range(2, 101):
            usuario = 5
        elif values['-USERN-'] == "" and values['-AGE-'] == "":
            usuario = 6
        elif values['-USERN-'] == "" and values["-GENDER-"] not in gens:
            usuario = 7
        elif values["-GENDER-"] == "" and values['-USERN-'] != "" and values['-AGE-'] != "":
            usuario = 8
        elif values['-USERN-'] == "" and values['-AGE-'] != "" and values["-GENDER-"] in gens:
            usuario = 9

    return usuario


def message_incorrect_data(message_number):
    avisos = {
                    1: "Campos vácios, ingrese sus datos",
                    2: "Escriba un nombre de usuario",
                    3: "Escriba su edad",
                    4: "Elija un género valido",
                    5: "Edad inválida",
                    6: "Ingrese su edad y un nombre de usuario",
                    7: "Género inválido, escriba un nombre de usuario",
                    8: "Elija su género",
                    9: "Escriba un nombre de usuario"
            }
    sg.Popup(avisos[message_number])
