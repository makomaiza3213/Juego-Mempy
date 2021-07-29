import PySimpleGUI as sg


def menu_configurations(player):
    """
        diseño de la ventana de configuraciones 
    """
    sg.theme('DarkAmber')
    frame_layout = [[sg.Text('mensaje de "victoria"', size=(21, 2), font=('Fixedsys', 12)),
                     sg.InputText(player.msj_victoria, key='-MSJVIC-', font='Fixedsys')],
                    [sg.Text('mensaje de "derrota"', size=(21, 2), font=('Fixedsys', 12)),
                     sg.InputText(player.msj_derrota, key='-MSJDER-', font='Fixedsys')],
                    [sg.Text('mensaje de "tiempo restante"', size=(21, 2), font=('Fixedsys', 12)),
                     sg.InputText(player.msj_tiempo, key='-MSJRES-', font='Fixedsys')]]

    frame_level = [[sg.InputCombo([4, 5], default_value=player.nivel["dimensiones"]["x"], font='Fixedsys', key='-DIM1-'), sg.Text('x'), sg.InputCombo([4, 6], default_value=player.nivel["dimensiones"]["y"], font='Fixedsys', key='-DIM2-')],
                   [sg.Text('Coincidencias ', font=('Fixedsys', 12)), sg.InputCombo([2, 3], default_value=player.nivel["coincidencias"], font='Fixedsys', key='-COINCID-')],
                   [sg.Text('Tiempo Partida', font=('Fixedsys', 12)), sg.Combo([1, 2, 3], default_value=player.nivel["tiempo_juego"], font='Fixedsys', key='-TIME-')],
                   ]

    current_level = player.nivel_actual

    layout = [
        [sg.Radio('Nivel 1', "RADIO1", default=current_level == "1", enable_events=False, font=('Fixedsys', 12), key='-LV1-'),
         sg.Radio('Nivel 2', "RADIO1", default=current_level == "2", enable_events=True, font=('Fixedsys', 12), key='-LV2-'),
         sg.Radio('Nivel 3', "RADIO1", default=current_level == "3", enable_events=True, font=('Fixedsys', 12), key='-LV3-'),
         sg.Radio('Nivel 4', "RADIO1", default=current_level == "4", enable_events=True, font=('Fixedsys', 12), key='-LV4-')],
        [sg.Frame('Configurar nivel 4', frame_level, border_width=6, element_justification="center", font=('Fixedsys', 15))],
        [sg.Frame('Configure sus mensajes', frame_layout, border_width=6, font=('Fixedsys', 15))],
        [sg.Text('Seleccione un tema', font=('Fixedsys', 15)),
         sg.InputCombo(['Black', 'TealMono', 'Topanga', 'DarkGreen1'], player.tema, size=(11, 1),
                       font='Fixedsys', key='-TEMA-')],
        [sg.Button('Guardar', key="-GUARDAR-", font=('Fixedsys', 12)), sg.Button('volver', font=('Fixedsys', 12), key='-VOLVER-')]]

    layout_window = [
        [sg.Frame('Selecciona tu nivel', layout, font=('Fixedsys', 15), border_width=12, element_justification='center')]]
    window = sg.Window('Configuración', layout_window, element_justification='center').Finalize()
    return window
