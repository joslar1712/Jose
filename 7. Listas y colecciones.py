productos=[
    {"nombre":"Manzana", "categoria":"frutas" ,"valor":500},
    {"nombre":"Pan rollo", "categoria":"pan" ,"valor":600},
    {"nombre":"Pera", "categoria":"frutas" ,"valor":200},
    {"nombre":"Espinaca", "categoria":"Verdura" ,"valor":500},
    {"nombre":"Guineo", "categoria":"fruta" ,"valor":300},
    {"nombre":"Zanahoria", "categoria":"Verdura" ,"valor":500}
]
#Agrupar por categoria
agrupados={}
for producto in productos:
    cat=producto["categoria"]
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados[cat].append(producto["nombre"])  
    agrupados[cat].append(producto["valor"])  
    agrupados[cat].append([producto["nombre"],producto["valor"]])
print(agrupados)

''''
#Como puedo agrupar en categoria y precio
agrupados2={}
for producto in productos:
    cat=producto["categoria"]
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados2[cat].append([producto["nombre"],producto["valor"]])
print(agrupados)'''