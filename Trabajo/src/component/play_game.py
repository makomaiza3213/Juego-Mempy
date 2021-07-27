import PySimpleGUI as sg
from src.component.write import write_csv
from src.handlers.play_game import two_touchs, three_touchs, score, \
    previous_functionalities_starting_a_game, pre_initializations_for_the_component, playtime_features, verify_winner
from src.handlers import sounds
from src.windows import layout_play_game


def loop(player, lista):
    """
        loop que capta los eventos de la ventana como el tablero y otros botones, visualizacion de datos en ventana como
        el tiempo, funcionalidades del juego , control de datos y sus pertinentes avisos
    """
    lista, min_cont, sec_cont, time_cont, list_elements, found_list, sec, min, fin, timer_running, first_touch, second_touch, three_touch, list_elems_touch, cant, play_data = pre_initializations_for_the_component(player, lista)

    window, matriz = layout_play_game.layout_level(player, list_elements[0], list_elements[1], list_elements[3],
                                                   list_elements[4])
    while True:
        event, values = window.read()
        try:
            if event in 'INICIAR':
                sounds.play_sound("click.wav")
                play_data, timer_running = previous_functionalities_starting_a_game(player, matriz, window, play_data, timer_running)
                break
        except TypeError:
            print("Debe presionar Iniciar para empezar a jugar")

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
                if event == "SI ":
                    write_csv("fin", play_data, "abandonada")
                    window_warning.close()
                    window.close()
                    break
                if event == "NO":
                    window_warning.close()

            if type(event) is tuple:

                fila, colum, data = event
                window[(fila, colum, data)].update(data)
                # fileDir = os.path.dirname(os.path.realpath('__file__'))  # para las imagenes linea 57 58
                # window[(fila, colum, data)].update(image_filename=os.path.join(fileDir, "src", "images", data))

                window.refresh()

                if player.nivel['coincidencias'] == 2:
                    list_elems_touch = two_touchs((fila, colum, data), window, fin, min, sec, first_touch, second_touch,
                                                  play_data, found_list, player)
                    first_touch = list_elems_touch[3]
                    second_touch = list_elems_touch[4]
                    fin = list_elems_touch[0]
                else:
                    list_elems_touch = three_touchs((fila, colum, data), window, fin, min, sec, first_touch,
                                                    second_touch,
                                                    three_touch, play_data, found_list, player)
                    first_touch = list_elems_touch[3]
                    second_touch = list_elems_touch[4]
                    three_touch = list_elems_touch[5]
                    fin = list_elems_touch[0]

            timer_running, min, sec, sec_cont, min_cont, play_data = playtime_features(timer_running, window, min, sec, sec_cont, min_cont, play_data, player)
            if not timer_running:
                break

            window["-HITS-"].update(str(fin) + "/" + str(list_elements[4]))

            list_elems_touch, fin, list_elements, timer_running = verify_winner(list_elems_touch, fin, list_elements, player, sec_cont, min_cont, timer_running, play_data)
            if not timer_running:
                break

    return window


def start(player, lista):
    """
        Lanza la ejecución de la ventana de juego y su posterior cierre
    """
    window_game = loop(player, lista)
    window_game.close()
