import os
import pandas as pd
from src.windows import layout_statistics as layout
from matplotlib import pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def state():
    def graficar(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    def obtener_datos():
        archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..", "jugadas.csv")
        data_set = pd.read_csv(archivo)
        df = data_set

        # Gráfico que muestre el porcentaje de partidas por estado (terminada, cancelada,
        # abandonadas).
        partidas_por_estado_finaliz = df[df['Estado'] == 'finalizada']

        partidas_estado_cancel_abandonada = df[df['Estado'] == 'partida abandonada']

        partidas_estado_timeout = df[df['Estado'] == 'timeout']

        total_finalizadas_abandonadas = len(partidas_por_estado_finaliz) + len(partidas_estado_cancel_abandonada) + len(
            partidas_estado_timeout)

        etiquetas = ["Finalizadas", "Abandonadas", "Timeout"]
        cantidad_finalizadas = len(partidas_por_estado_finaliz)
        cantidad_abandonadas = len(partidas_estado_cancel_abandonada)
        cantidad_timeout = len(partidas_estado_timeout)
        data_dibujo = [cantidad_finalizadas, cantidad_abandonadas, cantidad_timeout]

        return etiquetas, data_dibujo

    window, fig = layout.layout_porc_genero()

    etiquetas, data_dibujo = obtener_datos()

    explode = (0.1, 0)
    plt.pie(data_dibujo, labels=etiquetas, autopct='%1.1f%%',
            shadow=False, startangle=90, labeldistance=2.1)
    plt.axis('equal')
    plt.legend(etiquetas)
    plt.title("Porcentaje de partidas por estado")

    graficar(window['figCanvas'].TKCanvas, fig)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Salir':
            plt.clf()
            plt.close()
            break
    window.close()
