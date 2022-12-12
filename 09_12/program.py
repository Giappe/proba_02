import random # ctrl+click na random otvara taj fajl i sve njegove komponente
# import kalkulator # moduli se importuju na pocetku fajla
# from kalkulator import * # imaportuje se sve iz fajla kalkulator
# import kalkulator as k # skracenica umesto da kucamo pun naziv

import racunanje.kalkulator as k
from racunanje import kalkulator # skracujemo naziv prebacujuci na fajl bez foldera
from racunanje import * # ukljucujem sve iz foldera racunanje

#random.randint (10, 5)

print(k.sabiranje(4, 5))

rezultat_oduzimanja = k.oduzimanje(5, 3)
print(rezultat_oduzimanja)
print(k.sabiranje(2, 5))
print(k.deljenje(8, 2)) # deljenje ide automatski kao float

print(k.oduzimanje(5, 2)) # stavljam u print() da bih video vrednost, inace se ona snima u memoriju i ceka pozivanje

