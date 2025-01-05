"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd 
archivo = "files/input/tbl0.tsv"
file = pd.read_csv(archivo, sep='\t')

agrupados = file.groupby("c1")["c2"]
sumas = agrupados.sum()


def pregunta_07():
    return sumas