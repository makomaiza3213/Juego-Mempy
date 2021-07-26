from src.handlers.handlers_csv import drugstores, clubs, fishes, cards, churches, products, district
from src.handlers import images


def seleccion(dia, turno):
    """
        definicion de los criterios segun el dia y el rango horario, invoca la funcion correspondiente ,
        valga la redundancia, y retorna una lista con las palabras a usar en el tablero
    """
    criterios_data = {
        0: {"mañana": {"criterios": "los 10 peces más pescados ", "funcion": fishes.calcula_max, "parametros": ()},
            "tarde": {"criterios": "los peces pescados en la fecha indicada en Mardel en la prov de Bs As,Gral Py",
                      "funcion": fishes.peces_Mardel_BsAs_GralPy,
                      "parametros": ("2019-11", "Mar del Plata", "Buenos Aires", "General Pueyrredon")}
            },
        1: {"mañana": {"criterios": "Iglesias con pagina web o correo electronico o numero telefonico ",
                       "funcion": churches.pag_web_y_gmail, "parametros": ()},
            "tarde": {"criterios": "Iglesias con comuna impar", "funcion": churches.comunas, "parametros": ()}
            },
        2: {"mañana": {"criterios": "Las 15 marca que tienen mas productos libres de gluten",
                       "funcion": products.product_brand_filter, "parametros": ()},
            "tarde": {"criterios": "Las 15 marcas de autos de Europe , USA, con precio por debajo de el promedio",
                      "funcion": cards.car_filter_by_price, "parametros": ()}
            },
        3: {"mañana": {"criterios": 'Peces pescados en el Puerto Rawson en la provincia de Chubut',
                       "funcion": fishes.peces_Rawson_Chubut, "parametros": ("Rawson", "Chubut")},
            "tarde": {"criterios": "Peces costeros pescados en Otros puertos de Bs As",
                      "funcion": fishes.peces_costeros, "parametros": ("Costeros", "otros puertos Buenos Aires")}
            },
        4: {"mañana": {"criterios": "los barrios con atencion en cooperativas indicadas ",
                       "funcion": district.barrios_cooperativa, "parametros": (
                        "Punto Verde Con Atención", "Cooperativa de Trabajo de Recuperadores Urbanos del Oeste",
                        "Cooperativa de Provisión de Servicios para Recolectores del Oeste")},
            "tarde": {"criterios": "los barrios con atencion pertenecientes a cualquiera de las 3 comunas indicadas",
                      "funcion": district.barrios_con_atencion,
                      "parametros": ("Punto Verde Con Atención", "COMUNA 10", "COMUNA 12", "COMUNA 9")}
            },
        5: {"mañana": {"criterios": "Droguerias de Buenos Aires", "funcion": drugstores.provincia, "parametros": ()},
            "tarde": {"criterios": "Droguerias que sean privadas y tengan paginas web",
                      "funcion": drugstores.privadas_y_web, "parametros": ()}
            },
        6: {"mañana": {"criterios": "Las 15  marcas de autos Sedan según su longitud y valor",
                       "funcion": cards.filter_cars_by_brand, "parametros": ()},
            "tarde": {"criterios": "Los 15 barrios donde hay clubes con fútbol y sede única",
                      "funcion": clubs.club_filter, "parametros": ()}
            }
    }

    fun_param = criterios_data[dia][turno]
    lista = fun_param['funcion'](*fun_param['parametros'])

    return lista
