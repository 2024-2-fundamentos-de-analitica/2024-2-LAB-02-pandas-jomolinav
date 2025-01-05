"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd 
archivo = "files/input/tbl0.tsv"
file = pd.read_csv(archivo, sep='\t')


#grupo = file.groupby("c1")["c2"]
resultado = file.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).to_frame()
#print(resultado)

def pregunta_10():
    return resultado