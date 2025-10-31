'''Multiplicación: Hacer un programa que solicite al usuario números enteros siempre y cuando sean menores de 10 
e imprima la multiplicación de cada uno de los números digitados(3*5*6*3..). Cuando el usuario digite un número 
mayor de 10 imprima la multiplicación que lleva hasta el momento'''
multiplicacion=1
lista=[]
while True: 
    numero = int(input("Ingrese un número entero: "))
    if numero < 10:
        lista.append(numero)
    else:
        for i in lista:
            multiplicacion *= i
        break
    
print(f"La multiplicacion de los numeros es: {multiplicacion}")
        
