import datetime
import os

import pygame

from src.handlers.images import open_image
from src.handlers.write import write_csv, create_csv
from src.handlers import sounds
import random
import time
import PySimpleGUI as sg

from src.handlers.scores import update_scores


def pre_initializations_for_the_component(player, lista):
    min_cont, sec_cont = 0, 0  # variables para llevar el tiempo de forma ascendente
    time_cont = 0
    list_elements = board_elements(player, lista)
    found_list = []
    nivel = player.nivel_actual
    sec = 0  # sec y min , controlan el temporizador
    if player.nivel['tiempo_juego'] != 0:
        min = player.nivel['tiempo_juego'] - 1
        sec = 60
    else:
        if player.nivel['tiempo_juego'] == 0:
            min = player.nivel['tiempo_juego']
            if nivel == "1":
                sec = 20
            elif nivel == "2":
                sec = 15
            elif nivel == "3":
                sec = 10
    fin = 0
    timer_running = False
    list_touchs = [None, None, None]
    list_elems_touch = []
    cant = int(((list_elements[0] * list_elements[1]) / player.nivel['coincidencias']))
    play_data = [1, cant, player.nick, player.genero, player.edad, nivel]
    return lista, min_cont, sec_cont, time_cont, list_elements, found_list, sec, min, fin, timer_running, list_touchs, list_elems_touch, cant, play_data


def previous_functionalities_starting_a_game(player, matriz, window, play_data, timer_running):
    """
        funcionalidades previas al inicio de una partida
    """
    window.FindElement("INICIAR").Update(disabled=True)
    show_words(player, matriz, window)
    timer_running = True
    file_plays = create_csv(play_data)
    file_plays = write_csv("inicio_partida", play_data, file_plays)
    player.puntaje_0 = 0
    window["-POINTS-"].update(f"✩ {0}")
    return play_data, timer_running, file_plays


def time_sleep(player):
    if player.nivel_actual == "1":
        time.sleep(1)
    elif player.nivel_actual == "2":
        time.sleep(2)
    elif player.nivel_actual == "3":
        time.sleep(2)
    elif player.nivel_actual == "4":
        if player.nivel["dimensiones"]["x"] * player.nivel["dimensiones"]["y"] == 16:
            time.sleep(4)
        elif player.nivel["dimensiones"]["x"] * player.nivel["dimensiones"]["y"] == 20:
            time.sleep(5)
        elif player.nivel["dimensiones"]["x"] * player.nivel["dimensiones"]["y"] == 24:
            time.sleep(6)
        elif player.nivel["dimensiones"]["x"] * player.nivel["dimensiones"]["y"] == 30:
            time.sleep(8)


def show_words(player, matriz, window):
    """
        Muestra todas las palabras del tablero antes de iniciar la partida
    """
    list_buttons_colors = {"Black": 'blanco.png',
                           "TealMono": "azul.png",
                           "Topanga": "azul.png",
                           "DarkGreen1": "verde.png"}

    for i in range(player.nivel["dimensiones"]["x"]):
        for j in range(player.nivel["dimensiones"]["y"]):
            if datetime.datetime.today().weekday() != 2:
                window[(j, i, matriz[i][j])].update(matriz[i][j], image_size=(150, 75),
                                                    image_filename=open_image(list_buttons_colors[player.tema]))
            else:
                window[(j, i, matriz[i][j])].update(image_filename=open_image(matriz[i][j]), image_size=(75, 75))
    window.refresh()

    time_sleep(player)

    for i in range(player.nivel["dimensiones"]["x"]):
        for j in range(player.nivel["dimensiones"]["y"]):
            if datetime.datetime.today().weekday() != 2:
                window[(j, i, matriz[i][j])].update("", image_size=(150, 75),
                                                    image_filename=open_image("question.png"))
            else:
                window[(j, i, matriz[i][j])].update(image_filename=open_image("question.png"), image_size=(75, 75))

    window.refresh()


def playtime_features(timer_running, window, min, sec, sec_cont, min_cont, play_data, player, file_plays):
    if timer_running:
        window['-TIMER1-'].update('{:02d}:{:02d}'.format(min, sec))
        sec -= 1
        sec_cont += 1

    if (sec == 0) and (min == 0):
        timer_running = False
        file_plays = write_csv("fin", play_data, file_plays, "timeout")
        file_plays.close()
        sounds.play_sound("defeat2.wav")
        popup_victory_defeat(player, player.msj_derrota)

    if sec == 0:
        min -= 1
        sec = 60

    alert_time(player, window, min, sec)

    if sec_cont == 60:
        min_cont += 1
        sec_cont = 0

    return timer_running, min, sec, sec_cont, min_cont, play_data


