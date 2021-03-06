import PySimpleGUI as sg
from src.windows import layout_menu_configurations as layout
from src.handlers import config as cfg
from src.handlers import sounds


def loop(player, lista):
    """
    Loop para la ventana de configuraciones que se encarga de captar eventos y
    tomar los valores de entrada y ejecución de la ventana de juego

    Args:
        player: object, datos del jugador
        lista: list, listado de palabras para el juego

    Returns:
        window: object
    """
    window = layout.menu_configurations(player)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == '-GUARDAR-':
            sounds.play_sound("click2.wav")
            if values['-LV4-']:
                if cfg.verify(values):
                    sg.Popup("Guardado", auto_close=True, auto_close_duration=2, font=("Fixedsys", 20))
                    cfg.save_config(player, values)
                else:
                    sg.popup("Configuración inválida, intente de nuevo", font=("Fixedsys", 20))
            else:
                if cfg.verify_123(values):
                    cfg.save_config(player, values)
                    sg.Popup("Guardado", auto_close=True, auto_close_duration=2, font=("Fixedsys", 20))
                else:
                    sg.popup("Configuración inválida, intente de nuevo", font=("Fixedsys", 20))

        if event == '-VOLVER-':
            sounds.play_sound("click2.wav")
            break

    return window


def start(player, lista):
    """
        Ejecución de la ventana de configuraciones y su posterior cierre de ejecución
    """
    window_configuration = loop(player, lista)
    window_configuration.close()
