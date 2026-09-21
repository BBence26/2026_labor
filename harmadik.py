#nyelvi szerkezetek

import random
from random import randint
#from random import *

def kerter (a,b):
    k=2*a+2*b
    print(f'Kerület: {k}')
    return k

def lotto():
    from random import randint
    i=0
    while i<5:
        print(randint(1, 90))

#FŐPROGRAM
felh_kora = 25 #int(input("Hány éves vagy: "))
if felh_kora <= 18:
    print("Gyerek")
elif felh_kora <=25:
    print('Ifjú')
elif felh_kora <=65:
    print('Koros')
else:
    print('Nyugger')
    uzenet = 'Gyere be' if felh_kora <=18 else 'Maradj kint'
    print(uzenet)

    i=1
    while i<10:
        print(i)
        if i == 3:
            continue
        if i == 5:
            break
    else:
        print('Gond nélkül lefutott')
    print("Vége a ciklusnak!")

alap=5
magassag=3
print(kerter(alap,magassag))

#kerulet = kerter (alap, magassag)[0]
#terulet = kerter (alap, magassag)[1]
#print(f'Kerület = {kerulet}\nTerület = {terulet}')
#eredmeny = kerter (alap, magassag)
#print(f'Kerület = {eredmeny [0]}\nTerület = {eredmeny [1]}')
#print (f'Kerület = {kerter (alap, magassag)[0]}\nTerület = {eredmeny [1]}')

i=0
while i<10:
    print(random.randint(1,90))
lotto()