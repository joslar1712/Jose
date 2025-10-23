'''
En este ejercicio, trabajarás con un conjunto de datos de ventas de una tienda almacenado en Google Drive. Tu tarea será cargar los datos, agrupar las ventas por "Categoría" y generar un gráfico de barras para visualizar los resultados.

📂 Fuente de datos:

Los datos están disponibles en el siguiente archivo CSV: https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C

Dado que el editor de Python en Moodle no permite subir archivos directamente, deberás acceder a los datos desde Google Drive y cargarlos en un DataFrame de pandas.

🔹 Objetivo del ejercicio:

Cargar los datos desde el archivo CSV en un DataFrame de pandas.
Agrupar las ventas por "Categoría" y sumar la "Cantidad Vendida".
Generar un gráfico de barras para visualizar los resultados.
Mostrar los resultados tanto numéricamente como gráficamente.'''
'''
import pandas as pd
import matplotlib.pyplot as mp

df=pd.read_csv("data/ejercicio1und9.csv")
print(df)

dfc = df.groupby("Categoría")['Cantidad Vendida'].sum()
print(dfc)

mp.bar(df["Categoría"],df["Cantidad Vendida"])

mp.show()
'''
import pandas as pd
import matplotlib.pyplot as mp
import gdown 

#Carga importando csv
df=pd.read_csv("data/ejercicio1und9.csv")

#Carga desde google drive
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"#URL archivo google
output = "data/datosund9.csv"
gdown.download(url, output, quiet=False)
df_gd=pd.read_csv("data/datosund9.csv")

print("Data frame con pandas")
print(df.head())#con head mostramos solo 5 filas
print("Data frame con gdown")
print(df_gd)

agrupado = df.groupby("Categoría")["Cantidad Vendida"].sum().reset_index()
print("Datos agrupados por categoria con pd import")
print(agrupado)

agrupadogd = df_gd.groupby("Categoría")["Cantidad Vendida"].sum().reset_index()
print("Datos agrupados por categoria con gdown")
print(agrupadogd)

mp.figure(figsize=(10,6))
mp.bar(agrupadogd["Categoría"], agrupadogd["Cantidad Vendida"], color="cyan")
mp.title("Ventas por categoria")
mp.xlabel("Categoría")
mp.ylabel("Cantidad vendida")
mp.xticks (rotation=45)
mp.tight_layout()
mp.grid(color="#BC3F3F",linestyle="--", linewidth = 0.5)
mp.show()

