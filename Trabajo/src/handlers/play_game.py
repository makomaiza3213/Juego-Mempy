from src.component.write import write_csv, create_csv
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
    sec, min = 60, player.nivel['tiempo_juego'] - 1  # sec y min , controlan el temporizador
    fin = 0
    timer_running = False
    first_touch, second_touch, three_touch, list_elems_touch = None, None, None, []
    cant = int(((list_elements[0] * list_elements[1]) / player.nivel['coincidencias']))
    play_data = [1, cant, player.nick, player.genero, player.edad, nivel]
    return lista, min_cont, sec_cont, time_cont, list_elements, found_list, sec, min, fin, timer_running, first_touch, second_touch, three_touch, list_elems_touch, cant, play_data


def previous_functionalities_starting_a_game(player, matriz, window, play_data, timer_running):
    """
        funcionalidades previas al inicio de una partida
    """
    window.FindElement("INICIAR").Update(disabled=True)
    show_words(player, matriz, window)
    timer_running = True
    create_csv(play_data)
    write_csv("inicio_partida", play_data)
    player.puntaje = 0
    player.attempt_ok = 0
    player.attempt_error = 0
    return play_data, timer_running


def show_words(player, matriz, window):
    """
        Muestra todas las palabras del tablero antes de iniciar la partida
    """
    for i in range(player.nivel["dimensiones"]["x"]):
        for j in range(player.nivel["dimensiones"]["y"]):
            window[(j, i, matriz[i][j])].update(matriz[i][j])
    window.refresh()
    time.sleep(5)
    for i in range(player.nivel["dimensiones"]["x"]):
        for j in range(player.nivel["dimensiones"]["y"]):
            window[(j, i, matriz[i][j])].update("?")
    window.refresh()


def playtime_features(timer_running, window, min, sec, sec_cont, min_cont, play_data, player):
    if timer_running:
        window['-TIMER1-'].update('{:02d}:{:02d}'.format(min, sec))
        sec -= 1
        sec_cont += 1

    if (sec == 0) and (min == 0):
        timer_running = False
        write_csv("fin", play_data, "timeout")
        sg.Popup(player.msj_derrota)

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


def verify_winner(list_elems_touch, fin, list_elements, player, sec_cont, min_cont, timer_running, play_data):
    if list_elems_touch is not None:
        if fin == list_elements[4]:  # comprobar si ganaste
            timer_running = False
            sounds.play_sound('victory.wav')
            score(player, sec_cont, min_cont)
            write_csv("fin", play_data, "finalizada", "", player.puntaje)
            update_scores(player)
            player.puntaje_0 = 0
            player.attempt_ok_0 = 0
            player.attempt_error_0 = 0
            sg.popup(player.msj_victoria)
    return list_elems_touch, fin, list_elements, timer_running


def score_level_1(player, sec, pje_time, pje_attempt):
    if 5 <= sec <= 15:
        player.puntaje = pje_time
        if player.attempt_ok > player.attempt_error:
            player.puntaje = pje_attempt
    elif 16 <= sec <= 30:
        player.puntaje = pje_time - 20
        if player.attempt_ok > player.attempt_error:
            player.puntaje = pje_attempt
    elif 31 <= sec <= 45:
        player.puntaje = pje_time - 40
        if player.attempt_ok > player.attempt_error:
            player.puntaje = pje_attempt
    else:
        player.puntaje = pje_time - 70
        if player.attempt_ok > player.attempt_error:
            player.puntaje = pje_attempt


def score_level_2(player, sec, min, pje_time, pje_attempt):
    if min == 0:
        if 5 <= sec <= 30:
            player.puntaje = pje_time
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
        elif 31 <= sec <= 60:
            player.puntaje = pje_time - 40
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt

    else:
        if 0 <= sec <= 30:
            player.puntaje = pje_time - 80
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
        elif 31 <= sec <= 60:
            player.puntaje = pje_time - 130
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt


def score_level_3(player, sec, min, pje_time, pje_attempt):
    if min == 0:
        if 5 <= sec <= 30:
            player.puntaje = pje_time
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
        elif 31 <= sec <= 60:
            player.puntaje = pje_time - 50
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
    elif min == 1:
        if 0 <= sec <= 30:
            player.puntaje = pje_time - 100
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
        elif 31 <= sec <= 60:
            player.puntaje = pje_time - 150
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
    else:
        if 0 <= sec <= 30:
            player.puntaje = pje_time - 175
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
        elif 31 <= sec <= 60:
            player.puntaje = pje_time - 190
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt


