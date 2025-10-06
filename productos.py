productos=[
    {"nombre" : "manzana", "categoria":"frutas","valor" : 500 },
    {"nombre" : "pan rollo", "categoria" : "pan" , "valor" : 600},
    {"nombre" : "pera", "categoria":"frutas","valor" : 200 },
    {"nombre" : "espinaca", "categoria" : "verdura" , "valor" : 300},
    {"nombre" : "guineo", "categoria" : "verdura" , "valor" : 300}
]
#Agrupar productos por categorias 

agrupados={}
for producto in productos:
    cat=producto ["categoria"]
    if cat not in agrupados:
        agrupados [cat]= []
    agrupados[cat].append([producto["nombre"],producto["valor"]])
    
print(agrupados)
