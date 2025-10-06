#TIPOS DE ESTRUCTURA FOR
for i in range (5):
    print("Hello World")
    #Inicio incluyente, final excluyente
for i in range (5):
    print(f"Hello World {i}")
    #Se puede especificar variable de inicio, final y los pasos
for i in range (12,15,1):
    print(f"Hello World {i}")
#Ejemplo para recibir notas
promedio=0.0
for i in range(3):
    nota=float(input(f"Ingrese nota {i+1}:"))
    #promedio = promedio + nota
    promedio += nota
promedio=promedio/3
if promedio >= 3:
    print("Aprobó")
else:
    print(f"Reprobó promedio: {promedio}")
#Ejemplo bucle while
for i in range(3):
    nota=float(input(f"Ingrese nota {i+1}:"))
    promedio += nota
promedio=promedio/3
if promedio >= 3:
    print("Aprobó")
else:
    print(f"Reprobó promedio: {promedio}")