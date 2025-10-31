'''
Requisitos de finalización
🔢 Ejercicio: Fusión de Datos con Left Join
En este ejercicio, trabajarás con dos conjuntos de datos almacenados en los archivos ventas1.csv y productos.csv. 
El objetivo es combinar ambos DataFrames utilizando una fusión (left join) en la columna "Producto_ID", asegurando que se conserven todas las ventas, incluso si algún producto no está registrado en el archivo de productos.

📂 Fuentes de datos:

🔗 Descargar archivo ventas1.csvhttps://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b
🔗 Descargar archivo productos.csvhttps://drive.google.com/uc?export=download&id=1Vbfvur9orXO3lbb9RQgu27hAg1F9BMKm

Los archivos de datos están disponibles en ventas1.csv y productos.csv.

Para cargar estos datos en Python, debes usar la biblioteca pandas y leer los archivos en DataFrames.

🔹 Objetivo del ejercicio:

✅ Cargar los datos desde los archivos ventas1.csv y productos.csv en DataFrames de pandas.
✅ Realizar una fusión (left join) en base a la columna "Producto_ID" utilizando pd.merge().
✅ Asegurar que todas las ventas se mantengan, incluso si no hay coincidencias en el archivo de productos.
✅ Mostrar las primeras 10 filas del DataFrame resultante para verificar la fusión.
'''
import pandas as pd

urlventas="https://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b"
urlproductos="https://drive.google.com/uc?export=download&id=1Vbfvur9orXO3lbb9RQgu27hAg1F9BMKm"

dfventas=pd.read_csv(urlventas)
dfproductos=pd.read_csv(urlproductos)

print(dfventas.head())
print(dfproductos.head())

dfCombinado = pd.merge(dfventas, dfproductos, how="left", on = "Producto_ID")