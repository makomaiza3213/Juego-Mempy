import json


def write_json(data, filename):
    """
        Escribe en el json especificado, los datos recibidos por parametro
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def add_user(values):
    """
        Agrega al archivo de usuarios un nuevo usuario con los datos recibidos del registro y la configuracion por defecto
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
        Crea el archivo de usuarios en caso de que no exista,
        agrega un usuario con los datos recibidos del registro y la configuracion por defecto,
        y actualiza el archivo
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
    usuario = False
    gens = ["masculino", "femenino", "otros"]
    if values['-USERN-'] != "" or values['-AGE-'] != "":
        if values["-GENDER-"] in gens:
            usuario = True
    return usuario
