from itertools import groupby


from src.handlers.handlers_csv.general_functions_for_datasets import open_file


def product_brand_filter():
    """
    Función que ordena y filtra las 10 marca que tienen mas productos libres de gluten.
    """
    list_file = open_file("alimentos-libres-de-gluten.csv")
    x_sorted = sorted(list_file[1], key=lambda x: x[0].upper())
    x_grouped = [list(it) for k, it in groupby(x_sorted, key=lambda x: x[0].upper())]
    x_sorted2 = sorted(x_grouped, key=lambda x: len(x), reverse=True)
    x_sorted3 = x_sorted2[1:16]
    new = [i[0][0] for i in x_sorted3]
    list_file[0].close()
    return new


def filter_brand():
    """
        Función que filtra los productos de marca Fortuna y los gurda en un una lista
        de diccionarios.
    """
    list_file = open_file("alimentos-libres-de-gluten.csv")
    data = list(list_file[1])
    list_brand = filter(lambda x: x[0] == 'Fortuna', data)
    new = [{"marca": i[0]} for i in list_brand]
    print(new)
    list_file[0].close()
    return new
