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