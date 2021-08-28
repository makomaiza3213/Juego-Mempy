import PySimpleGUI as sg
import pygame.mixer

from src.windows import layout_menu_game as layout
from src.component import configurations, scores, menu_statistics
from src.component import play_game
from src.handlers import sounds


def loop(player, lista):
    """
    Loop de la ventana del menú del juego que capta
    los eventos para el redireccionamiento a la ventana correspondiente

    Args:
        player: object, datos del jugador
        lista: list, listado de palabras para el juego

    Returns:
        window: object
    """
    window = layout.menu_game()

    while True:

        event, values = window.read()

        if event == "JUGAR":
            #sounds.play_sound("click2.wav")
            window.hide()
            #pygame.mixer.stop()
            sounds.play_sound("click2.wav")
            play_game.start(player, lista)
            #sounds.play_sound("game music.wav")
            window.Maximize()
            window.un_hide()

        elif event == "CONFIGURACION":
            sounds.play_sound("click2.wav")
            window.hide()
            configurations.start(player, lista)
            window.Maximize()
            window.un_hide()

        elif event == "PUNTUACIONES":
            sounds.play_sound("click2.wav")
            window.hide()
            scores.start()
            window.Maximize()
            window.un_hide()

        elif event == "ESTADISTICAS":
            sounds.play_sound("click2.wav")
            window.hide()
            menu_statistics.start()
            window.Maximize()
            window.un_hide()

        if event in (sg.WIN_CLOSED, 'SALIR DEL JUEGO'):
            sounds.play_sound("click2.wav")
            break

    return window


def start(player, lista):
    """
    Ejecucion de la ventana del menú del juego y su posterior cierre de ejecución

    Args:
        player: object, datos del jugador
        lista: list, listado de palabras para el juego
    """
    window_game_menu = loop(player, lista)
    window_game_menu.close()
