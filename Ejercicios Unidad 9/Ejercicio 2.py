'''
En este ejercicio, trabajarás con un conjunto de datos de ventas de una tienda almacenado en Google Drive. Tu tarea será cargar los datos, utilizar la columna "Fecha" para analizar cómo han cambiado las ventas con el tiempo y visualizar los resultados mediante un gráfico de líneas.

📂 Fuente de datos:

Los datos están disponibles en el siguiente archivo CSV: https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C

Dado que el editor de Python en Moodle no permite subir archivos directamente, deberás acceder a los datos desde Google Drive y cargarlos en un DataFrame de pandas.

🔹 Objetivo del ejercicio:

Cargar los datos desde el archivo CSV en un DataFrame de pandas.
Convertir la columna "Fecha" al formato de fecha (datetime).
Agrupar los datos por "Fecha" y calcular el total de "Cantidad Vendida" por día.
Generar un gráfico de líneas para visualizar la evolución de las ventas con el tiempo.
Mostrar los resultados tanto numéricamente como gráficamente.'''

import pandas as pd
import matplotlib.pyplot as mp

