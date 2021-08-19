import PySimpleGUI as sg


def table_scores(l1, l2, l3, l4):
    """
        diseño de la tabla de puntuaciones
    """
    sg.theme('Dark Brown 1')

    tab1 = [
        [sg.Table(l1, headings=["      USUARIO   ", "     PUNTAJE "], size=(10, 10), font=("Fixedsys", 10))],
    ]

    tab2 = [
        [sg.Table(l2, headings=["      USUARIO   ", "     PUNTAJE "], size=(10, 10), font=("Fixedsys", 10))],
    ]

    tab3 = [
        [sg.Table(l3, headings=["      USUARIO   ", "     PUNTAJE "], size=(10, 10), font=("Fixedsys", 10))],
    ]

    tab4 = [
        [sg.Table(l4, headings=["      USUARIO   ", "     PUNTAJE "], size=(10, 10), font=("Fixedsys", 10))],
    ]

    tablero = [[sg.TabGroup([[sg.Tab('   NIVEL 1     ', tab1, font=("Fixedsys", 10)), sg.Tab('   NIVEL 2     ', tab2, font=("Fixedsys", 10))]])],
               [sg.TabGroup([[sg.Tab('   NIVEL 3     ', tab3, font=("Fixedsys", 10)), sg.Tab('   NIVEL 4     ', tab4, font=("Fixedsys", 10))]])],
               [sg.Button("VOLVER AL MENÚ")]]

    window = sg.Window('Table Simulation', tablero, font=("Fixedsys", 12)).finalize()

    window.Maximize()

    return window
