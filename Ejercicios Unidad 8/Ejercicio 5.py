'''
🔢 Ejercicio: Cálculo de "Ingresos Totales" tras la Fusión de Datos
En este ejercicio, trabajarás con dos conjuntos de datos almacenados en los archivos ventas1.csv y productos.csv. Después de fusionar los DataFrames, crearás una nueva columna llamada "Ingresos Totales", calculada como el producto de "Cantidad Vendida" y "Precio Unitario".

📂 Fuentes de datos:

🔗 Descargar archivo ventas1.csvhttps://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b
🔗 Descargar archivo productos.csvhttps://drive.google.com/uc?export=download&id=1Vbfvur9orXO3lbb9RQgu27hAg1F9BMKm

Los archivos de datos están disponibles en ventas1.csv y productos.csv.

Para cargar estos datos en Python, debes usar la biblioteca pandas y leer los archivos en DataFrames.

🔹 Objetivo del ejercicio:

✅ Cargar los datos desde los archivos ventas1.csv y productos.csv en DataFrames de pandas.
✅ Establecer la columna "Producto_ID" como índice en ambos DataFrames utilizando .set_index("Producto_ID").
✅ Fusionar los DataFrames utilizando el método adecuado (.join() o pd.merge()).
✅ Crear una nueva columna llamada "Ingresos Totales", calculada como:

Ingresos Totales = Cantidad Vendida * Precio Unitario
✅ Mostrar las primeras 10 filas del DataFrame resultante para verificar los cálculos.
'''
import pandas as pd
#Descargando data
urlVentas="https://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b"
urlProductos="https://drive.google.com/uc?export=download&id=1Vbfvur9orXO3lbb9RQgu27hAg1F9BMKm"

#Asignando data a df
dfVentas = pd.read_csv(urlVentas)
dfProductos = pd.read_csv(urlProductos)
print(f"Datos ventas: \n {dfVentas.head()}")
print(f"\nDatos productos: \n {dfProductos.head()}")

#Establecer columna de "Producto_ID" como indice en los df
dfVentas.set_index("Producto_ID", inplace=True) # El inplace es para que no cree otro df si no lo haga ahi mismo
dfProductos.set_index("Producto_ID", inplace=True)
'''
#Fusionar los DataFrames utilizando el método adecuado (.join() o pd.merge()).
dfCombinado= dfVentas.join(dfProductos, how="inner")#How inner es para que los una cuando los dos datos de los df coincidan
print("\n Datos Fusionados:")
print(dfCombinado.head())
'''
#Con merge funciona igual
dfCombinado= pd.merge(dfVentas, dfProductos, on="Producto_ID", how="inner") # on producto id quiere decir cuando el indice de la izquierda = indice izquierda haga union
print("\n Datos Fusionados con merge:")
print(dfCombinado.head())

dfCombinado["Ingresos Totales"] = dfCombinado["Cantidad Vendida"] * dfCombinado["Precio Unitario"]
print(f"\Df combinado con ingresos totales:\n {dfCombinado.head(10)}")