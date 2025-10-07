#Permite reutilizar el codigo y dar claridad y limpieza al código
#def define la funcion como unica
# (Parametros) en parentesis
def suma(a,b): # Los parámetros
    sum=a+b    # Procedimeiento
    return sum # Lo que retorna
print(suma(8,10))
print(suma(20,13))
print(suma(27,15))

def cuadrado(n):
    return n**2
numero=cuadrado(2)
print(f"El resultado es: {numero}")

#Funcion saludar
#Aunque no es aconsejable retornor print, lo ideal es
#solo valores como en suma
def saluda():
    return print("Hola Buenos Dias!")
saluda()
#Saluda con nombre
def saluda(nom):
    return print(f"Hola Buenos Dias! {nom}")
saluda("Miguel")

#Ejercicio 1
def cambia(d,o):
    r=[]
    for i in d:
        if i is None:
            r.append(o)
        else:
            r.append(i)
    return r
datos=[1,None,2,None,3]
print(f"Antes {datos}")
print(f"Despues con funcion normal {cambia(datos,0)}")

#Lambda: Toda la duncion debe ser lineal, lo qeu entra:lo que sale
suma2= lambda x,y:x+y #Definimos la funcion lambda
print(f"La suma es usando lambda= {suma2(4,1)}") #Imprimir usando Lamda

cambia2=lambda datos,p: [p if i is None else i for i in datos]
print(f"Antes {datos}")
print(f"Despues con funcion lambda {cambia2(datos,0)}")

#Ejercicio en clase:
#Si tenemos:
numeros=[10,8,45,26,7]
#Funcion que muestre el mayor, el menor y la suma:
#Funcion para el mayor
def mayor(n):
    r=0
    for i in n:
        if i>r:
            r=i
    return r
print(f"El numero mayor es: {mayor(numeros)}")
#Menor
def menor(n):
    r=n[0]
    for i in n:
        if i<r:
            r=i
    return r
print(f"El numero menor es: {menor(numeros)}")
#Suma
def suma(n):
    r=0
    for i in n:
        r += i
    return r
print(f"La suma es: {suma(numeros)}")
#Forma mas sencilla:
#Organizando la lista
def sol (n):
    mx=max(n)
    mn=min(n)
    sm=sum(n)
    return (print(f"El maximo es {mx}, el minimo es {mn}, la suma es {sm}"))

print(sol(numeros))
