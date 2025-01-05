"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd 
archivo = "files/input/tbl2.tsv"
file = pd.read_csv(archivo, sep='\t')

archivo2 = "files/input/tbl0.tsv"
file2 = pd.read_csv(archivo2, sep='\t')

resultado = pd.merge(file, file2, on="c0")
resultado = resultado.groupby("c1")["c5b"]
resultado = resultado.sum()


def pregunta_13():
    return resultado
