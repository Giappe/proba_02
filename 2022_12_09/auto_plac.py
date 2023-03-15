import car
from car import *

# auto1 = Automobil()
# print(auto1.model, auto1.marka, auto1.godiste, auto1.alu_felne)

class Automobil:
    broj_tockova = 4 # staticko svojstvo

    def __init__(self, zeljena_marka, zeljeni_model, godiste, alu_felne): # instancno svojstvo
        print("Pravim automobil")
        self.marka = zeljena_marka
        self.model = zeljeni_model
        self.godiste = godiste
        self.alu_felne = alu_felne

a = Automobil("Citroen", "C3", 2017, False)

