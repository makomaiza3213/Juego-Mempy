import PySimpleGUI as sg


def menu_game():
    """
        diseño de la ventana del menu del juego 
    """
    sg.theme('DarkAmber')
    menu_game_layout = [[sg.Button('JUGAR', size=(20, 2), font=('Trajan', 10))],
                        [sg.Button('CONFIGURACION', size=(20, 2), font=('Trajan', 10))],
                        [sg.Button('PUNTUACIONES', size=(20, 2), font=('Trajan', 10))],
                        [sg.Button('ESTADISTICAS', size=(20, 2), font=('Trajan', 10))],
                        [sg.Button('SALIR DEL JUEGO',size=(20, 2),font=("Trajan", 10), button_color=('White', 'red'))]]
    window_menu_game = sg.Window('Menú del juego', menu_game_layout, margins=(300, 200))
    return window_menu_game
