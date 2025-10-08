'''
Pandas manipulacion y analisis de datos.
facilita limpieza, transformacion y uso de los datos
Numpy
'''
#Accediendo con indices
import pandas as pa

serie = pa.Series([10,20,30], index=['A','B','C'])
print(serie)
print (serie['B'])
#Accediendo con posicion
serie2 = pa.Series([10,20,30])
print(serie2)
print(serie2[2])
#Sacando el promedio
print(serie2.mean())