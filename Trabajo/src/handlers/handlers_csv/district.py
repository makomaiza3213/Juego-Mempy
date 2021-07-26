from src.handlers.handlers_csv.general_functions_for_datasets import open_file


def barrios_con_atencion(con, com1, com2, com3):
    """
        abro y leo el csv de barrios y retorno aquellos que tengan atencion y pertenezcan a las comunas 9,10 y 12
    """
    list_file = open_file("puntos-verdes.csv")
    barrios = list(filter(lambda x: (x[7] == con or x[13] == com1 or x[13] == com2 or x[13] == com3), list_file[1]))
    list_file[0].close()
    return list(set(map(lambda bar: bar[12], barrios)))


def barrios_cooperativa(con, coop1, coop2):
    """
        abro y leo el csv de barrios y retorno aquellos que tengan atencion y pertenezcan a las cooperativas:
        Coop. Trabajo de Recuperadores Urbanos del Oeste, Coop. de Provisión de Servicios para Recolectores del Oeste
    """
    list_file = open_file("puntos-verdes.csv")
    barrios = list(filter(lambda x: (x[7] == con or x[8] == coop1 or x[8] == coop2), list_file[1]))
    list_file[0].close()
    return list(set(map(lambda bar: bar[12], barrios)))
