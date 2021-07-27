import PySimpleGUI as sg


def warning():
    frame_yes_no = [[sg.Button("SI ", font=("Helvetica", 12), border_width=5), sg.Button("NO", font=("Helvetica", 12), border_width=5)]]
    layout = [
        [sg.Text("¿SEGURO QUE QUIERES SALIR?", font=("Helvetica", 15))],
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
        [sg.Text(player.nick, font=('Helvetica', 25)), sg.Text(f"0/{aciertos}", font=('Helvetica', 15), key="-HITS-")]]

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
    layout += [[sg.Column(board, k='-C-'),
                sg.Button('INICIAR', size=(8, 0), font=('Helvetica', 15), button_color=('white', 'red')),
                sg.Button('SALIR', size=(8, 0), font=('Helvetica', 15), button_color=('white', 'red'))],
               [sg.Text(" ", size=(8, 0), font=('Helvetica', 20), key="-TIMER1-")],
               [sg.Text("", size=(8, 0), font=('Helvetica', 22), text_color="red", key="-ALERTIME-")]]

    window = sg.Window(player.nick, layout, margins=(200, 150))
    return window, matriz
