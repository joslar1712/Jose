import pandas as pa

datos = {
    'Nombre':['Juan','Ana','Milena'],
    'edad':[12,25,32],
    'ciudad':['Bogota','Cali','Medellin']
}
#Creando data Frame
dataf= pa.DataFrame(datos)
#Imprimiendo data Frame
print(dataf)
#Accediendo a la columna
print(dataf['edad'])
#Accediendo a la fila por el nombre del indice
print(dataf.loc[1])
#Accediendo a la fila por la posicion del indice
print(dataf.iloc[-1])

#Realizando busquedas
filtro = dataf[dataf['edad']>=25]
print(filtro)
