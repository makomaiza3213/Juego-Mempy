import os
import pandas as pd
from src.windows import layout_statistics as layout
from matplotlib import pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def percentage_by_gender():
    def graficar(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    def obtener_datos_usuario_genero():
        archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..", "jugadas.csv")
        data_set = pd.read_csv(archivo)
        df = data_set

        # De toda las partidas finalizadas que porcentaje representa según genero:
        # primero filtrar por "Nombre evento" == fin despues filtar los que son masculino , otros, femenino.
        partidas_finalizadas = df[df['Estado'] == 'finalizada']

        usuario_genero_femenino = partidas_finalizadas[partidas_finalizadas["usuario-genero"] == "femenino"]

        usuario_genero_masculino = partidas_finalizadas[partidas_finalizadas["usuario-genero"] == "masculino"]

        usuario_otros_generos = partidas_finalizadas[partidas_finalizadas["usuario-genero"] == "otros"]

        etiquetas = ["Masculino", "Otros", "Femenino"]
        cantidad_masculino = len(usuario_genero_masculino)
        cantidad_otros = len(usuario_otros_generos)
        cantidad_femenino = len(usuario_genero_femenino)
        data_dibujo = [cantidad_masculino, cantidad_otros, cantidad_femenino]

        return etiquetas, data_dibujo

    window, fig = layout.layout_porc_genero()

    etiquetas, data_dibujo = obtener_datos_usuario_genero()

    explode = (0.1, 0)

    plt.pie(data_dibujo, labels=etiquetas, autopct='%1.1f%%',
            shadow=False, startangle=90, labeldistance=2.1)
    plt.axis('equal')
    plt.legend(etiquetas)
    plt.title("Porcentaje de partidas finalizadas por género")

    graficar(window['figCanvas'].TKCanvas, fig)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Salir':
            plt.clf()
            plt.close()
            break
    window.close()
