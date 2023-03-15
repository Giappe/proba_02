

class Automobil:
    marka    = ""
    model    = ""
    godiste  = 0
    alu_felne = False
    broj_tockova = 4 # staticko svojstvo
    # __jmgb = 0 # dve donje crte skrivaju vrednost izvan klase (tako se stite informacije),
    # # jedna dona crta daje pristup naslednicima klase, ali ne i ostalim korisnicima

    #metode
    def vozi(self):
        print("Auto je u pokretu")
        print(self.model)
    
    def postavi_felne(self):
        if self.alu_felne == True:
            print("Imate vec alu felne")
        else:
            self.alu_felne = True
            print("Postavljene su alu felne")


auto1 = Automobil()
print(auto1.model, auto1.marka, auto1.godiste, auto1.alu_felne)



auto1.marka = "Citroen"
auto1.model = "C3"
auto1.godiste = 2017
auto1.alu_felne = False
print(auto1.model, auto1.marka, auto1.godiste, auto1.alu_felne)

# staticko svojstvo je klasa koja ima zajednicko svim sutomobilima (svi imaju 4 tocka, farove, asupuh)
# instancno svojstvo su instancirane klase, vezano je za isti objekat, ali ima razlicite odlike (jedni su Citreon, drugi su sportski, razlicitih su boja)

Automobil.broj_tockova # pristup statickom svojstvu

auto1.vozi()
auto1.postavi_felne()

# STRING tipovi
slova = "AbcD"
slova = str() #""
slova = "AbcD"

slova.upper() # metoda stringa
slova.lower()

