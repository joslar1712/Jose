''' 
Crea un data frame con los siguientes datos:
producto: ['Manzana', 'Banana', 'Cereza']
precio: [2.5, 1.8, 3.0]
cantidad: [10, 15, 8]
Muestra las primeras dos filas del data frame
Accede a la columna precio y calcula el precio total de todos los productos(precio * cantidad) y suma el total
Añádelo como una nueva columna llamada 'total'.
Version de IA mas simple: 
import pandas as pd

# Crear el DataFrame
df = pd.DataFrame({
    'producto': ['Manzana', 'Banana', 'Cereza'],
    'precio': [2.5, 1.8, 3.0],
    'cantidad': [10, 15, 8]
})

# Mostrar las dos primeras filas
print(df.head(2))

# Calcular y añadir la columna 'total'
df['total'] = df['precio'] * df['cantidad']
print(df)

# Sumar el total de todos los productos
print("Suma total:", df['total'].sum())
''' 
import pandas as pa
serie={
    'producto':['Manzana','Banana','Cereza'],
    'precio':[2.5,1.8,3.0],
    'cantidad':[10,15,8]
}
#Creando el data frame
df=pa.DataFrame(serie)
print(df)

#Muestra las primeras dos filas del data frame
print(f"Primeras dos filas:\n{df.iloc[[0,1]]}")

#Accede a la columna precio y calcula el precio total de todos los productos(precio * cantidad) y suma el total
totalFila = df['precio']*df['cantidad']
print(totalFila)

#Sumando el total
total=0
for i in totalFila:
    total += i
print(total)

#añadiendo al data frame
df['total']=totalFila
print(df)

