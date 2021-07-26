import csv
import os
from src.handlers.handlers_csv.general_functions_for_datasets import open_file


def filter_cars_by_brand():
    """
        Esta función filtra las marcas de autos de tipo Sedan donde su tamaño sea mayor o 
        igual 1,80 mts y su MSRP sea mayor o igual a $30,000 y menor igual a $40,000
    """
    list_file = open_file("cards.csv")
    data = list(list_file[1])
    new_data = list(filter(lambda x: x[2] == "Sedan" and x[14] >= '180' and '$30,000' <= x[6] <= '$40,000', data))
    list_file[0].close()
    return list(set(map(lambda marca: marca[0], new_data)))


def car_filter_by_price():
    """
        Esta función abre el archivo csv cards, guarda la información en una estructura
        auxiliar, cierra el archivo y retorna una lista con las marcas de autos.
    """
    list_file = open_file("cards.csv")
    data = list(list_file[1])

    data_price = list(map(lambda num: float(num[6].replace('$', '').replace(',', '')), data))
    promedio = sum(data_price) / len(data_price)
    new_data = list(
        filter(lambda x: float(x[6].replace('$', '').replace(',', '')) < promedio and x[3] == 'Europe' or x[3] == 'USA',
               data))
    list_file[0].close()
    return list(set(map(lambda origen: origen[0], new_data)))
