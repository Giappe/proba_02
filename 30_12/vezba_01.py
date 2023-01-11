class Card:
    def __init__(self):
        self.__broj = 0
        self.__boja = ""
        self.__sifra = ""
    @property
    def broj(self):
        return self.__broj
    
    @property
    def boja(self):
        return self.__boja
    
    @property
    def sifra(self):
        return self.__sifra
    
    @broj.setter
    def broj(self, vrednost):
        self.__broj = vrednost
    
    @boja.setter
    def boja(self, vrednost):
        self.__boja = vrednost

    @sifra.setter
    def sifra(self, vrednost):
        self.__sifra = vrednost
    
karta1 = Card()
print(karta1.broj)
karta1.broj = 7
print(karta1.broj)


# -------------------------------------------------------------------

# zadatak:

#boja, model, registracija
#registracija je privatno svojstvo - upotreba property
#ulazni parametar dokumenti, ako su True postavlja se vrednost, u suprotnom se ne postavlja


class Automobil:
    def __init__(self, boja, model):
        self.boja = boja
        self.model = model
        self.__registracija = ""
    
    @property
    def registracija(self):
        return self.__registracija

    @registracija.setter
    def registracija(self, dokumenta):
        if dokumenta:
            self.__registracija = "registrovan je"

a = Automobil("bela", "ford")
print(a.registracija)
a.registracija = True
print(a.registracija)