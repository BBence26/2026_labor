#Ez a második labor feladatait tartalmazza
import harmadik
#felh_kora=int(15.45)
felh_kora=int(input("Hány éves vagy: " ))
felh_kora+=1

#felh_neve='Bence'
felh_neve=input("Kérem a nevet: ")
#felh_neve*=2

metszet=felh_neve[2]
metszet2=felh_neve[2:5]
metszet3=felh_neve[:-5]

#print('Szia', felh_neve+'!', felh_kora,metszet3)

jegyek=[2,5,4,3]
jegyek+=[5]
del jegyek[0]
print('Szia', felh_neve+'!', jegyek) #jegyek[2]

halmaz={'magyar','angol','orosz',3}
print(halmaz)

hallgato={"nev":'Jolán',"kor: ": 19}
print(hallgato["nev"])

print (hallgato["nev"])
print(halmaz)
print('Szia', felh_neve, "!", jegyek)
print('Jó', 'reggelt', 'DUE!', end='\n\n', sep='-')
print('Új sor')


