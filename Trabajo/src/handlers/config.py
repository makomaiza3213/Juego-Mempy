import json


def save_config(player, values):
    """
        Setea la configuracion de un jugador con la que haya elegido 
    """
    with open("usuarios.json", "r") as json_file:
        data = json.load(json_file)
        i = 0
        ok = False
        while i <= len(data['usuarios']) and (not ok):
            if data['usuarios'][i]['nombre'] == player.nick:
                if values['-LV1-']:
                    lv = 1
                    player.nivel['dimensiones']['x'] = data['usuarios'][i]['configuracion']["level1"]['dimensiones']['x']
                    player.nivel['dimensiones']['y'] = data['usuarios'][i]['configuracion']["level1"]['dimensiones']['y']
                    player.nivel['coincidencias'] = data['usuarios'][i]['configuracion']["level1"]['coincidencias']
                    player.nivel['tiempo_juego'] = data['usuarios'][i]['configuracion']["level1"]['tiempo_juego']
                elif values['-LV2-']:
                    lv = 2
                    player.nivel['dimensiones']['x'] = data['usuarios'][i]['configuracion']["level2"]['dimensiones']['x']
                    player.nivel['dimensiones']['y'] = data['usuarios'][i]['configuracion']["level2"]['dimensiones']['y']
                    player.nivel['coincidencias'] = data['usuarios'][i]['configuracion']["level2"]['coincidencias']
                    player.nivel['tiempo_juego'] = data['usuarios'][i]['configuracion']["level2"]['tiempo_juego']
                elif values['-LV3-']:
                    lv = 3
                    player.nivel['dimensiones']['x'] = data['usuarios'][i]['configuracion']["level3"]['dimensiones']['x']
                    player.nivel['dimensiones']['y'] = data['usuarios'][i]['configuracion']["level3"]['dimensiones']['y']
                    player.nivel['coincidencias'] = data['usuarios'][i]['configuracion']["level3"]['coincidencias']
                    player.nivel['tiempo_juego'] = data['usuarios'][i]['configuracion']["level3"]['tiempo_juego']
                else:
                    lv = 4
                    player.nivel['dimensiones']['x'] = values['-DIM1-']
                    player.nivel['dimensiones']['y'] = values['-DIM2-']
                    player.nivel['coincidencias'] = values['-COINCID-']
                    player.nivel['tiempo_juego'] = values['-TIME-']

                level = "level" + str(lv)

                player.nivel_actual = lv
                player.msj_victoria = values['-MSJVIC-']
                player.msj_derrota = values['-MSJDER-']
                player.msj_tiempo = values['-MSJRES-']
                player.tema = values['-TEMA-']


                # data['usuarios'][i]['configuracion'][level]['dimensiones']['x'] = player.nivel['dimensiones']['x']
                # data['usuarios'][i]['configuracion'][level]['dimensiones']['y'] = player.nivel['dimensiones']['y']

                data['usuarios'][i]['configuracion'][level]['dimensiones']['x'] = player.nivel['dimensiones']['x']
                data['usuarios'][i]['configuracion'][level]['dimensiones']['y'] = player.nivel['dimensiones']['y']
                data['usuarios'][i]['configuracion'][level]['coincidencias'] = player.nivel['coincidencias']
                data['usuarios'][i]['configuracion'][level]['tiempo_juego'] = player.nivel['tiempo_juego']
                data['usuarios'][i]['configuracion']['nivel_actual'] = player.nivel_actual
                data['usuarios'][i]['configuracion']['msj_victoria'] = player.msj_victoria
                data['usuarios'][i]['configuracion']['msj_derrota'] = player.msj_derrota
                data['usuarios'][i]['configuracion']['msj_tiempo'] = player.msj_tiempo
                data['usuarios'][i]['configuracion']['tema'] = player.tema

                ok = True
            else:
                i = i + 1
        with open("usuarios.json", "w") as file:
            json.dump(data, file, indent=4)


def verify(val):
    """
        Verifica que la configuracion que haya elegido el jugador cumpla con los valores establecidos para el nivel 4
    """
    ok = False

    list_themes = ['Black', 'TealMono', 'Topanga', 'DarkGreen1']
    if val['-TEMA-'] in list_themes:
        if int(val['-DIM1-']) in range(4, 6):
            if int(val['-DIM2-']) in range(4, 7):
                if int(val['-COINCID-']) in range(2, 4):
                    if val['-COINCID-'] == 3:
                        if (val['-DIM1-'] * val['-DIM2-']) % 3 == 0:
                            ok = val
                    else:
                        if (val['-DIM1-'] * val['-DIM2-']) % 2 == 0:
                            ok = val
    return ok


def verify_123(val):
    """
        verifica si el tema que haya in
    """
    ok = False
    list_themes = ['Black', 'TealMono', 'Topanga', 'DarkGreen1']
    if val['-TEMA-'] in list_themes:
        return True
    return ok
