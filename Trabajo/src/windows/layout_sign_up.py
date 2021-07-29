import PySimpleGUI as sg


def open_sign_up():
    """
        diseño de la ventana de Registro de un jugador
    """
    # prueba de commit pycharm
    sg.theme('DarkAmber')
    Sign_layout = [[sg.Text('Ingresa tus datos', font=("Fixedsys", 30))],
                   [sg.Text('Nick', font=("Fixedsys", 18)),
                    sg.InputText(size=(15, 1), font=("Fixedsys", 15), key='-USERN-')],
                   [sg.Text('Edad', font=("Fixedsys", 18)),
                    sg.InputText(size=(15, 1), font=("Fixedsys", 15), key='-AGE-')],
                   [sg.Text('Genero', font=("Fixedsys", 18)),
                    sg.InputCombo(["masculino", "femenino", "otros"], size=(15, 1), font=("Fixedsys", 15), key='-GENDER-')],
                   [sg.Button('Guardar', font=("Fixedsys", 18))]]
    window = sg.Window('Registro', Sign_layout, margins=(200, 150))
    return window
