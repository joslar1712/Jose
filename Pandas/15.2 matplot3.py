import matplotlib.pyplot as mp

#El exito de la analitica dependera de saber que tipo de datos ingresa para poder tratarla adecuadamente

edades=[20,21,22,25,25,26,27,30,35,40,42]

mp.hist(edades, bins=5, color="darkblue", edgecolor="black")
mp.title("Rango de edades")
mp.xlabel("Edades Rnagos")
mp.ylabel("Distrivucion de edades")
mp.show()