import os
import csv


def open_file(dataset):
    if "captura-puerto-flota-2019.csv" in dataset:
        archivo = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", "datasets", dataset),
                       encoding=None)
        csvreader = csv.reader(archivo, delimiter=',')
        next(csvreader)
        return [archivo, csvreader]
    else:
        archivo = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", "datasets", dataset),
                       encoding="UTF8")
        csvreader = csv.reader(archivo, delimiter=',')
        next(csvreader)
        return [archivo, csvreader]
