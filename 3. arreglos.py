# En vez de varias variables, se guardan todas en un arreglo
a=1
b=2
c=3
d=[1,2,3]
e=["Pera","Uva","Manzana"]
#Formas de imprimir
print(e)
print(e[1])
#Estructura de datos en python
#() se ingresan parametros para una funcion
#[] Definen elementos
#Definiendo lista
lista=[1,2,3]
print(lista) #[1, 2, 3]
#append(): Agrega al final
lista.append(4)
print(lista) #[1, 2, 3, 4]
#extend(): Extiende agregando elementos de otra lista
lista.extend([5,6])
print(lista) #[1, 2, 3, 4, 5, 6]
#insert(): Inserta en una posicion especifica
lista.insert(2,10)
print(lista) #1, 2, 10, 3, 4, 5, 6]
#remove(): Elimina la primera aparicion del elemento especificado
lista.remove(3)
print(lista) #[1, 2, 10, 4, 5, 6]
#pop(): Elimina y devuelve el elemento en la posicion dada
lista.pop(1)
print(lista) #[1, 10, 4, 5, 6]
#IMPRESIONES:
#Longitud de la lista
print(len(lista))
#Lista total
for elemento in lista:
    print(elemento)
#Tuplas, Arreglos que no se puede modificar una vez definida