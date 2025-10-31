'''
Tornillo: Cree un programa que solicite el tamaño de un tornillo e imprima su 
tamaño de acuerdo a las siguientes condiciones: 
De 1 cm(incluído)  hasta 3 cm(no incluído) es pequeño
De 3 cm(incluído) hasta 5 cm(no incluído) es mediano
De 5 cm(incluído) hasta 6.5 cm(no incluído) es grande
De 6.5cm (incluído) hasta 8.5 cm(no incluído) es muy grande
De 8.5 cm(incluído) en adelante es gigante'''

tamano=float(input("Ingrese el tamaño del tornillo en centímetros: "))
if tamano==1 or tamano <= 3:
    print("El tornillo es pequeño.")
elif tamano==3 or tamano <= 5:
    print("El tornillo es mediano.")
elif tamano==5 or tamano <= 6.5:
    print("El tornillo es grande.")
elif tamano==6.5 or tamano <= 8.5:
    print("El tornillo es muy grande.")
else:
    print("El tornillo es gigante.")