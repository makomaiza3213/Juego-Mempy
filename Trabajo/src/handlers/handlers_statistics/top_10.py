import os
import pandas as pd
from src.windows.layout_statistics import layout_top_10
from src.handlers import sounds 


def obtener_datos():

    archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..", "jugadas.csv")
    data_set = pd.read_csv(archivo)
    df = data_set

    top10 = (((df[df['Estado'] == 'Ok'].assign(rn=df[df['Estado'] == 'Ok'].sort_values(["Tiempo jugada"], ascending=True).groupby(["Partida"]).cumcount()+ 1)).query("rn == 1")).groupby(['Palabra']).size().to_frame('size'))
    top10.sort_values('size', ascending=False).head(10)
    top10_serie = top10.squeeze()

    window = layout_top_10(list(top10_serie.index.values))
    event, values = window.read()
    if event == "Salir":
        sounds.play_sound("click.wav")
        window.close()
  
    
     

