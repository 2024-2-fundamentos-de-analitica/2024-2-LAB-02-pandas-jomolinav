"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd 
archivo = "files/input/tbl2.tsv"
file = pd.read_csv(archivo, sep='\t')


file['c5'] = file['c5a'] + ':' + file['c5b'].astype(str)

resultado = file.groupby('c0')['c5'].apply(lambda x: ','.join(sorted(x))).reset_index()

def pregunta_12():
     return resultado