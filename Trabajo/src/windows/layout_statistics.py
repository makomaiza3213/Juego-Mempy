import PySimpleGUI as sg
from matplotlib import pyplot as plt


def menu_statistics():
    """
        diseño de la ventana del menu del juego 
    """
    sg.theme('DarkAmber')
    layout = [[sg.Button('TOP10', size=(30, 3), font=('Trajan', 12))],
              [sg.Button('PARTIDAS POR ESTADO', size=(30, 3), font=('Trajan', 12))],
              [sg.Button('PARTIDAS FINALIZADAS POR GENERO', size=(30, 3), font=('Trajan', 12))],
              [sg.Button('PROMEDIO DE TIEMPO DE PARTIDAS FINALIZADAS POR NIVEL', size=(30, 3), font=('Trajan', 12))],
              [sg.Button('SALIR', size=(30, 3), font=("Helvetica", 12), button_color=('White', 'red'))]]
    window_menu = sg.Window('Menú de las estadisticas', layout, margins=(300, 200))
    return window_menu


def layout_top_10(lista_p):
    """
        diseño de la ventana del menu del juego 
    """
    print(lista_p)

    sg.theme('DarkAmber')
    layout = [[sg.Table(lista_p, headings=["PALABRAS"])],
              [sg.Button("Salir", font=("Helvetica", 12), button_color=('White', 'red'))]]

    window = sg.Window('TOP 10', layout, margins=(150, 100))
    return window


def layout_porc_genero():
    sg.theme('LightGrey')
    AppFont = 'Any 16'
    layout = [[sg.Canvas(key='figCanvas')],
              [sg.Button('Salir', font=AppFont)]]
    window = sg.Window('Porcentaje de partidas por estado',
                       layout,
                       finalize=True,
                       resizable=True,
                       element_justification="right")
    fig = plt.figure()
    return window, fig


def layout_porc_nivel():
    sg.theme('LightGrey')
    AppFont = 'Any 16'
    layout = [[sg.Canvas(key='figCanvas')],
              [sg.Button('Salir', font=AppFont)]]
    window = sg.Window('Promedio de tiempo de partidas finalizadas por nivel',
                       layout,
                       finalize=True,
                       resizable=True)
    fig = plt.figure()
    return window, fig
