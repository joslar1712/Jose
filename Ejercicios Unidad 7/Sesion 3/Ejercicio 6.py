'''
Serie Fibonacci: Crea un programa que calcule y visualice los elementos de la serie de Fibonacci. Esta serie se define de la siguiente manera:
Fibonacci(0) = 0 
Fibonacci(1) = 1 
Fibonacci( n) = Fibonacci(n-1) + Fibonacci(n-2) 
El usuario tan sólo introducirá el número de elementos que quiere visualizar.
'''
a=int(input("Ingrese el número de elementos de la serie Fibonacci: "))
n=a
Seriefibonacci=[]
fibonacci=0
if n == 0 or n== 1:
    n=2
for i in range (n):
    if i == 0: 
        fibonacci=0
        Seriefibonacci.append(fibonacci)
    elif i == 1:
        fibonacci=1
        Seriefibonacci.append(fibonacci)
    else:
        fibonacci = Seriefibonacci[i-1]+Seriefibonacci[i-2]
        Seriefibonacci.append(fibonacci)
print(f"Los primeros {a} elementos de la serie Fibonacci son: {Seriefibonacci}")