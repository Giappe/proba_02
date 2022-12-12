# Osoba
# ime, prezime, godine

class Osoba:
    def __init__(self, ime, prezime, godiste):
        print("Osoba A")
        self.ime = ime
        self.preizme = prezime
        self.godiste = godiste

a = Osoba("Marija", "Ivanovic", 1985)

print(a.godiste, a.ime, a.preizme)