x = 100 # int
print(x)
poruka = "Hello" # str
print(poruka)

class Proizvod:
    def __init__(self, naziv, cena):
        self.naziv = naziv
        self.cena = cena
    
    def __str__(self) -> str:
        return f"Naziv: {self.naziv} Cena: {self.cena}"
    
    def __add__(self, drugi):
        return self.cena + drugi.cena


p1 = Proizvod("Laptop", 500)
print(p1)

p2 = Proizvod("Telefon", 400)
print(p2)

print(p1 + p2)

a = 10
b = 15
print(a+b)
m1 = "Hello "
m2 = "World!"
print(m1+m2)

def predavanje(slajdovi = "", materijali = "", pribor = ""):
    pass

predavanje()
predavanje("poneo sam slajdove")
predavanje("poeo sam slajdove", "tu su materijali")
predavanje("slajdovi poneti", "imam materijale", "pribor je tu")
predavanje(pribor="doneo sam pribor")