import PySimpleGUI as sg


def table_scores(l1, l2, l3, l4):
    """
        diseño de la tabla de puntuaciones
    """
    sg.theme('Dark Brown 1')

    tab1 = [
        [sg.Table(l1, headings=["NOMBRE  ", "PUNTAJE"], col_widths=25)],
    ]

    tab2 = [
        [sg.Table(l2, headings=["NOMBRE  ", "PUNTAJE"])],
    ]

    tab3 = [
        [sg.Table(l3, headings=["NOMBRE  ", "PUNTAJE"])],
    ]

    tab4 = [
        [sg.Table(l4, headings=["NOMBRE  ", "PUNTAJE"])],
    ]

    tablero = [[sg.TabGroup([[sg.Tab('NIVEL 1', tab1), sg.Tab('NIVEL 2', tab2)]])],
               [sg.TabGroup([[sg.Tab('NIVEL 3', tab3), sg.Tab('NIVEL 4', tab4)]])],
               [sg.Button("VOLVER AL MENÚ")]]

    window = sg.Window('Table Simulation', tablero, font='Courier 12')

    return window
