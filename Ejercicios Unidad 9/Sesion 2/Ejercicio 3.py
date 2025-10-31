'''
Ejercicio: Análisis de la Distribución de la Cantidad Vendida por Producto con Boxplot
En este ejercicio, trabajarás con el conjunto de datos almacenado en el archivo datos_groupby.csv. Utilizarás la biblioteca Seaborn para generar un boxplot que permita analizar la distribución de la cantidad vendida por producto.

📂 Fuente de datos:

🔗 Descargar archivo datos_groupby.csv https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C

El archivo de datos está disponible en datos_groupby.csv.

Para cargar estos datos en Python, debes usar la biblioteca pandas y leer el archivo en un DataFrame.

🔹 Objetivo del ejercicio:

✅ Cargar los datos desde el archivo datos_groupby.csv en un DataFrame de pandas.
✅ Asegurar que las columnas "Producto_ID" y "Cantidad Vendida" están correctamente definidas.
✅ Utilizar la biblioteca Seaborn para generar un boxplot, donde:

El eje X represente los Productos (o una agrupación adecuada si hay muchos).
El eje Y represente la Cantidad Vendida.
✅ Mostrar el gráfico para analizar la distribución de las cantidades vendidas por producto y detectar posibles valores atípicos.'''
#Importando librerias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mp

#Cargando archivo csv
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pd.read_csv(url)
print(df.head())

#Seleccionar columnas numericas para el mapa de calor
df_numeric=df.select_dtypes(include="number")
print("Columnas numéricas: ")
print(df_numeric.head())

#Calcular matriz de correlacion
matrizCorrelacion=df_numeric.corr()
print("Matriz de correlacion: ")
print(matrizCorrelacion)

#Crear el mapa de calor usando matplot y seaborn
mp.figure(figsize=(8,6))
sns.heatmap(matrizCorrelacion, annot=True, cmap="coolwarm", fmt=".2f",linewidths=0.5)
mp.title("Mapa de calor de la matriz de correlacion")
mp.tight_layout()
mp.show()

