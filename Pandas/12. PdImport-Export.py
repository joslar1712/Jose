import pandas as pd

#Cargar archivo .csv
df=pd.read_csv("Jose/data/archivo.csv")
'''
Cuando esta separado por ; o otro como tabulacion se especifica.
df=pd.read_csv("Jose/data/archivo.csv", sep=";")
Cuando no hay encabezado
df=pd.read_csv("Jose/data/archivo.csv", header=None)
Para darle encabezado
df=pd.read_csv("Jose/data/archivo.csv", names=["Producto","Precio","Cantidad"])
Para cambiar el formato de la data
encoding="utf-8"
'''

#Mostrar la data del .csv
print(df)
print(df.head(2)) #Solo dos filas

#Se puede importar especificamente lo que se va a usar para optimizar los recursos 
#Importar columnas especificas del .csv
fr2 = pd.read_csv("Jose/data/archivo.csv", usecols=["Producto","Precio"])
print("Nuevo data frame solo con dos columnas")
print(fr2)

#Importar numero de filas
fr3= pd.read_csv("Jose/data/archivo.csv", nrows=2, encoding="utf-8")
print("Nuevo data frame con solo dos filas")
print(fr3)

#Añadiendo nueva columna al df
df['Total'] = df['Precio'] * df['Cantidad']
print(df)

#Exportando data
df.to_csv("nuevo_archivo.csv",index=False)
# pip install openpyxl lib necesaria para exportar excel
df.to_excel("nuevo_archivo_excel.xlsx",index=False)
df.to_excel("nuevo_archivo_excel_IndexTrue.xlsx",index=True) 