import matplotlib.pyplot as mp

meses=["Enero","Febrero","Marzo","Abril"]
ventas=[120,150,110,200]

#mp.TipoDeGrafica(x,y, LibreriaParaMasParametros)
#Color web para hexadecimal de colores
mp.plot(meses,ventas, color="#F527EB")
mp.title("Evolucion de ventas")
mp.xlabel("Meses")
mp.ylabel("Ventas")
mp.grid(True, color="#7A7A7A53")
mp.show()