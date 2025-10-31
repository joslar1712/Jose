'''Tipo de Triangulo: Cree un programa que solicite la longitud de los 3 lados de un 
triangulo e imprima si es equilátero(3 lados iguales), isósceles(2 lados iguales) o 
escaleno(todos los lados diferentes)'''

lado1=float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2=float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3=float(input("Ingrese la longitud del tercer lado del triángulo: "))

if lado1==lado2 and lado2==lado3:
    print("El triángulo es equilátero.")
elif lado1==lado2 or lado2==lado3 or lado1==lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")