import PySimpleGUI as sg


def login():
    """
        diseño de la ventana de inicio de la aplicacion ,para inicio de Sesion y registro
    """
    sg.theme('DarkAmber')
    layout_column = [[sg.Text("INGRESAR", size=(8, 1), font=("Fixedsys", 20))],
                     [sg.Text('USUARIO', font=("Fixedsys", 15))],
                     [sg.InputText(size=(15, 1), font='Default 12', key='-USERNAME-')],
                     [sg.Button('ENTRAR', size=(10, 1), font=("Fixedsys", 12), border_width=5)],
                     [sg.Text("", size=(0, 1))],
                     [sg.Text('¿ERES NUEVO?', font=("Fixedsys", 20))],
                     [sg.Button('REGISTRATE', size=(10, 1), font=("Fixedsys", 12), border_width=5)],
                     [sg.Text("", size=(0, 1))],
                     [sg.Button(" SALIR ", font=("Fixedsys", 12), border_width=5, button_color=('black', 'red'))]]

    window = sg.Window("Welcome!", layout_column, element_justification='center', margins=(200, 150))
    return window
