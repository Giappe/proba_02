# marka, model, godiste, parkiran
class Automobil:
    broj_tockova = 4
    def __init__(self, marka, model, godiste, parkiran=False):
        self.marka = marka
        self.model = model
        self.godiste = godiste
        self.parkiran = parkiran
    
    # Marka: ... Model: ... Godiste: ... Parkiran / U pokretu
    def informaicje(self): # instancni metod
        status = "Parkiran" if self.parkiran else "U pokretu" # self.parkiran se ne proverava ovde, tako da se ne pise == vec samo ovako kako je u ovom primeru
        return f"Marka: {self.marka} \nModel: {self.model} \nGodiste: {self.godiste} \n{status}"
    
    def info_o_automobilima(): # staticki metod
        print("Automobili imaju 4 tocka")
        print("Najcesce se registruju jednom godisnje")
    
    # parkirakj - proveri da li je auto parkiran -
    # svojstvo parkiran prebaciti u True

    def parkiraj(self):
        if self.parkiran == True:
            print("Vec ste parkirani")
        else:
            self.parkiran = True

automobil1 = Automobil("Citroen", "C4", 2021, True)
# "Marka: Citroen"

print(f"Marka: {automobil1.marka}")
print("Model:", automobil1.model)
print(f"Godiste: {automobil1.godiste}")

print(automobil1.informaicje())

automobil2 = Automobil("Ford", "Focus", 2020, False)

print(automobil2.informaicje())

Automobil.info_o_automobilima()

# class Proizvod:
#     def __init__(self, naziv, opis, cena):
#         self.naziv = naziv
#         self.opis = opis
#         self.cena = cena
        

automobil1.parkiraj()
automobil2.parkiraj()