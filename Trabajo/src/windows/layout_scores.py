import PySimpleGUI as sg

from src.handlers.images import open_image


def table_scores(l1, l2, l3, l4):
    """
        diseño de la tabla de puntuaciones
    """
    sg.theme('Dark Brown 1')

    logo = open_image("logo.png")

    tab1 = [
        [sg.Table(l1, headings=["      USUARIO                  ", "          PUNTAJE            "], justification="center"
                  , header_font=("Fixedsys", 16), font=("Fixedsys", 17))],
    ]

    tab2 = [
        [sg.Table(l2, headings=["      USUARIO                  ", "          PUNTAJE            "], justification="center"
                  , header_font=("Fixedsys", 16), font=("Fixedsys", 17))],
    ]

    tab3 = [
        [sg.Table(l3, headings=["      USUARIO                  ", "          PUNTAJE            "], justification="center"
                  , header_font=("Fixedsys", 16), font=("Fixedsys", 17))],
    ]

    tab4 = [
        [sg.Table(l4, headings=["      USUARIO                  ", "          PUNTAJE            "], justification="center"
                  , header_font=("Fixedsys", 16), font=("Fixedsys", 17))],
    ]

    tablero = [
               [sg.Text("", size=(0, 2))],
               [sg.Button(image_filename=logo, border_width=10)],
               [sg.Text("", size=(0, 2))],
               [sg.TabGroup([[sg.Tab('   NIVEL 1     ', tab1, font=("Fixedsys", 20)), sg.Tab('   NIVEL 2     ', tab2, font=("Fixedsys", 20))]], font=("Fixedsys", 20))],
               [sg.TabGroup([[sg.Tab('   NIVEL 3     ', tab3, font=("Fixedsys", 20)), sg.Tab('   NIVEL 4     ', tab4, font=("Fixedsys", 20))]], font=("Fixedsys", 20))],
               [sg.Text("", size=(0, 2))],
               [sg.Button("VOLVER AL MENÚ", border_width=10, font=("Fixedsys", 20))]]

    window = sg.Window('Table Simulation', tablero,
                       element_justification="center").finalize()

    window.Maximize()

    return window
