import os
import pandas as pd
from src.windows.layout_statistics import layout_top_10
from src.handlers import sounds 


def obtener_datos():

    archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..", "jugadas.csv")
    data_set = pd.read_csv(archivo)

    #df_filtrado_ok=df[df['Estado'] == 'Ok']
    # a todos los estados = ok los ordeno por "Tiempo de jugada" en forma ascendente (de menor a mayor) con la funcion sort_values()
    # sort_values(["Tiempo jugada"]) recibe la columna por la que quiero ordenar con ascending= True en forma ascendente.   
    #df_filtrado_ok_ordenado_por_tiempo=df_filtrado_ok.sort_values(["Tiempo jugada"], ascending=True)    

    # A los "Estado" = ok ordenados por fecha los agrupo por "Partida" y numero en cada grupo desde 1 (por eso el +1) hasta la longitud del grupo.
    # DataFrameGroupBy.cumcount(ascending=True)= Numera cada elemento en cada grupo desde 0 hasta la longitud de ese grupo - 1.
    #df_filtrado_ok_ordenado_por_tiempo_agrupado_por_partida = df_filtrado_ok_ordenado_por_tiempo.groupby(["Partida"]).cumcount()+ 1

    # DataFrame.assign(**kwargs) = Asignar nuevas columnas a un DataFrame.Devuelve un nuevo objeto con todas las columnas originales
    # además de las nuevas. Las columnas existentes que se reasignan se sobrescribirán. 
    # Asigno al dataframe la columna rn que tinen la nuemeracion de cada uno de los grupos.
    #df_filtrado_ok.assign(rn=df_filtrado_ok_ordenado_por_tiempo_agrupado_por_partida)

    # DataFrame.query = Consulta las columnas de un DataFrame con una expresión booleana.("rn == 1") primeras columnas ok
    # De la columna asignada anteriormente me quedo con las número = 1 de cada grupo 
    #df_filtrado_ok_ordenado_por_tiempo_agrupado_por_partida_rn_1 = df_filtrado_ok.assign(rn=df_filtrado_ok_ordenado_por_tiempo_agrupado_por_partida).query("rn == 1")

    # Los que son 0k ordenados por tiempo agrupado por partida que en rn = 1 (primer ok de partida)y las agrupo por "Palabra" 
    # y con size() cuento cuantas hay luego con to_frame('size') covierto la serie obtenida en un dataframe,
    # size(Devuelve el número de elementos de los datos subyacentes.) ???
    # es una serie con to_frame lo convierto en dataframe
    #df_filtrado_ok_ordenado_por_tiempo_agrupado_por_partida_rn_1_agrupdo_por_palabra = df_filtrado_ok_ordenado_por_tiempo_agrupado_por_partida_rn_1.groupby(['Palabra']).size().to_frame('size')

    # Ordeno los datos del dataframe con sort_values  en forma descendente  la columna size. ('size')
    #y con head() tomo los 10 primeros.Esta función devuelve las primeras n filas del objeto n = numero de filas
    #df_filtrado_ok_ordenado_por_tiempo_agrupado_por_partida_rn_1_agrupdo_por_palabra.sort_values('size', ascending=False).head(10)  

    df = data_set
    top10 = (((df[df['Estado'] == 'Ok'].assign(rn=df[df['Estado'] == 'Ok'].sort_values(["Tiempo jugada"], ascending=True).groupby(["Partida"]).cumcount()+ 1)).query("rn == 1")).groupby(['Palabra']).size().to_frame('size'))
    top10.sort_values('size', ascending=False).head(10)
    top10_serie = top10.squeeze()

    window = layout_top_10(list(top10_serie.index.values))
    event, values = window.read()
    if event == "Salir":
        sounds.play_sound("click.wav")
        window.close()
  
    
     

