def filtro(lista, x, y):
    """
        Agrega a una nueva lista la cantidad de elementos necesarios para completar el tablero
    """
    n = int((x * y) / 2)
    nue_lista = []
    for i in range(n):
        nue_lista.append(lista[i])
    return nue_lista


def claves(lista, cuad):
    """
        Le asigna una elemento a cada boton del tablero
    """
    i = 0  # indice de la lista
    dic = {'-F-': lista[i]}
    for z in range(cuad - 1):  # cuad = filas * columas
        i = i + 1
        dic['-F-' + str(z)] = lista[i]
        if i == (len(lista) - 1):
            i = -1
    return dic
