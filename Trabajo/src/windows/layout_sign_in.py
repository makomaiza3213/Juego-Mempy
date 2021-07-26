import PySimpleGUI as sg


def login():
    """
        diseño de la ventana de inicio de la aplicacion ,para inicio de Sesion y registro
    """
    sg.theme('DarkAmber')
    layout_column = [[sg.Text("Iniciar Sesion", size=(10, 1), font=("Helvetica", 25))],
                     [sg.Text('Usuario', font=("Helvetica", 12))],
                     [sg.InputText(size=(15, 1), font='Default 12', key='-USERNAME-')],
                     [sg.Button('Entrar', font=("Helvetica", 12))],
                     [sg.Text('¿Eres nuevo?', font=("Helvetica", 20))],
                     [sg.Button('Registrate', font=("Helvetica", 12))],
                     [sg.Button("Salir ", font=("Helvetica", 12), button_color=('White', 'red'))]]

    window = sg.Window("Welcome!", layout_column, element_justification='center', margins=(200, 150))
    return window
