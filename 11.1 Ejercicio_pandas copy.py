''' 
Crea una serie con los siguientes datos:[100,200,300,400,500].
Asigna como indices los nombres de los dias de la semana:["Lunes","Martes","Miercoles","Jueves","Viernes"].
Accede al valor correspondiente al indice "Miercoles"
Calcula el promedio de los valores de la serie
Crea una nueva serie sumando 50 a cada valor de la original
''' 
import pandas as pa
serie={
    'producto':['Manzana','Banana','Cereza'],
    'precio':[2.5,1.8,3.0],
    'cantidad':[10,15,8]
}
#
df=pa.DataFrame(serie)
print(df)
#Muestra las primeras dos filas del data frame
print(df.head(2))
for i in 