from abc import *
import time

# class Trening(ABC):
#     def __init__(self, naziv, trajanje, kalorije):
#         self.naziv = naziv
#         self.trajanje = trajanje
#         self.kalorije = kalorije
    
#     def prikazi_opis(self):
#         return "Naziv: {self.naziv}\n Trajanje: {self.trajanje} min\n Kalorije: {self.kalorije} kcal"

#     @abstractmethod
#     def zapocni_trening(self):
#         pass

# class Kardio(Trening):
#     def zapocni_trening(self):
#         print(f"Zapocet je trening: {self.naziv}")
#         time.sleep(5)
#         print(f"Zavrsen je trening. Potrosili ste {self.kalorije} kcal.")



# kardio1 = Kardio("Trcanje", 60, 300)
# kardio1.zapocni_trening()

# -------------------------------------------------------------------------------

# getter-i i setter-i (java way):

# class Osoba:
#     def __init__(self, ime, prezime):
#         self.ime = ime
#         self.prezime = prezime
#         self.__jmbg = "" # privatno svojstvo
    
#     def get_jmbg(self):
#         if self.__jmbg != "":
#             return self.__jmbg
#         else:
#             print("Nije postavljen JMBG")


# class Osoba:
#     def __init__(self, ime, prezime):
#         self.ime = ime
#         self.prezime = prezime
#         self.__jmbg = "" # privatno svojstvo
    
#     def get_jmbg(self):
#         if self.__jmbg != "":
#             # "1234567890101"
#             # "123456798****"
#             prvi_deo = self.__jmbg[0:9]
#             izlaz = prvi_deo + "****"
#         else:
#             print("Nije postavljen JMBG")

#     def set_jmbg(self, vrednost):
#         if isinstance(vrednost, str):
#             if len(vrednost) == 13:
#                 self.__jmbg = vrednost
#             else:
#                 print("JMBG mora da ima 13 karaktera")
#         else:
#             print("Podatak mora da bude string tipa")

# o = Osoba("Sofija", "Sofijic")
# print(o.get_jmbg())
# o.set_jmbg("1234567890101")
# print(o.get_jmbg())

# -------------------------------------------------------------------------------

# Property dekorator: @property @a.setter

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.__jmbg = "" # privatno svojstvo
    
    @property
    def jmbg(self):
        if self.__jmbg != "":
            # "1234567890101"
            # "123456798****"
            prvi_deo = self.__jmbg[0:9]
            izlaz = prvi_deo + "****"
        else:
            print("Nije postavljen JMBG")

    
    @jmbg.setter
    def jmbg(self, vrednost):
        if isinstance(vrednost, str):
            if len(vrednost) == 13:
                self.__jmbg = vrednost
            else:
                print("JMBG mora da ima 13 karaktera")
        else:
            print("Podatak mora da bude string tipa")

o = Osoba("Sofija", "Sofilic")
o.jmbg = "1234567890101"
print(o.jmbg)

