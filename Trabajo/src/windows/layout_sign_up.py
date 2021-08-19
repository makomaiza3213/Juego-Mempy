import PySimpleGUI as sg

from src.handlers.images import open_image


def open_sign_up():
    """
        diseño de la ventana de Registro de un jugador
    """
    sg.theme('DarkAmber')

    logo = open_image("logo.png")
    Sign_layout = [
                   [sg.Text("", size=(0, 7))],

                   [sg.Button(image_filename=logo, border_width=10, key="-LOGO-")],

                   [sg.Text("", size=(0, 3))],

                   [sg.Text('INGRESA TUS DATOS', font=("Fixedsys", 30))],

                   [sg.Text("", size=(0, 2))],

                   [sg.Text('Nick  ', font=("Fixedsys", 22), justification="center"),
                    sg.InputText(size=(16, 1), font=("Fixedsys", 15), key='-USERN-')],

                   [sg.Text("", size=(0, 2))],

                   [sg.Text('Edad  ', font=("Fixedsys", 22), justification="center"),
                    sg.InputText(size=(16, 1), font=("Fixedsys", 15), key='-AGE-')],

                   [sg.Text("", size=(0, 2))],

                   [sg.Text('Genero', font=("Fixedsys", 20), justification="center"),
                    sg.InputCombo(["masculino", "femenino", "otros"], size=(15, 1), font=("Fixedsys", 15), key='-GENDER-')],

                   [sg.Text("", size=(0, 2))],

                   [sg.Button('GUARDAR', font=("Fixedsys", 15), border_width=8)]
                ]
    window = sg.Window('Registro', Sign_layout, element_justification="center").finalize()

    window.Maximize()

    return window
