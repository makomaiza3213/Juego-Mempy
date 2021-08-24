import PySimpleGUI as sg
from src.windows import layout_statistics as layout
from src.handlers.handlers_statistics import top_10, games_state, game_by_gender, average_time
from src.handlers import sounds


def loop():
    """
        Loop de la ventana del menú de estadisticas que capta los eventos y su redirigido correcto a sus ventanas
    """
    
    window = layout.menu_statistics() 

    while True:

        event, values = window.read()
        
        if event == "TOP10":
            sounds.play_sound("click.wav")
            window.hide()
            top_10.obtener_datos()
            window.Maximize()
            window.un_hide()
        
        elif event == "PARTIDAS POR ESTADO":
            sounds.play_sound("click.wav")
            window.hide()
            games_state.state()
            window.Maximize()
            window.un_hide()

        elif event == "PARTIDAS FINALIZADAS POR GENERO":
            sounds.play_sound("click.wav")
            window.hide()
            game_by_gender.percentage_by_gender()
            window.Maximize()
            window.un_hide()
        
        elif event == "PROMEDIO DE TIEMPO DE PARTIDAS FINALIZADAS POR NIVEL":
            sounds.play_sound("click.wav")
            window.hide()
            average_time.percentage_by_nivel()
            window.Maximize()
            window.un_hide()

        if event in (sg.WIN_CLOSED, 'VOLVER AL MENÚ'):
            sounds.play_sound("click.wav")
            break    
   
    return window


def start():
    """
        Ejecucion de la ventana del menú de estadisticas y su posterior cierre
    """ 
    window_menu = loop()
    window_menu.close()
