'''
Crear un csv con datos 
Nombres:
Apellidos
Sexo
Año de nacimiento

Exportar a excel solo 5 datos de
Nombres
Apellidos
Edad
'''
import pandas as pd

#Importando archivo completo
#No es necesario pero es con fines educativos
dfc=pd.read_csv("Jose/data/Ejer1ImpExp.csv")
print(dfc)
#Forma de modificar columnas con un df entero.
alt=["Nombres","Apellidos"]
dfca=dfc[alt]
print(dfca)

#Importando especificamente lo que necesitamos
df=pd.read_csv("Jose/data/Ejer1ImpExp.csv", usecols=["Nombres","Apellidos","Año de nacimiento"],
               nrows=5)
print(df)
df['Edad']=2025-df['Año de nacimiento']
print("\nAñadiendo Edad:")
print(df)
#Ordenando de mayor a menor
dfOrdenado=df.sort_values(by="Nombres")
print(dfOrdenado)
#Exportando df ordenado
dfOrdenado.to_excel("EjercicioImpExpPD.xlsx",index=False)