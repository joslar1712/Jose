'''
Utiles para en caso que se tengas mas objetos dentro del objeto, por ejemplo
una persona con varios estudios.
''' 
#Arreglos con objetos y objetos anidados
import pandas as pd
#Leyendo archivo Json
df=pd.read_json("data/DataArregloObjetosyObjetosanidados.json")
print(df)

#Normalizacion de data
#Al impromir 
df_normalizado=pd.json_normalize(df["estudios"])
print(df_normalizado)

#Concatenemos
df_final = pd.concat([df.drop(columns='estudios'),df_normalizado],axis=1)
print(df_final)
#Esto permite que podamos usar todos los datos de la tabla ya que se trajeron
#Los objetos dentro del objeto.
