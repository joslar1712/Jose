persona= {
    "nombre" : "Mauricio",
    "edad" : 42,
    "ciudad": "chiquinquira"
}

print (persona ["edad"])
persona ["nombre"]="juanito"
print (persona)
persona["profesion"]="ingeniero"
print (persona)
print(persona.keys())
data2={
    "estrato" : 2,
    "eps" : "sanitas",
    "comidas" : ["pastas" , "mexicana"],
    "profesion" : "carnicero",
    "direccion" :{
        "calle" : "carrera",
        "numero" : "75-26",
        "complemento" : "Apto 602"
    } 
}
persona.update(data2)
print (persona) 
print (f"nombre: {persona["nombre"]} apartamento: {persona["direccion"]}")
print (f"nombre: {persona["nombre"]} apartamento: {persona["direccion"]["complemento"]}")
print (f"segunda comida {persona["comidas"]}")
print (f"segunda comida {persona["comidas"][1]}")


