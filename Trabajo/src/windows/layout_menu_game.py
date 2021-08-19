import PySimpleGUI as sg

from src.handlers.images import open_image


def menu_game():
    """
        diseño de la ventana del menu del juego 
    """
    sg.theme('DarkAmber')
    logo = open_image("logo.png")
    menu_game_layout = [
        [sg.Text("", size=(0, 7))],
        [sg.Button(image_filename=logo, border_width=10)],
        [sg.Text("", size=(0, 4))],
        [sg.Button('JUGAR', size=(20, 2), font=('Fixedsys', 14), border_width=10)],
        [sg.Button('CONFIGURACION', size=(20, 2), font=('Fixedsys', 14), border_width=10)],
        [sg.Button('PUNTUACIONES', size=(20, 2), font=('Fixedsys', 14), border_width=10)],
        [sg.Button('ESTADISTICAS', size=(20, 2), font=('Fixedsys', 14), border_width=10)],
        [sg.Button('SALIR DEL JUEGO', size=(20, 2), font=("Fixedsys", 14), border_width=10,
                   button_color=('black', 'red'))]]
    window_menu_game = sg.Window('Menú del juego', menu_game_layout, element_justification="center").finalize()

    window_menu_game.Maximize()

    return window_menu_game
