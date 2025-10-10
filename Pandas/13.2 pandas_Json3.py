import pandas as pd
#Filtrando por formato fecha 
#Leer Json
df = pd.read_json("data/Json3.json")
print("DataFrame original: ")
print(df)
'''Aunque asi funciona no deberia ser asi, ya que se comparan cadenas string pero la fecha en la data debe ser anio-mes-dia
#Filtro por fecha
dfFiltrado = df[df["fecha_Nac"] > "2000-01-01"]
print("Nuevo data frame por fecha")
print(dfFiltrado)
'''
#Filtro por fecha
#Tener en cuenta los formatos y que todo este fe la misma manera en la data, debe formatearse con excel
df["fecha_Nac"]=pd.to_datetime(df["fecha_Nac"],format=('%d/%m/%Y'))#Pasando fecha a un formato de fecha segun como esta en la data
dfFiltrado = df[df["fecha_Nac"].between('1998-01-01','2001-01-01')]#between es para filtrar en un rango de fechas
print("Nuevo data frame por fecha")
print(dfFiltrado)