def alert_time(player, window, min, sec):
    if min == 0:
        if sec <= 15 and sec % 2 != 0:
            window["-ALERTIME-"].update(player.msj_tiempo)
        elif sec <= 15 and sec % 2 == 0:
            window["-ALERTIME-"].update("")


def verify_winner(list_elems_touch, fin, list_elements, player, sec_cont, min_cont, timer_running, play_data,
                  file_plays):
    if list_elems_touch is not None:
        if fin == list_elements[4]:  # comprobar si ganaste
            timer_running = False
            pygame.mixer.pause()
            sounds.play_sound('correct.wav')
            pygame.mixer.unpause()
            file_plays = write_csv("fin", play_data, file_plays, "finalizada", "", player.puntaje)
            file_plays.close()
            update_scores(player)
            player.puntaje_0 = 0
            popup_victory_defeat(player, player.msj_victoria)

    return list_elems_touch, fin, list_elements, timer_running


def popup_victory_defeat(player, msj):
    color_background_text = {"Black": ('black', 'white'),
                           "TealMono": ("white", "#193b4b"),
                           "Topanga": ("#fce896", "#193b4b"),
                           "DarkGreen1": ("#fce896", "#1e641d")}

    for x in range(3):
        sg.popup(msj, title="VICTORIA!", font=('Fixedsys', 30), auto_close=True,
                 auto_close_duration=1, background_color=color_background_text[player.tema][1],
                 text_color=color_background_text[player.tema][0],
                 location=(650, 650), no_titlebar=True, button_type=5)


def update_score_by_game(player, sec, min):
    points = {"1": {
        range(0, 3): 50,
        range(3, 6): 50,
        range(6, 10): 40,
        range(10, 14): 30,
        range(14, 18): 20,
        range(18, 20): 10
    },
        "2": {
            range(0, 3): 70,
            range(3, 6): 70,
            range(6, 10): 60,
            range(10, 15): 50,
        },
        "3": {
            range(0, 2): 75,
            range(2, 5): 75,
            range(5, 8): 75,
            range(8, 10): 75,
        },
        "4": {
            "0": {
                range(0, 5): 200,
                range(5, 11): 100,
                range(11, 16): 100,
                range(16, 25): 100,
                range(25, 30): 100,
                range(30, 36): 100,
                range(36, 44): 100,
                range(44, 50): 100,
                range(50, 60): 100,
            },
            "1": {
                range(0, 5): 100,
                range(5, 11): 75,
                range(11, 16): 75,
                range(16, 25): 75,
                range(25, 30): 75,
                range(30, 36): 75,
                range(36, 44): 75,
                range(44, 50): 75,
                range(50, 60): 75
            },
            "2": {
                range(0, 5): 50,
                range(5, 11): 25,
                range(11, 16): 25,
                range(16, 25): 25,
                range(25, 30): 25,
                range(30, 36): 25,
                range(36, 44): 25,
                range(44, 50): 25,
                range(50, 60): 25
            }
        },
    }

    if player.nivel_actual == "4":
        valores = points[player.nivel_actual][str(min)]
        valores = valores.items()
        list_points = list(valores)
        for x in list_points:
            if sec in x[0]:
                player.puntaje = x[1]
    else:
        list_points = points[player.nivel_actual]
        for rango, pts in list_points.items():
            if sec in rango:
                player.puntaje = pts


def board_elements(player, lista):
    """
    Esta funcion calcula con cuantos elementos se va a graficar la grilla:
    @param player: informacion del jugador actual
    @param lista: elementos posibles a utilizar
    @return: una determinada cantidad de elementos correspondientes a las dimensiones del tablero
    """
    nivel = player.nivel_actual
    filas = player.nivel["dimensiones"]["x"]
    columnas = player.nivel["dimensiones"]["y"]
    coincid = player.nivel["coincidencias"]
    num = int(((filas * columnas) / coincid))
    random.shuffle(lista)
    lista = lista[:num]
    lista = coincid * lista
    random.shuffle(lista)
    return [filas, columnas, nivel, lista, num]


