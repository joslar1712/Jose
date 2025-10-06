'''
Diccionarios de datos: Archivos.json
Antes usaba XML que era un lenguaje etiquetado
Ahora se usa .json con clave valor, son mas dinamicos.
'''
persona={
    "nombre":"Jose",
    "edad":25,
    "ciudad":"Bogota"
}
#Imprimiendo la coleccion
print(persona)
#Accediendo a un atributo de la coleccion
print (persona["edad"])
#Modificando datos de la coleccion
persona["ciudad"]="Soacha"
print(persona)
persona["Profesion"]="Ingeniero"
print(persona)
#Para ver las claves o atributos del diccionario 
print(persona.keys())
data2={
    "estrato":2,
    "eps":"Compensar",
    "comidas":["pasta","sancocho"],
    "Profesion":"Electricista",
    "direccion":{
        "calle":"carrera",
        "numero":"25-54",
        "complemento":"Apto 703"
    }
}
#Para unificar o concatenar la informacion de las colecciones
persona.update(data2)
print(persona)
#Para imprimir de forma especifica:
print(f"Nombre: {persona["nombre"]} apartamento: {persona["direccion"]["complemento"]}")
print(f"Segunda comida {persona["comidas"][1]}") #Accediendo a arreglos
