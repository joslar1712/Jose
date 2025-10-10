import matplotlib.pyplot as mp

edades=[22,25,30,30,32,35,40,42,50,55,60,60,65,70,75]

# Crea un histograma para analizar la distribuion de edades
mp.scatter(edades, bins=5, color="Chocolate")
mp.show()
# Ajusta el número de bins (intervalos) para mostrar los datos de manera mas clara.
# Asegurate de incluir untitulo, nombres de los ejes, colores que faciliten la visualizacion