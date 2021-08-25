import datetime

import PySimpleGUI as sg

from src.handlers.images import open_image


def warning():
    frame_yes_no = [[sg.Button("SI", font=("Fixedsys", 12), border_width=5), sg.Button("NO", font=("Fixedsys", 12), border_width=5)]]
    layout = [
        [sg.Text("¿SEGURO QUE QUIERES SALIR?", font=("Fixedsys", 15))],
        [sg.Frame("", frame_yes_no, element_justification="center")]]
    frame_warning = [[sg.Frame("", layout, element_justification="center")]]
    window = sg.Window("ADVERTENCIA", frame_warning, margins=(50, 50))
    return window


def layout_level(player, filas, columnas, lista, aciertos):
    """
        diseño de la ventana de juego
    """

    sg.theme(player.tema)

    layout = [
        [sg.Text(player.nick, font=("Fixedsys", 35))],
        [sg.Text(f"NIVEL {player.nivel_actual}", font=("Fixedsys", 25)), sg.Text(f"    ACIERTOS 0/{aciertos}", font=('Fixedsys', 25), key="-HITS-")]]

    matriz = []
    board = []
    for row in range(filas):
        l1 = []
        l2 = []
        for col in range(columnas):
            palabra = lista.pop()
            l1.append(palabra)
            if datetime.datetime.today().weekday() == 2:
                l2.append(
                    sg.Button(image_filename=open_image("question.png"), image_size=(75, 75), button_color="black",
                              enable_events=True, pad=(0, 0), border_width=8,
                              key=(col, row, palabra))
                )
            else:
                l2.append(
                    sg.Button(image_filename=open_image("question.png"), image_size=(150, 75), enable_events=True,
                              size=(13, 20), pad=(0, 0), border_width=8,
                              key=(col, row, palabra)))
        matriz.append(l1)
        board.append(l2)

    list_buttons_colors = {"Black": ('black', 'white'),
                           "TealMono": ("white", "#1E4354"),
                           "Topanga": ("#EEDA79", "#1E4354"),
                           "DarkGreen1": ("#EEDA79", "#1E641D")}
    layout += [[sg.Column(board, k='-C-'),
                sg.Button('INICIAR', size=(8, 0), font=('Fixedsys', 20), border_width=4, button_color=list_buttons_colors[player.tema]),
                sg.Button('SALIR', size=(8, 0), font=('Fixedsys', 20), border_width=4, button_color=list_buttons_colors[player.tema])],
               [sg.Text(" ", size=(8, 0), font=('Fixedsys', 20), key="-TIMER1-")],
               [sg.Text("", size=(8, 0), font=('Fixedsys', 22), text_color="red", key="-ALERTIME-")],
               [sg.Text(f"✩{player.puntaje}", size=(20, 0), font=("Fixedsys", 35), key="-POINTS-")]]

    window = sg.Window(player.nick, layout, element_justification="center", font=('Fixedsys', 15)).finalize()

    window.Maximize()

    return window, matriz
