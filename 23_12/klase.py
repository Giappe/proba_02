class Osoba:
    def __init__(self, ime, prezime): # inicijalizator / konstruktor
        self.ime = ime
        self.prezime = prezime
    
    def predstavi_se(self): # self je objekat koji je pozvao efekat 
        return f"Ja sam {self.ime} {self.prezime}"

osoba1 = Osoba("Sofija", "Sofilic") # instanca / objekat su sinonimi
print(osoba1.ime)
print(osoba1.predstavi_se())
poruka_osobe1 = osoba1.predstavi_se()
print(poruka_osobe1)

class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa, ustanova):
        super().__init__(ime, prezime) # poziv roditeljskog konstruktora
        self.broj_indeksa = broj_indeksa
    
    def predstavi_se(self):
        return f"{super().predstavi_se()}, moj broj indeksa je: {self.broj_indeksa}"
        return "OVA OSOBA JE STUDENT"
    

student1 = Student("Sofija", "Sofilic", "55/22", "IT Academia")
print(student1.predstavi_se())

class Profesor(Osoba):
    def __init__(self, ime, prezime, programski_jezik):
        super().__init__(ime, prezime)
        self.programski_jezik = programski_jezik
    
    def predstavi_se(self):
        return f"{super().predstavi_se()}, predajem: {self.programski_jezik}"

prof = Profesor("aleksandra", "lazarevic", "javascript")
print(prof.predstavi_se())

# --------------------------------------------------------------------------------

# zadatak:

# klasa Oblik
# boja
# metoda izracunaj_povrsinu -> print("Racunam povrsinu")

# Kvadrat - nasledjuje klasu oblik
# a
# metoda izracunaj_povrsinu -> zadrzava od roditelja i print(a*a)

# Krug - naslecuje klasu oblik
# r
# metoda izracunaj povrsinu -> zadrzava od roditelja i print(r*r*3.14)

class Oblik:
    def __init__(self, boja):
        self.boja = boja
    
    def izracunaj_povrsinu(self):
        return "Racunam povrsinu"
    
class Kvadrat(Oblik):
    def __init__(self, boja, a):
        super().__init__(boja)
        self.a = a
    
    def izracunaj_povrsinu(self):
        povrsina = self.a * self.a
        return f"{super().izracunaj_povrsinu()}, vrednost je: {povrsina}"

class Krug(Oblik):
    def __init__(self, boja,r):
        super().__init__(boja)
        self.r = r
    
    def izracunaj_povrsinu(self):
        povrsina = self.r*self.r*3.14
        return f"{super().izracunaj_povrsinu()}, rezultat je: {povrsina}"

# -------------------------------------------------------------------------------

# Vezba 2: Credit Card

class Card:
    def __init__(self, broj, stanje):
        self.broj = broj
        self.stanje = stanje
    
    def pay(self, suma):
        self.stanje -= suma

class Visa(Card):
    porez = 1.05

    def pay(self, suma):
        if isinstance(suma, int): # proverava kog je tipa
            self.stanje -= suma * self.porez
        else:
            print("Unesite vrednost int tipa")
            print(type(suma) == str)

class Master(Card):
    porez = 1.08

    def pay(self, suma):
        if isinstance(suma, int):
            self.stanje -= suma * self.porez
        else:
            print("Unesite vrednost int tipa")
            print(type(suma) == str)

print()