'''Horas trabajadas: Escribir un programa que pregunte al usuario por el número de horas 
trabajadas y el costo por hora. Después muestre en pantalla el pago que le corresponde'''

horasTrabajadas = float(input("Ingrese el numero de horas trabajadas: "))
costoHora= float(input("Ingrese el costo por hora: "))
pago = horasTrabajadas*costoHora
print(f"El pago correspondiente es: {pago}")