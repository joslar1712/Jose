#Todo parte de analizar como viene la data y como debemos tratarla para obtener un resultado
#Objetos con arreglos adentro
import pandas as pd

df=pd.read_json("data/DataobjetosArreglo.json")
print(df)

#Se debe separar por grupos el Json para poder serializar los datos y poder usarlos
dfg1= pd.DataFrame(df["grupo1"].tolist())
dfg2= pd.json_normalize(df["grupo2"])

print("Datos 1:")
print(dfg1)
print("Datos 1:")
print(dfg2)

#Unificando la data con axis 0 por columnas axis 1 por filas
df_final=pd.concat([dfg1,dfg2],axis=0,ignore_index=True)
print(df_final)
#Duplicando valores y filtrando
print("Validacion de data duplicada:")
print(df_final.duplicated())
#Sumatoria de de duplicados
print("Total de datos duplicados:")
print(df_final.duplicated().sum())

#Verificar duplicados por columna
#Los duplicados seran los datos que se repiten despues de encontar el primero
print("Verificando duplicados en columna Id:")
print(df_final)
print(df_final.duplicated(subset=["Id"]))

#Verificar duplicados por  varias columnas
print("Verificando duplicados en columna Id y Nombres:")
print(df_final)
print(df_final.duplicated(subset=["Id","Nombre"]))

#Eliminando datos duplicados
#Siempre crear un df aparte del original si se va a manipular
#Creando data frame sin datos duplicados
dfLimpio=df_final.drop_duplicates()
print("Dataset con duplicados:")
print(df_final)
print("Dataset sin duplicados:")
print(dfLimpio)

#Para eliminar las ultimas duplicadas en vez de la primera
dfLimpio=df_final.drop_duplicates(keep="last")
print("Dataset con duplicados:")
print(df_final)
print("Dataset sin duplicados manteneniendo el ultimo:")
print(dfLimpio)

#Para eliminar las ultimas duplicadas en columna especifica
dfLimpio=df_final.drop_duplicates(subset=["Id"])
print("Dataset con duplicados:")
print(df_final)
print("Dataset sin duplicados filtrado por columna:")
print(dfLimpio)

#Transformando data para que sea del mismo tipo
#Suma de edades
print(df_final)
#Convertir Texto en Numero
#Error raise ayuda a indicar en que linea el dato no es coherente con la conversion
df_final["Edad"]=pd.to_numeric(df_final["Edad"],errors='raise')
print(f"Suma edades {df_final['Edad'].sum()}")

