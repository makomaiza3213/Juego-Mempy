import PySimpleGUI as sg
from src.handlers.scores import file_scores
from src.windows import layout_sign_in as layout
from src.component import new_user, menu_game, class_player
from src.handlers import login as lg
from src.handlers import selection as sl
import os
from src.handlers import sounds


def loop():
    """
        capta los eventos y los valores de entrada para su procesamiento y posterior redirigido correcto
    """
    window = layout.login()
    sounds.play_sound('game music.wav')
    event, values = window.read()
    if event == "ENTRAR":
        sounds.play_sound('click.wav')
        if os.path.exists("usuarios.json"):
            usuario = lg.buscar(values['-USERNAME-'])
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

    if event == "REGISTRATE":
        sounds.play_sound('click.wav')
        window.close()
        new_user.start()


def start():
    """
        Lanza la ejecución de la ventana del menú de inicio de sesión y registro
    """
    loop()
