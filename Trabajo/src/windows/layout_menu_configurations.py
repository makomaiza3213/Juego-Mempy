import PySimpleGUI as sg

from src.handlers.images import open_image


def menu_configurations(player):
    """
        diseño de la ventana de configuraciones 
    """
    sg.theme('DarkAmber')
    logo = open_image("logo.png")
    frame_layout = [
                    [sg.Text("", size=(0, 1))],
                    [sg.Text('Victoria', size=(21, 1), justification="center", font=('Fixedsys', 20)),
                     sg.InputText(player.msj_victoria, size=(35, 1), key='-MSJVIC-', font=('Fixedsys', 20))],
                    [sg.Text('Derrota', size=(21, 1), justification="center", font=('Fixedsys', 20)),
                     sg.InputText(player.msj_derrota, size=(35, 1), key='-MSJDER-', font=('Fixedsys', 20))],
                    [sg.Text('Tiempo Restante', size=(21, 1), justification="center", font=('Fixedsys', 20)),
                     sg.InputText(player.msj_tiempo, size=(35, 1), key='-MSJRES-', font=('Fixedsys', 20))]]

    frame_level = [
                   [sg.InputCombo([4, 5], default_value=player.nivel["dimensiones"]["x"], font=('Fixedsys', 18), key='-DIM1-'), sg.Text('x'), sg.InputCombo([4, 6], default_value=player.nivel["dimensiones"]["y"], font=('Fixedsys', 18), key='-DIM2-')],
                   [sg.Text('Coincidencias ', font=('Fixedsys', 18)), sg.InputCombo([2, 3], default_value=player.nivel["coincidencias"], font=('Fixedsys', 18), key='-COINCID-')],
                   [sg.Text('Tiempo Partida', font=('Fixedsys', 18)), sg.Combo([1, 2, 3], default_value=player.nivel["tiempo_juego"], font=('Fixedsys', 18), key='-TIME-')],
                   ]

    current_level = player.nivel_actual

    layout = [
        [sg.Radio('Nivel 1', "RADIO1", default=current_level == "1", enable_events=False, font=('Fixedsys', 20), key='-LV1-'),
         sg.Radio('Nivel 2', "RADIO1", default=current_level == "2", enable_events=True, font=('Fixedsys', 20), key='-LV2-'),
         sg.Radio('Nivel 3', "RADIO1", default=current_level == "3", enable_events=True, font=('Fixedsys', 20), key='-LV3-'),
         sg.Radio('Nivel 4', "RADIO1", default=current_level == "4", enable_events=True, font=('Fixedsys', 20), key='-LV4-')],
        [sg.Frame('Configurar nivel 4', frame_level, border_width=2, element_justification="center", font=('Fixedsys', 25))],
        [sg.Frame('Configure sus mensajes', frame_layout, border_width=2, font=('Fixedsys', 25))],
        [sg.Text("", size=(0, 1))],
        [sg.Text('Seleccione un tema', font=('Fixedsys', 20)),
         sg.InputCombo(['Black', 'TealMono', 'Topanga', 'DarkGreen1'], player.tema, size=(11, 1),
                       font=('Fixedsys', 18), key='-TEMA-')],
        [sg.Text("", size=(0, 1))],
        [sg.Button('Guardar', key="-GUARDAR-", font=('Fixedsys', 20)), sg.Button('volver', font=('Fixedsys', 20), key='-VOLVER-')]]

    layout_window = [
        [sg.Text("", size=(0, 2))],
        [sg.Button(image_filename=logo, border_width=10)],
        [sg.Text("", size=(0, 2))],
        [sg.Frame('Selecciona tu nivel', layout, font=('Fixedsys', 30), border_width=2, element_justification='center')]]
    window = sg.Window('Configuración', layout_window, element_justification='center').Finalize()

    window.Maximize()

    return window
