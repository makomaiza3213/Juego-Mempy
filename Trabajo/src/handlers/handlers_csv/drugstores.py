from src.handlers.handlers_csv.general_functions_for_datasets import open_file


def provincia():
    """
       Devuelve una lista de las dorgerias que se encuentran en la provincia de BUENOS AIRES     
    """
    list_file = open_file("establecimientos-droguerias-redro-enero-2021.csv")
    prov = "BUENOS AIRES"
    lista = list(filter(lambda x: (x[5] == prov), list_file[1]))
    list_file[0].close()
    return list(set(map(lambda nom: nom[1], lista)))


def privadas_y_web():
    """
        Devuelve una lista de las Droguerias que sean privadas y tengan paginas web
    """
    list_file = open_file("establecimientos-droguerias-redro-enero-2021.csv")
    estado = "Privado"
    lista = list(filter(lambda x: (x[10] == estado and x[16] != ""), list_file[1]))
    list_file[0].close()
    return list(set(map(lambda nom: nom[1], lista)))
