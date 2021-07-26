import PySimpleGUI as sg


def menu_configurations(player):
    """
        diseño de la ventana de configuraciones 
    """
    sg.theme('DarkAmber')
    frame_layout = [[sg.Text('mensaje de "victoria"', size=(21, 2), font='Any 12'),
                     sg.InputText(player.msj_victoria, key='-MSJVIC-')],
                    [sg.Text('mensaje de "derrota"', size=(21, 2), font='Any 12'),
                     sg.InputText(player.msj_derrota, key='-MSJDER-')],
                    [sg.Text('mensaje de "tiempo restante"', size=(21, 2), font='Any 12'),
                     sg.InputText(player.msj_tiempo, key='-MSJRES-')]]

    frame_level = [[sg.InputCombo([4, 5], default_value=player.nivel["dimensiones"]["x"], key='-DIM1-'), sg.Text('x'),sg.InputCombo([4, 6], default_value=player.nivel["dimensiones"]["y"],key='-DIM2-')],
                   [sg.Text('Coincidencias ', font='Any 12'), sg.InputCombo([2, 3], default_value=player.nivel["coincidencias"], key='-COINCID-')],
                   [sg.Text('Tiempo Partida', font='Any 12'), sg.Combo([1, 2, 3], default_value=player.nivel["tiempo_juego"], key='-TIME-')],
                   ]

    current_level = player.nivel_actual

    layout = [
        [sg.Radio('Nivel 1', "RADIO1", default=current_level == "1", enable_events=False, font='Any 12', key='-LV1-'),
         sg.Radio('Nivel 2', "RADIO1", default=current_level == "2", enable_events=True, font='Any 12', key='-LV2-'),
         sg.Radio('Nivel 3', "RADIO1", default=current_level == "3", enable_events=True, font='Any 12', key='-LV3-'),
         sg.Radio('Nivel 4', "RADIO1", default=current_level == "4", enable_events=True, font='Any 12', key='-LV4-')],
        [sg.Frame('Configurar nivel 4', frame_level, element_justification="center", font='Any 15', title_color='white')],
        [sg.Frame('Configure sus mensajes', frame_layout, font='Any 15', title_color='white')],
        [sg.Text('Seleccione un tema', font='Any 15'),
         sg.InputCombo(['Black', 'TealMono', 'Topanga', 'DarkGreen1'], player.tema, size=(11, 1),
                       key='-TEMA-')],
        [sg.Button('Guardar', key="-GUARDAR-", font='Any 12'), sg.Button('volver', font='Any 12', key='-VOLVER-')]]

    layout_window = [
        [sg.Frame('Selecciona tu nivel', layout, font='Any 15', title_color='white', element_justification='center')]]
    window = sg.Window('Configuración', layout_window, element_justification='center').Finalize()
    return window
