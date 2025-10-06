import random;

frutas =['uva', 'pera', 'manzana','banano','fresa']


print(frutas[0])#accede al primer elemento 
print(frutas[-1])# accede al ultimo elemento de la lista 
print('---------')
#recorrer toda la lista elemento por elemento 
for elemento in frutas:
    print(elemento)
print('---------')
#eliminar manzan??
#del frutas [2]
print(frutas)
if 'manzana' in frutas:
    print('manzana se encuetra en la lista')
else: 
    print('manzana no se encuentra en la lista')
    
print('---------')   
# contar elementos d ela lista 
print(f'la lista de fruta contien {len(frutas)} elementos')

f_corta= [f for f in frutas if len (f)<=4]
print(f'la lista cuenta con {len(f_corta)} frutas con nombres cortos ')
print(f'la frutas co nobre corto son:  {len(f_corta)} ')

print('---------')  

f_corta2 = []
for f in frutas:
    if len(f)<=4:
        f_corta2.append(f)



print(f'la lista cuenta con {len(f_corta2)} frutas con nombres cortos ')
print(f'la frutas co nobre corto son:  {len(f_corta2)} ')


n=random.randint(1,11)
print(f'numero aleatorio es {n}')

nu=[]
nu = random.randint(1,50)
for nu in range(15):
    nu.apepnd(nu)

