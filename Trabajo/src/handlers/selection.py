import datetime
from src.handlers import criteria


def values_hour_day():
    """
        tomando dia y hora actuales invoca a una funcion correspondiente a dichos valores y retorna los valores de dicho criterio
    """
    nro_dia = datetime.datetime.today().weekday()
    tiempo = datetime.datetime.now()

    if 0 < tiempo.hour < 12:
        turno = "mañana"
    else:
        turno = "tarde"
    lista = criteria.seleccion(nro_dia, turno)
    return lista
