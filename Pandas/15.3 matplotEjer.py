'''1.'''

import matplotlib.pyplot as mp

meses=["Enero","Febrero","Marzo","Abril"]
ventas=[1500,1800,1200,2000]
gasto_publicitario=[500,700,400,800]

# Crea un grafico de barras que muestre las ventas por cada mes
mp.bar(meses,ventas, color="blue")
mp.title("Ventas por mes")
mp.xlabel("Mes")
mp.ylabel("Ventas")
mp.show()
# Crea un grafico de lineas que muestre la tendencia de las ventas durante los meses
mp.plot(meses,ventas, color="darkblue")
mp.title("Ventas por mes")
mp.xlabel("Mes")
mp.ylabel("Ventas")
mp.show()
# Crea un grafico de dispersion para analizar la relacion entre el gasto publicitario y las ventas
mp.scatter(ventas, gasto_publicitario, color="red")
mp.title("Ventas por mes")
mp.xlabel("Ventas")
mp.ylabel
("Gasto Publicitario")
mp.show()