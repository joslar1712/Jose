''' 
Crea una serie con los siguientes datos:[100,200,300,400,500].
Asigna como indices los nombres de los dias de la semana:["Lunes","Martes","Miercoles","Jueves","Viernes"].
Accede al valor correspondiente al indice "Miercoles"
Calcula el promedio de los valores de la serie
Crea una nueva serie sumando 50 a cada valor de la original
''' 
'''
import pandas as pa
serie={
    'series':[100,200,300,400,500],
    'dias':["Lunes","Martes","Miercoles","Jueves","Viernes"]
}'''
import pandas as pa
serie = pa.Series([100,200,300,400,500], index=["Lunes","Martes","Miercoles","Jueves","Viernes"])
#Accediendo al indice miercoles
print(f"El valor de miercoles es: {serie['Miercoles']}")
#Calcula el promedio de los valores de la serie
print(f"El promedio de la serie es: {serie.mean()}")
#Crea una nueva serie sumando 50 a cada valor de la original
'''for i in serie:
    serie+=50'''
#Forma mas sencilla para sumar sin for
serie+=50
print(f"La serie sumandole 50 a cada elemento es:\n{serie}")
print(f"La serie sumandole 50 a cada elemento es:\n{serie.values}")