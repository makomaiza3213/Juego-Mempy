import operator
from src.handlers.handlers_csv.general_functions_for_datasets import open_file


def max_sort(peces):
    """
        recibe una lista con nombre y cantidad de todos los peces y retorna otra lista unicamente con los nombres de los
        peces
    """
    items = peces.items()
    peces_max = sorted(peces.items(), key=operator.itemgetter(1), reverse=True)
    maximos = []
    for i in range(0, 15):
        maximos.append(peces_max[i])
    nom_max = [pez[0] for pez in maximos]
    return nom_max


def calcula_max():
    """
        leo el csv de peces guardando el nombre y la cantidad total de todos los peces,
        para luego ordenarlos de mayor a menor y retornar una lista con los nombres
    """
    list_file = open_file("captura-puerto-flota-2019.csv")
    peces = {}
    for linea in list_file[1]:
        if linea[10] in peces:
            peces[linea[10]] += int(linea[12])
        else:
            peces[linea[10]] = int(linea[12])
    max = max_sort(peces)
    list_file[0].close()
    return max


def peces_Rawson_Chubut(puerto, prov):
    """
        abro y leo el csv de peces tomando aquellos peces que han sido pescados
        en el puerto Rawson en la provincia de Chubut
    """
    list_file = open_file("captura-puerto-flota-2019.csv")
    peces = list(filter(lambda x: (x[2] == puerto and x[3] == prov or x[3] == 'Buenos Aires'), list_file[1]))
    list_file[0].close()
    return list(set(map(lambda pez: pez[10], peces)))


def peces_costeros(flota, puerto):
    """
        abro y leo el csv de peces tomando aquellos peces que han sido
        pescados en diferentes puertos de Bs As que sean costeros
    """
    list_file = open_file("captura-puerto-flota-2019.csv")
    peces = list(filter(lambda x: (x[1] == flota and x[2] == puerto), list_file[1]))
    list_file[0].close()
    return list(set(map(lambda pez: pez[10], peces)))


def peces_Mardel_BsAs_GralPy(fecha, puerto, prov, depar):
    """
        abro y leo el csv de peces tomando aquellos peces que han sido pescados
        el 2019-11 en Mar del Plata en el puerto del Gral Pueyrredon
    """
    list_file = open_file("captura-puerto-flota-2019.csv")
    peces = list(filter(lambda x: (x[0] == fecha and x[2] == puerto and x[3] == prov and x[5] == depar), list_file[1]))
    list_file[0].close()
    return list(set(map(lambda pez: pez[10], peces)))
