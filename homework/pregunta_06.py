"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
archivo = "files/input/tbl1.tsv"
file = pd.read_csv(archivo, sep='\t')
fila = file["c4"]
unicos  = fila.unique().tolist()
unicos = [x.upper() for x in unicos]
unicos = (sorted(unicos))

def pregunta_06():
    return unicos
