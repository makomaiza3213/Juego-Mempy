import json
import os
from src.handlers import selection as sl
import PySimpleGUI as sg
from src.component import class_player, menu_game, new_user
from src.handlers.scores import file_scores
from src.handlers import sounds


def buscar(nom):
    """
        Lee y busca en el archivo el nombre que recibe por parámetro y retorna dicho usuario si lo encontró , sino retorna False
    """
    existe = False
    with open("usuarios.json") as file:
        data = json.load(file)
    for usuario in data['usuarios']:
        if usuario["nombre"] == nom.upper():
            existe = usuario
    return existe


def functionalities_enter(window, values):
    """
        Verificación de la existencia del archivo json de usuarios,
        busqueda del usuario
        instanciación del objeto player
        creación del archivo  json de puntuaciones
    """
    # window.close()
    sounds.play_sound('click.wav')
    if os.path.exists("usuarios.json"):
        usuario = buscar(values['-IN-'])
        if usuario:
            player = class_player.Player(usuario)
            lista = sl.values_hour_day()
            file_scores(player)  # crea el archivo para puntuaciones
            window.close()
            menu_game.start(player, lista)
        else:
            sg.popup("USTED DEBE REGISTRARSE")
            window.close()
            new_user.start()
    else:
        sg.popup("USTED DEBE REGISTRARSE")
        window.close()
        new_user.start()