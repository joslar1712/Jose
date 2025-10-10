#Install matplot
# python -m pip install matplotlib
#Documentacion:
#https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py

import matplotlib.pyplot as mp

productos=["Manzanas","Peras","Naranjas"]
ventas=[50,80,30]

#alimentacion de datos, ejes x,y
mp.bar(productos,ventas)
mp.title("Ventas por producto")
mp.xlabel("Productos")
mp.ylabel("Ventas")
mp.show()