def touch_controller(tupla, window, fin, min, sec, list_touchs, const, found_list, player, sec_cont, min_cont,
                     file_plays):
    if list_touchs[0] is None:
        list_touchs[0] = (tupla[0], tupla[1], tupla[2])
        write_csv("intento_Error", const, file_plays, "Error", tupla[2])
    elif list_touchs[1] is None:
        list_touchs[1] = (tupla[0], tupla[1], tupla[2])
    elif player.nivel['coincidencias'] == 3:
        if list_touchs[2] is None:
            list_touchs[2] = (tupla[0], tupla[1], tupla[2])

    if (list_touchs[0] is not None and list_touchs[1] is not None and list_touchs[2] is not None) or (
            list_touchs[0] is not None and list_touchs[1] is not None and player.nivel["coincidencias"] == 2):
        if (list_touchs[0][2] not in found_list and list_touchs[1][2] not in found_list and player.nivel["coincidencias"] == 2) or (
                list_touchs[0][2] not in found_list and list_touchs[1][2] not in found_list and
                list_touchs[2][2] not in found_list):
            if (list_touchs[0] != list_touchs[1]) and (
                    list_touchs[1] != list_touchs[2] and list_touchs[0] != list_touchs[2]) or (
                    list_touchs[0] != list_touchs[1]) and (list_touchs[1] != list_touchs[2]):
                if (list_touchs[0][2] == list_touchs[1][2] and player.nivel["coincidencias"] == 2) or (
                        list_touchs[0][2] == list_touchs[1][2] == list_touchs[2][2] and
                        player.nivel["coincidencias"] == 3):
                    sounds.play_sound("ok.wav")
                    file_plays = write_csv("intento_Ok", const, file_plays, "Ok", tupla[2])
                    fin += 1
                    found_list.append(list_touchs[0][2])
                    update_score_by_game(player, sec_cont, min_cont)
                    window["-POINTS-"].update(f"✩ {str(player.puntaje)}", text_color="green")
                    list_touchs[0] = None
                    list_touchs[1] = None
                    list_touchs[2] = None
                else:
                    sounds.play_sound("error.wav")
                    file_plays = write_csv("intento_Error", const, file_plays, "Error", tupla[2])
                    time.sleep(1)
                    sec -= 1
                    if datetime.datetime.today().weekday() == 2:
                        fileDir = os.path.dirname(os.path.realpath('__file__'))
                        window[list_touchs[0]].update(
                            image_filename=os.path.join(fileDir, "src", "images", 'question.png'), image_size=(75, 75))
                        window[list_touchs[1]].update(
                            image_filename=os.path.join(fileDir, "src", "images", 'question.png'), image_size=(75, 75))
                        if player.nivel["coincidencias"] == 3:
                            window[list_touchs[2]].update(
                                image_filename=os.path.join(fileDir, "src", "images", 'question.png'),
                                image_size=(75, 75))
                    else:
                        fileDir = os.path.dirname(os.path.realpath('__file__'))
                        window[list_touchs[0]].update(
                            "",
                            image_filename=os.path.join(fileDir, "src", "images", 'question.png'), image_size=(150, 75)
                        )
                        window[list_touchs[1]].update(
                            "",
                            image_filename=os.path.join(fileDir, "src", "images", 'question.png'), image_size=(150, 75)
                        )
                        if player.nivel["coincidencias"] == 3:
                            window[list_touchs[2]].update(
                                "",
                                image_filename=os.path.join(fileDir, "src", "images", 'question.png'),
                                image_size=(150, 75)
                            )
                    list_touchs[0] = None
                    list_touchs[1] = None
                    list_touchs[2] = None
            else:
                if list_touchs[0] == list_touchs[1]:
                    list_touchs[1] = None
                elif list_touchs[1] == list_touchs[2]:
                    list_touchs[2] = None
                elif (list_touchs[0] != list_touchs[1]) and list_touchs[0] == list_touchs[2]:
                    list_touchs[2] = None
        elif list_touchs[0][2] in found_list:
            list_touchs[0] = None
        elif list_touchs[1][2] in found_list:
            list_touchs[1] = None
        elif list_touchs[2][2] in found_list:
            list_touchs[2] = None
    return [fin, min, sec, list_touchs]
