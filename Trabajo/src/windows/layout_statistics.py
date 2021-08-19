import PySimpleGUI as sg
from matplotlib import pyplot as plt

from src.handlers.images import open_image


def menu_statistics():
    """
        diseño de la ventana del menu del juego 
    """
    sg.theme('DarkAmber')
    logo = open_image("logo.png")
    layout = [
        [sg.Text("", size=(0, 7))],
        [sg.Button(image_filename=logo, border_width=10)],
        [sg.Text("", size=(0, 4))],
        [sg.Button('TOP10', size=(31, 3), font=('Fixedsys', 12), border_width=5)],
        [sg.Button('PARTIDAS POR ESTADO', size=(31, 3), font=('Fixedsys', 12), border_width=5)],
        [sg.Button('PARTIDAS FINALIZADAS POR GENERO', size=(31, 3), font=('Fixedsys', 12), border_width=5)],
        [sg.Button('PROMEDIO DE TIEMPO DE PARTIDAS FINALIZADAS POR NIVEL', size=(31, 3), font=('Fixedsys', 12),
                   border_width=5)],
        [sg.Button('SALIR', size=(31, 3), font=("Fixedsys", 12), button_color=('black', 'red'), border_width=5)]]
    window_menu = sg.Window('Menú de las estadisticas', layout, element_justification="center").finalize()

    window_menu.Maximize()

    return window_menu


def layout_top_10(lista_p):
    """
        diseño de la ventana del menu del juego 
    """

    sg.theme('DarkAmber')

    logo = open_image("logo.png")

    layout = [[sg.Text("", size=(0, 7))],
              [sg.Button(image_filename=logo, border_width=10)],
              [sg.Text("", size=(0, 4))]]

    list_words = []
    for row in range(0, len(lista_p)):
        word = lista_p.pop()

        list_words.append([sg.Text(f"{row+1} {word}", font=("Fixedsys", 20))])

    layout += [[sg.Column(list_words)],
               [sg.Button("Salir", font=("Fixedsys", 20), button_color=('black', 'red'))]]

    window = sg.Window('TOP 10', layout, element_justification="center").finalize()

    window.Maximize()

    return window


def layout_porc_genero():
    sg.theme('DarkAmber')
    logo = open_image("logo.png")

    AppFont = ("Fixedsys", 16)
    layout = [
              [sg.Text("", size=(0, 4))],
              [sg.Button(image_filename=logo, border_width=10)],
              [sg.Text("", size=(0, 1))],
              [sg.Canvas(key='figCanvas')],
              [sg.Text("", size=(0, 1))],
              [sg.Button('Salir', font=AppFont)]]
    window = sg.Window('Porcentaje de partidas por estado',
                       layout,
                       finalize=True,
                       resizable=True,
                       element_justification="center").finalize()
    fig = plt.figure()

    window.Maximize()

    return window, fig


def layout_porc_nivel():
    sg.theme('DarkAmber')
    AppFont = ("Fixedsys", 16)
    logo = open_image("logo.png")
    layout = [
              [sg.Text("", size=(0, 4))],
              [sg.Button(image_filename=logo, border_width=10)],
              [sg.Text("", size=(0, 1))],
              [sg.Canvas(key='figCanvas')],
              [sg.Text("", size=(0, 1))],
              [sg.Button('Salir', font=AppFont)]]
    window = sg.Window('Promedio de tiempo de partidas finalizadas por nivel',
                       layout,
                       finalize=True,
                       resizable=True,
                       element_justification="center").finalize()
    fig = plt.figure()

    window.Maximize()

    return window, fig
