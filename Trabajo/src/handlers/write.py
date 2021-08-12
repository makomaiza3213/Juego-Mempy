import time
import csv
import os


def increase_number_game(filename, play_data):
    """
        apertura del csv de registro de jugadas y la correcta actualización de la lista que contiene los datos
        a escribir en el csv, toma de la ultima partida el numero de partida e incrementa en uno en la lista(play_data)
        dicho valor
    """
    with open(filename)as file:
        datos = csv.reader(file)
        list_datos = list(datos)
        play_data[0] = int(list_datos[len(list_datos) - 1][1]) + play_data[0]
        file_plays = file
    return file_plays


def create_csv(play_data):
    """
        consulta por la existencia del csv de jugadas ,
        en caso de estar creado:     actualiza los datos de la lista para su posterior escritura
        en caso contrario :     crea el encabezado y el archivo csv para su posterior escritura
    """
    if os.path.exists("jugadas.csv"):
        file_plays = increase_number_game("jugadas.csv", play_data)
    else:
        fields = ["Tiempo jugada", "Partida", "Cantidad total de palabras a adivinar", "Nombre de evento",
                  "Usuario-nick",
                  "usuario-genero", "usuario-edad", "Estado", "Palabra", "nivel", "puntaje"]
        filename = "jugadas.csv"
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvfile.close()
    return file_plays


def write_csv(evento, play_data, file_plays, estado="", palabra="", puntaje=""):
    """
        por medio de consultas de tiempo y valores recibidos por parametros actualiza los datos de
        la lista que corresponde a una fila del archivo csv, abre el archivo y escribe los datos
    """
    tiempo = time.time()

    if evento == "inicio_partida":
        rows = [str(tiempo), play_data[0], play_data[1], evento, play_data[2], play_data[3], play_data[4],
                estado, palabra, play_data[5], puntaje]
    else:
        if (evento == "intento_Error") or (evento == "intento_Ok"):
            if evento == "intento_Error":
                estado = "Error"
            else:
                estado = "Ok"
            rows = [str(tiempo), play_data[0], play_data[1], "intento", play_data[2], play_data[3], play_data[4],
                    estado, palabra, play_data[5], puntaje]
        else:
            if evento == "fin":
                rows = [str(tiempo), play_data[0], play_data[1], evento, play_data[2], play_data[3], play_data[4],
                        estado, palabra,
                        play_data[5], puntaje]

    if file_plays.closed:
        file_plays = open("jugadas.csv", "a", newline='')
        csvwriter = csv.writer(file_plays)
        csvwriter.writerow(rows)
    else:
        csvwriter = csv.writer(file_plays)
        csvwriter.writerow(rows)

    """with open("jugadas.csv", "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(rows)
        csvfile.close()
    """
    return file_plays
