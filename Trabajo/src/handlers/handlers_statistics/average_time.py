import os
import pandas as pd
from matplotlib import pyplot as plt
from src.windows import layout_statistics as layout
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg


def percentage_by_nivel():

    def obtener_datos_usuario_time():
        archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..", "jugadas.csv")
        data_set = pd.read_csv(archivo)
        df = data_set

        # Calcular Promedio de tiempo de partidas finalizadas por nivel.
        # estado,nivel,Tiempo jugada
        # 1) filtramos el dataframe y nos quedamos con las inicios de partidas.
        df_inicio_partidas = df[df["Nombre de evento"] == "inicio_partida"].set_index("Partida")

        # 2) filtramos el dataframe y nos quedamos con los finales de partidas.
        df_fin_partidas = df[df["Nombre de evento"] == "fin"].set_index("Partida")

        # Hacemos el join de los inicios con los finales de partidas, con la propiedad lsuffix cambiamos
        # el nombre a las columnas para que no tengan el mismo nombre.
        df_partidas_inicio_fin = df_inicio_partidas.join(df_fin_partidas, lsuffix='_inicio', rsuffix='_fin')

        # Me quedo con las que tienen fecha de fin distinto de null(partidas inconclusas)
        df_partidas_inicio_fin_filtradas = df_partidas_inicio_fin[
            pd.notnull(df_partidas_inicio_fin["Tiempo jugada_fin"])]

        # Agregamos una columna calculada con la duración de la partida.
        df_partidas_inicio_fin_filtradas["duracion"] = df_partidas_inicio_fin_filtradas["Tiempo jugada_fin"] - \
                                                       df_partidas_inicio_fin_filtradas["Tiempo jugada_inicio"]

        # Filtramos las columnas que nos interesan 
        df_partidas_inicio_fin_filtradas.filter(
            items=['Partida', 'Tiempo jugada_inicio', 'Tiempo jugada_fin', 'duracion', 'nivel_inicio'])

        # Agrupa por nivel y promedia las duraciones
        df_partidas_inicio_fin_filtradas = df_partidas_inicio_fin_filtradas.groupby('nivel_inicio').mean()
        dibujo = df_partidas_inicio_fin_filtradas.filter(items=['nivel_inicio', 'duracion'])  
        plt.close()
        dibujo.plot(kind="bar", color="m")
        plt.show()
        plt.clf()

    obtener_datos_usuario_time()    
