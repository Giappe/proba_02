import random
import time 

# PROIZVOD - naziv, opis, cena
# KORPA - spisak_proizvoda, ukupna_cena

class Proizvod:
    def __init__(self, naziv, opis, cena):
        self.naziv = naziv
        self.opis = opis
        self.cena = cena
    
class Korpa:
    def __init__(self, spisak_proizvoda):
        self.spisak_proizvoda = spisak_proizvoda # svojstvo 1
        res = 0
        for pr in spisak_proizvoda:
            res += pr.cena
        self.ukupna_cena = res # svojstvo 2
        
pr1 = Proizvod("Patike", "Fudbalske patike", 27000)
pr2 = Proizvod("Patike", "Kosarkaske patike", 15000)
pr3 = Proizvod("Papuce", "Crocs", 5000)

lista_pr = []
lista_pr.append(pr2)
lista_pr.append(pr1)
lista_pr.append(pr3)

korpa = Korpa(lista_pr)
print(korpa.ukupna_cena)

# ----------------------------------------------------------------------------

class Team:
    def __init__(self, naziv_tima):
        self.naziv_tima = naziv_tima

class Score:
    domaci = 0
    gosti = 0

class Match:
                #      Team  Team    int   Score
    def __init__(self, tim1, tim2, minuti, score):
       self.domaci = tim1
       self.gosti = tim2
       self.minuti = minuti
       self.score = score
    
    def start(self):
        print("Zapoceta je utakmica")
        while True:

            # self.score.domaci = random.randint(0, 10)
            # self.score.gosti = random.randint(0, 10)
            nas_broj_tim_1 = 5
            nas_broj_tim_2 = 7
            if nas_broj_tim_1 == random.randint(0, 10):
                self.score.domaci += 1
                self.score.gosti += 0

            if nas_broj_tim_2 == random.randint(0, 10):
                self.score.domaci += 0
                self.score.gosti += 1

            print(f"{self.domaci.naziv_tima} - {self.gosti.naziv_tima}")
            print(f"{self.score.domaci} - {self.score.gosti}")

            time.sleep(2)

            self.minuti += 5

            if self.minuti >= 90:
                print("Utakmica je gotova")
                return
    
tim1 = Team("Crvena Zvezda")
tim2 = Team("Partizan")

utakmica = Match(tim1, tim2, 0, Score())
utakmica.start()

        