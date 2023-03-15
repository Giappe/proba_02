import time

class Vozilo:
    def __init__(self,tip,brzina):
        self.tip            = tip
        self.brzina         = brzina
        self.destinacija    = 0
        self.trenutna_tacka = 0
        self.stigao = False

    def korak(self):
        self.trenutna_tacka += self.brzina
        if self.trenutna_tacka >= self.destinacija:
            self.stigao = True
            print(self.tip,"je stigao")

    def kreni(self,destinacija):
        self.destinacija    = destinacija
        self.trenutna_tacka = 0

class Auto(Vozilo):
    def __init__(self):
        super().__init__("Auto",100)

class Kamion(Vozilo):
    def __init__(self):
        super().__init__("Kamion",100)


a = Auto()
k = Kamion()
a.kreni(1200)
k.kreni(800)
vozila = [a,k]
while True:
    for v in vozila:
        v.korak()
        if v.stigao:
            vozila.remove(v)
    time.sleep(0.5)