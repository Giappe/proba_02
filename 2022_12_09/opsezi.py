x = 10 # globalna promenljiva (globalni opseg)

def poruka():
    print("Hello")
    print(x)
    a = 15 # lokalna promenljiva (lokalni opseg)

def proba():
    global y # sada je y definisana kao globalna
    y = 15
    print(x)


poruka()
proba() # mora se prvo poyvati proba, pa onda print(y). U suprotnom se nista ne desi
print(y)


# TIPOVI PROGRAMIRANJA:
# imperativno programiranje (korak po korak) (C, {Python je baziran na C jeziku}, Basic)
# deklarativno programiranje (opisno) [HTML, SQL]
# proceduralno programirnaje (input, procedura, izlaz)
# objektno programiranje (objekti imaju atribute i operacije)
    # Class (koriste se kao sablon za kreiranje objekata)
    # Prototype (Kao sabloni se koriste kreirani objekti)

# TRI KONCEPTA OBJEKTNOG PROGRAMIRANJA:
# enkapsulacija (koristi se za skrivanje kompleksnih operacija, jedino sto je bitno je rezultat koji se dobija)
# nasledjivanje (kloniranje pojma uz intervenciju radi specifinosti)
# polimorfizam (dve funkcije koje se izsto zovu, ali imaju razlicitu primenu u zavisnosti od konteksta)

