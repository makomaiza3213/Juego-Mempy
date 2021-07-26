import PySimpleGUI as sg
from src.windows import layout_menu_game as layout
from src.component import configurations, scores, menu_statistics
from src.component import play_game
from src.handlers import sounds


def loop(player, lista):
    """
        Loop de la ventana del menú del juego que capta los eventos para su redirigido de ventana correcto
    """
    window = layout.menu_game()

    while True:

        event, values = window.read()

        if event == "JUGAR":
            sounds.play_sound("click.wav")
            window.hide()
            play_game.start(player, lista)
            window.un_hide()

        elif event == "CONFIGURACION":
            sounds.play_sound("click.wav")
            window.hide()
            configurations.start(player, lista)
            window.un_hide()

        elif event == "PUNTUACIONES":
            sounds.play_sound("click.wav")
            window.hide()
            scores.start()
            window.un_hide()

        elif event == "ESTADISTICAS":
            sounds.play_sound("click.wav")
            window.hide()
            menu_statistics.start()
            window.un_hide()

        if event in (sg.WIN_CLOSED, 'SALIR DEL JUEGO'):
            sounds.play_sound("click.wav")
            break

    return window


def start(player, lista):
    """
        Ejecucion de la ventana del menú del juego y su posterior cierre de ejecución
    """ 
    window_game_menu = loop(player, lista)
    window_game_menu.close()
