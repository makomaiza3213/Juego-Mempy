from src.handlers.handlers_csv.general_functions_for_datasets import open_file


def club_filter():
    """
        Esta función abre el archivo csv de clubes, guarda la información en una estructura 
        auxiliar, cierra el archivo y retorna los barrios donde hay clubes con fútbol como una
        de sus actividades  y posee sede única.
    """
    list_file = open_file("clubes.csv")
    data = list(list_file[1])
    new_data = list(filter(lambda x: 'Fútbol' in x[11] and x[5] == 'UNICA', data))
    data = set(map(lambda data: data[16], new_data))
    list_file[0].close()
    return list(data)


def commune_filter():
    """
        Esta función abre el archivo csv clubes, guarda la información en una estructura 
        auxiliar, y retorna una lista con las comunas donde, la langitud del nombre del 
        barrio al cual pertenece es mayor a 9 y donde, el nom_mapa forme parte del nombre 
        de su facebook.
    """
    list_file = open_file("clubes.csv")
    data = list(list_file[1])
    new_data = list(filter(lambda x: len(x[16]) > 9 or x[4] in x[9], data))
    data = set(map(lambda data: data[17], new_data))
    list_file[0].close()
    return list(data)