def score_level_4(player, sec, min, pje_time, pje_attempt):
    if min == 0:
        if sec <= 59:
            player.puntaje = pje_time
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
    elif min == 1:
        if 0 <= sec <= 30:
            player.puntaje = pje_time - 100  # 250
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
        elif 31 <= sec <= 60:
            player.puntaje = pje_time - 150  # 200
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
    elif min == 2:
        if 0 <= sec <= 30:
            player.puntaje = pje_time - 200  # 150
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt
        elif 31 <= sec <= 60:
            player.puntaje = pje_time - 300  # 50
            if player.attempt_ok > player.attempt_error:
                player.puntaje = pje_attempt


def score(player, sec, min):
    if player.nivel_actual == "1":
        score_level_1(player, sec, pje_time=80, pje_attempt=20)
    elif player.nivel_actual == "2":
        score_level_2(player, sec, min, pje_time=160, pje_attempt=40)
    elif player.nivel_actual == "3":
        score_level_3(player, sec, min, pje_time=250, pje_attempt=50)
    else:
        if player.nivel_actual == "4":
            score_level_4(player, sec, min, pje_time=350, pje_attempt=50)


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


def two_touchs(tupla, window, fin, min, sec, first_touch, second_touch, const, found_list, player):
    if first_touch is None:
        first_touch = (tupla[0], tupla[1], tupla[2])
        write_csv("intento_Error", const, "Error", tupla[2])
    elif second_touch is None:
        second_touch = (tupla[0], tupla[1], tupla[2])

    if first_touch is not None and second_touch is not None:
        if first_touch[2] not in found_list and second_touch[2] not in found_list:
            if first_touch != second_touch:
                if first_touch[2] == second_touch[2]:
                    sounds.play_sound("pickup.wav")
                    write_csv("intento_Ok", const, "Ok", tupla[2])
                    fin += 1
                    found_list.append(first_touch[2])
                    first_touch = None
                    second_touch = None
                    player.attempt_ok += 1
                else:
                    sounds.play_sound("broken.wav")
                    write_csv("intento_Error", const, "Error", tupla[2])
                    time.sleep(1)
                    sec -= 1
                    player.attempt_error += 1
                    # window[(fila, colum, value)].update(image_filename=os.path.join("image", value))
                    # window[first_touch].update(image_filename= 'question.png')
                    # window[second_touch].update(image_filename= 'question.png')

                    window[first_touch].update('?')  # , image_filename=None
                    window[second_touch].update('?')  # , image_filename=None
                    first_touch = None
                    second_touch = None
                    window.refresh()
            else:
                second_touch = None
        elif first_touch[2] in found_list:
            first_touch = None
        elif second_touch[2] in found_list:
            second_touch = None
    return [fin, min, sec, first_touch, second_touch, found_list]


def three_touchs(tupla, window, fin, min, sec, first_touch, second_touch, three_touch, const, found_list, player):
    if first_touch is None:
        first_touch = (tupla[0], tupla[1], tupla[2])
        write_csv("intento_Error", const, "Error", tupla[2])
    elif second_touch is None:
        second_touch = (tupla[0], tupla[1], tupla[2])
        write_csv("intento_Error", const, "Error", tupla[2])
    elif three_touch is None:
        three_touch = (tupla[0], tupla[1], tupla[2])

    if first_touch is not None and second_touch is not None and three_touch is not None:
        if first_touch[2] not in found_list and second_touch[2] not in found_list and three_touch[2] not in found_list:
            if (first_touch != second_touch) and (second_touch != three_touch) and (first_touch != three_touch):
                if first_touch[2] == second_touch[2] == three_touch[2]:
                    sounds.play_sound("pickup.wav")
                    write_csv("intento_Ok", const, "Ok", tupla[2])
                    fin += 1
                    found_list.append(first_touch[2])
                    player.attempt_ok += 1
                    first_touch = None
                    second_touch = None
                    three_touch = None
                else:
                    sounds.play_sound("broken.wav")
                    write_csv("intento_Error", const, "Error", tupla[2])
                    time.sleep(1)
                    sec -= 1
                    player.attempt_error += 1
                    # window[first_touch].update(image_filename= 'question.png')
                    # window[second_touch].update(image_filename= 'question.png')
                    window[first_touch].update('?')
                    window[second_touch].update('?')
                    window[three_touch].update('?')
                    first_touch = None
                    second_touch = None
                    three_touch = None
            else:
                if first_touch == second_touch:
                    second_touch = None
                elif second_touch == three_touch:
                    three_touch = None
                elif (first_touch != second_touch) and first_touch == three_touch:
                    three_touch = None
        elif first_touch[2] in found_list:
            first_touch = None
        elif second_touch[2] in found_list:
            second_touch = None
        elif three_touch[2] in found_list:
            three_touch = None
    return [fin, min, sec, first_touch, second_touch, three_touch]