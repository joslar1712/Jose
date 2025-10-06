import random
import numpy#python -m pip install numpy
num=[]
for i in range (15):# rango
    num.append(random.randint(1,50))
print(num)
print (sum(num))#suma.
print (max(num))#max.
print (min(num))#min.
prom=sum(num)/15 #promedio #promo=sum(num)/lne(num)
print(prom)
print(num[::-1])#invierta
print(num[-1])#ultimo numero del arreglo
print(set(num))#elimina los elementos duplicados. Quita uno y deja otro
num.sort()#sort de mayor a menor 
print(f"Numeros Ordenados {num}")
num.sort(reverse=True)# ordenelos de manera desendente
print(f"Decendente{num}")
print (num)




arreglo=[1,2,3]
print(arreglo)
Lista=[1,2,3]
my_array= numpy.array(Lista)
print(f"Lista {Lista}")
print(f"arreglo {my_array}")
b=Lista + my_array
print(f"combinar {b}")
array_lista = my_array.tolist()
union = array_lista + Lista
print(f"union de las listas {union}")