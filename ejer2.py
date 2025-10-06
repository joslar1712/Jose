import random;

nu=[]


for r in range(15):
    n = random.randint(1,50)
    nu.append(n)
   
print(nu)
np= [f for f in nu if  f % 2 == 0]
ni = [f for f in nu if f % 2==1]

print(f'la lista cuenta con los siguiente números pares {np} ')
print(f'la lista cuenta con los siguiente números impares {ni} ')

if 32 in nu:
    print ('si esta el numero 32')
else:
     print ('no. esta el numero 32')

print(nu)
print(sum(nu))
print(max(nu))
print(min(nu))
prom = sum(nu)/len(nu)
print(prom)
print(0)
print(nu[::-1])
print(nu[-1]) 
nu.sort(reverse=True)
print(nu)