import datetime
from src.handlers import criteria


def values_hour_day():
    """
        Tomando el día y la hora actuales, invoca a la función correspondiente a dichos valores
        y retorna los valores correspondientes

    Returns
            lista con las palabras correspondientes al dia y la hora
    """
    nro_dia = datetime.datetime.today().weekday()
    tiempo = datetime.datetime.now()

    if 0 < tiempo.hour < 12:
        turno = "mañana"
    else:
        turno = "tarde"
    lista = criteria.seleccion(nro_dia, turno)
    return lista
