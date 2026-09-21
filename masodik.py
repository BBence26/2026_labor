# Ez a második labor feladatait tartalmazza
import harmadik

harmadik.lotto()

felh_kora = int(15.65)
felh_kora = int(input("Hány éves vagy: "))
felh_kora += 19
felh_neve = input('Kérem a nevet:')
felh_neve = "Erik"
felh_neve *= 2
metszet = felh_neve[:-5]
jegyek = [2, 5, 4, 3]
jegyek += [5]
del jegyek[0]
halmaz = {'magyar', 'angol', 'orosz', 3}
hallgato = {"nev": 'Jolán', "kor": 19}
print(hallgato["nev"])
print(halmaz)
print('Szia', felh_neve, "!", jegyek)

print('Jó', 'reggelt', 'DUE!',end='\n\n', sep='-')
print('Több soros\n'
      'kiírás\n'
      '!!!!')

print(f'Szia {felh_neve}! \n{jegyek}')
print(f'Kora: {felh_kora: .2f}')

print(felh_neve.rjust(30, '.'))
print(felh_neve.ljust(30,'.'))
print(felh_neve.center(30, '.'))
print(str(felh_kora).center(30))