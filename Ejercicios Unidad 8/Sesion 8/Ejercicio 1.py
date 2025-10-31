'''
Ejercicio: Análisis de Ventas por Categoría en una Tienda
En este ejercicio, trabajarás con un conjunto de datos de ventas de una tienda almacenado en Google Drive. 
Tu tarea es cargar estos datos en Python utilizando pandas y realizar un análisis para obtener la cantidad total vendida por categoría.

📂 Fuente de datos:

Los datos están disponibles en el siguiente archivo CSV: https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C

Dado que el editor de Python en Moodle no permite subir archivos directamente, deberás acceder a los datos desde Google Drive y cargarlos en un DataFrame de pandas.

🔹 Objetivo del ejercicio:

Cargar los datos desde el archivo CSV en un DataFrame de pandas.
Mostrar las primeras 10 filas del DataFrame para explorar su estructura.
Agrupar los datos por la columna "Categoría" y sumar la "Cantidad Vendida" de cada grupo.
Mostrar los resultados del análisis.
'''
#Cargar los datos desde el archivo CSV en un DataFrame de pandas.

import pandas as pd
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"

df=pd.read_csv(url)
print(df.head())
#Agrupar los datos por la columna "Categoría" y sumar la "Cantidad Vendida" de cada grupo.
dfAgrupado=df.groupby("Categoría")["Cantidad Vendida"].sum().reset_index(name="Cantidad")
dfAgrupado=dfAgrupado.sort_values(by=("Cantidad"), ascending=False)
print(dfAgrupado)