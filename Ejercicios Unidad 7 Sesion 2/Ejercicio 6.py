'''
Serie Fibonacci: Crea un programa que calcule y visualice los elementos de la serie de Fibonacci. 
Esta serie se define de la siguiente manera:
Fibonacci(0) = 0 
Fibonacci(1) = 1 
Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) 
El usuario tan sólo introducirá el número de elementos que quiere visualizar.
'''
n=int(input("Ingrese el numero de elementos para calcular la serie: "))

fibonacci = []
for i in range (n+1):
    fibonacci.append(i)
print(fibonacci)

for i in fibonacci:
    if i == 0:
        print(f"Fibonacci de {i}: 0")
    else if i==1: 
        print(f"Fibonacci de {i}: 1")
    else:
        print(f"Fibonacci de {i}: {(i-1)+(i-2)}")