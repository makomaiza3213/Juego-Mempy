from src.handlers.handlers_csv.general_functions_for_datasets import open_file


def pag_web_y_gmail():
    """
      Devuelve una lista de las Iglesias que tengan pagina web , correo electronico o nemro telefonico mejor dicho que tengan metodos de comunicaion
    """
    list_file = open_file("iglesias.csv")
    lista = list(filter(lambda x: (x[6] != "" or x[7] != "" or x[8] != ""), list_file[1]))
    list_file[0].close()
    return list(map(lambda nom: nom[2], lista))


def cumple(cadena):
    ok = False
    if cadena != "":
        lista2 = list(cadena)
        cant = len(lista2)
        num = int(lista2[cant - 1])
        if num % 2 != 0:
            ok = True
    return ok


def comunas():
    """
       Devuelve un listado de las Iglesias que tengan comuna impar
    """
    list_file = open_file("iglesias.csv")
    lista = []
    for linea in list_file[1]:
        cadena = linea[10]
        if cumple(cadena):
            lista.append(linea[2])
    list_file[0].close()
    return lista
