import PySimpleGUI as sg

from src.handlers.images import open_image


def login():
    """
        diseño de la ventana de inicio de la aplicacion ,para inicio de Sesion y registro
    """
    sg.theme('DarkAmber')
    logo = open_image("logo.png")
    layout_column = [
                     [sg.Text("", size=(0, 7))],
                     [sg.Button(image_filename=logo, border_width=10, key="-LOGO-")],
                     [sg.Text("", size=(0, 4))],
                     [sg.Text("INGRESAR", font=("Fixedsys", 33))],
                     [sg.Text('USUARIO', font=("Fixedsys", 15))],
                     [sg.InputText(border_width=5, justification="center", size=(15, 4), font=("Fixedsys", 17), key='-IN-'), sg.Button('OK', bind_return_key=True, visible=False)],
                     [sg.Button('ENTRAR', font=("Fixedsys", 17), border_width=8)],
                     [sg.Text("", size=(0, 1))],
                     [sg.Text('¿ERES NUEVO?', font=("Fixedsys", 25))],
                     [sg.Button('REGISTRATE', font=("Fixedsys", 17), border_width=8)],
                     [sg.Text("", size=(0, 4))],
                     [sg.Button(" SALIR DEL JUEGO ", font=("Fixedsys", 17), border_width=8, button_color=('black', 'red'))]
                    ]
# adaptar logo y achicar botones
    window = sg.Window("Welcome!", layout_column, element_justification='center').finalize()

    window.Maximize()

    return window
