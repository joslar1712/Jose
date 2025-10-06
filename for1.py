prom=0
for i in range (3): 
    n1= int(input(f"INGRESE LA CALIFICACION {i+1} : "))
    while n1 > 5 or n1 < 0:
        n1 = int (input (f"INGRESE LA CALIFICACION {i+1}: "))
    prom = prom + n1
    #prom += n1
prom = prom / 3
if prom >=3:
    print (f"Aprovado nota {prom}")
else : 
    print (f"Reprovado nota {prom}") 
    
       
    
    
    