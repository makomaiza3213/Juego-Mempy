import PySimpleGUI as sg
from src.handlers.scores import file_scores
from src.windows import layout_sign_up as layout
from src.component import menu_game, class_player
from src.handlers import sign_up as sn
from src.handlers import selection as sl
import os.path as path
from src.handlers import sounds


def loop():
    """
        Loop de la ventana de menú que capta los eventos y valores de entrada para su procesamiento ,
        verificación de la existencia del archivo de registro de jugadores y la correcta escritura en dicho archivo
    """
    window = layout.open_sign_up()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Guardar":
            sounds.play_sound("click.wav")
            if sn.ok(values):
                if not path.exists("usuarios.json"):
                    usuario = sn.create_file_users(values)
                    player = class_player.Player(usuario)
                else:
                    usuario = sn.add_user(values)
                    player = class_player.Player(usuario)

                lista = sl.values_hour_day()
                file_scores(player)
                window.close()
                menu_game.start(player, lista)
            else:
                sg.popup("Complete todos los campos")

    return window


def start():
    """
        Lanza la ejecución de la ventana del registro de jugadores y su posterior cierre
    """
    window_new_user = loop()
    window_new_user.close()
