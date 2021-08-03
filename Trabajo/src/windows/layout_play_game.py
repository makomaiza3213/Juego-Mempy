import PySimpleGUI as sg


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
        [sg.Text(player.nick, font=("Fixedsys", 25))],
        [sg.Text(f"NIVEL {player.nivel_actual}", font=("Fixedsys", 17)), sg.Text(f"    ACIERTOS 0/{aciertos}", font=('Fixedsys', 17), key="-HITS-")]]

    matriz = []
    board = []
    for row in range(filas):
        l1 = []
        l2 = []
        for col in range(columnas):
            palabra = lista.pop()
            l1.append(palabra)
            l2.append(
                sg.Button('?', enable_events=True, size=(13, 2), pad=(0, 0), border_width=8, key=(col, row, palabra)))
        matriz.append(l1)
        board.append(l2)

    # window[i,j,palabra]
    list_buttons_colors = {"Black": ('black', 'white'),
                           "TealMono": ("white", "#1E4354"),
                           "Topanga": ("#EEDA79", "#1E4354"),
                           "DarkGreen1": ("#EEDA79", "#1E641D")}
    layout += [[sg.Column(board, k='-C-'),
                sg.Button('INICIAR', size=(8, 0), font=('Fixedsys', 15), border_width=4, button_color=list_buttons_colors[player.tema]),
                sg.Button('SALIR', size=(8, 0), font=('Fixedsys', 15), border_width=4, button_color=list_buttons_colors[player.tema])],
               [sg.Text(" ", size=(8, 0), font=('Fixedsys', 20), key="-TIMER1-")],
               [sg.Text("", size=(8, 0), font=('Fixedsys', 22), text_color="red", key="-ALERTIME-")],
               [sg.Text("PUNTOS 0", size=(20, 0), font=("Fixedsys", 15), key="-POINTS-")]]

    window = sg.Window(player.nick, layout, margins=(200, 150))
    return window, matriz
