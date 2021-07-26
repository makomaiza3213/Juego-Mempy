import PySimpleGUI as sg
from src.windows import layout_menu_configurations as layout
from src.handlers import config as cfg
from src.handlers import sounds


def loop(player, lista):
    """
        loop para la ventana de configuraciones que se encarga de captar eventos y tomar los valores de entrada
        para la correcta creación y ejecución de la ventana de juego
    """
    window = layout.menu_configurations(player)
    #list_key = ['-DIM1-', '-DIM2-', '-COINCID-', '-TIME-']
    # for key in list_key:
    #    window.FindElement(key).Update(disabled=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        # if values['-LV4-']:
        #    for key in list_key:
        #        window.FindElement(key).Update(disabled=False)
        # if not values['-LV4-']:
        #    for key in list_key:
        #        window.FindElement(key).Update(disabled=True)
        if event == '-GUARDAR-':
            sounds.play_sound("click.wav")
            if values['-LV4-']:
                if cfg.verify(values):
                    sg.Popup("Guardado")
                    window.Refresh()
                    cfg.save_config(player, values)
                else:
                    sg.popup("Elija valores permitidos")
            else:
                if cfg.verify_123(values):
                    cfg.save_config(player, values)
                    sg.Popup("Guardado")
                    window.Refresh()
                else:
                    sg.popup("Elija valores permitidos")

        if event == '-VOLVER-':
            sounds.play_sound("click.wav")
            break
    return window


def start(player, lista):
    """
        Ejecución de la ventana de configuraciones y su posterior cierre de ejecución
    """
    window_configuration = loop(player, lista)
    window_configuration.close()
