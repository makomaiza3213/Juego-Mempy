import datetime
import os

import PySimpleGUI as sg
from src.handlers.write import write_csv
from src.handlers.play_game import \
    previous_functionalities_starting_a_game, pre_initializations_for_the_component, playtime_features, verify_winner, \
    touch_controller
from src.handlers import sounds
from src.windows import layout_play_game


def loop(player, lista):
    """
        loop que capta los eventos de la ventana como el tablero y otros botones, visualizacion de datos en ventana como
        el tiempo, funcionalidades del juego , control de datos y sus pertinentes avisos
    """
    lista, min_cont, sec_cont, time_cont, list_elements, found_list, sec, min, fin, timer_running, list_touchs, list_elems_touch, cant, play_data = pre_initializations_for_the_component(player, lista)

    window, matriz = layout_play_game.layout_level(player, list_elements[0], list_elements[1], list_elements[3],
                                                   list_elements[4])

    while True:
        event, values = window.read()
        try:
            if event in 'INICIAR':
                sounds.play_sound("click.wav")
                play_data, timer_running, file_plays = previous_functionalities_starting_a_game(player, matriz, window, play_data, timer_running)
                break
        except TypeError:
            print("Presione INICIAR para jugar")

        if event in (sg.WIN_CLOSED, 'SALIR'):
            sounds.play_sound("click.wav")
            window.close()
            break

    if event in "INICIAR":
        while True:
            event, values = window.read(timeout=1000)

            if event in (sg.WIN_CLOSED, 'SALIR'):
                sounds.play_sound("click.wav")
                window_warning = layout_play_game.warning()
                event, values = window_warning.read()
                if event == "SI":
                    write_csv("fin", play_data, file_plays, "abandonada")
                    window_warning.close()
                    window.close()
                    break
                if event == "NO":
                    window_warning.close()

            if type(event) is tuple:

                fila, colum, data = event
                list_buttons_colors = {"Black": 'blanco.png',
                                       "TealMono": "azul.png",
                                       "Topanga": "azul.png",
                                       "DarkGreen1": "verde.png"}
                if datetime.datetime.today().weekday() != 2:
                    fileDir = os.path.dirname(os.path.realpath('__file__'))
                    window[(fila, colum, data)].update(data, image_size=(150, 75),
                                                       image_filename=os.path.join(fileDir, "src", "images", list_buttons_colors[player.tema]))
                else:
                    fileDir = os.path.dirname(os.path.realpath('__file__'))  # para las imagenes linea 57 58
                    window[(fila, colum, data)].update(image_filename=os.path.join(fileDir, "src", "images", data), image_size=(75, 75))
                window.refresh()
                list_elems_touch = touch_controller((fila, colum, data), window, fin, min, sec, list_touchs, play_data, found_list, player, sec_cont, min_cont, file_plays)
                list_touchs[0] = list_elems_touch[3][0]
                list_touchs[1] = list_elems_touch[3][1]
                list_touchs[2] = list_elems_touch[3][2]
                fin = list_elems_touch[0]

            timer_running, min, sec, sec_cont, min_cont, play_data = playtime_features(timer_running, window, min, sec, sec_cont, min_cont, play_data, player, file_plays)
            if not timer_running:
                break

            window["-HITS-"].update(str(fin) + "/" + str(list_elements[4]))

            list_elems_touch, fin, list_elements, timer_running = verify_winner(list_elems_touch, fin, list_elements, player, sec_cont, min_cont, timer_running, play_data, file_plays)
            if not timer_running:
                break

    return window


def start(player, lista):
    """
        Lanza la ejecución de la ventana de juego y su posterior cierre
    """
    window_game = loop(player, lista)
    window_game.close()
