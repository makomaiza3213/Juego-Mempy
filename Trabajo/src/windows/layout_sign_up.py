import PySimpleGUI as sg


def open_sign_up():
    """
        diseño de la ventana de Registro de un jugador
    """
    sg.theme('DarkAmber')
    Sign_layout = [[sg.Text('Ingresa tus datos', font=("Helvetica", 30))],
                   [sg.Text('Nick', font=("Helvetica", 18)),
                    sg.InputText(size=(15, 1), font='Default 15', key='-USERN-')],
                   [sg.Text('Edad', font=("Helvetica", 18)),
                    sg.InputText(size=(15, 1), font='Default 15', key='-AGE-')],
                   [sg.Text('Genero', font=("Helvetica", 18)),
                    sg.InputCombo(["masculino", "femenino", "otros"], size=(15, 1), font='Default 15', key='-GENDER-')],
                   [sg.Button('Guardar', font=("Helvetica", 18))]]
    window = sg.Window('Registro', Sign_layout, margins=(200, 150))
    return window
