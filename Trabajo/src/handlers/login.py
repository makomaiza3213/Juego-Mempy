import json
import os
from src.handlers import selection as sl
import PySimpleGUI as sg
from src.component import class_player, menu_game, new_user
from src.handlers.scores import file_scores
from src.handlers import sounds


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


def functionalities_enter(window, values):
    """
        Verificacion de la existencia del archivo json de usuarios,
        busqueda del usuario
        instanciacion del objeto player
        creacion del archivo  json de puntuaciones
    """
    window.close()
    sounds.play_sound('click.wav')
    if os.path.exists("usuarios.json"):
        usuario = buscar(values['-USERNAME-'])
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