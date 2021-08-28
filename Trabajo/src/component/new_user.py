import PySimpleGUI as sg
from src.handlers.scores import file_scores
from src.handlers.sign_up import message_incorrect_data
from src.windows import layout_sign_up as layout
from src.component import menu_game, class_player
from src.handlers import sign_up as sn
from src.handlers import selection as sl
import os.path as path
from src.handlers import sounds


def loop():
    """
        Loop de la ventana de registro que capta los eventos y valores de entrada,
        verifica la existencia del archivo usuarios.json y guarda según corresponda
    """
    window = layout.open_sign_up()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "GUARDAR":
            sounds.play_sound("click2.wav")
            message_number = sn.ok(values)
            if message_number not in range(1, 10):
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
                message_incorrect_data(message_number)

    return window


def start():
    """
        Lanza la ejecución de la ventana del registro de jugadores y su posterior cierre
    """
    window_new_user = loop()
    window_new_user.close()
