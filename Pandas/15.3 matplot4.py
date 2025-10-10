import matplotlib.pyplot as mp

ingresos=[100,200,300,500,550]
gastos=[80,120,250,400,520]
'''
mp.scatter(gastos,ingresos, color="chocolate")
mp.title("Gastos vs Ingresos")
mp.xlabel("Gastos")
mp.ylabel("Ingresos")
mp.show()'''

mp.plot(gastos,ingresos, color="chocolate")
mp.title("Gastos vs Ingresos")
mp.xlabel("Gastos")
mp.ylabel("Ingresos")
mp.show()