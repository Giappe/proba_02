

ime="sofija"
len(ime) #funkcija
ime.upper() #metoda

# DEFINISANJE FUNKCIJE
def ispisi_poruke(): #pocinje malim slovom, ne sme sadrzati definisane funkcije
     # telo funkcije
     print("Zdravo")
     print("Danasnji datum je 2.12")
     print("Predavanje Python")
    
# poziv funkcije

ispisi_poruke()


# ime = "Sofija"
# def pozdravna_poruka():
#     print(f"Hallo {ime}")



# ULAZNI PARAMETRI FUNKCIJE:

def pozdravna_poruka(ime):
    print(f"Hello {ime}")

pozdravna_poruka("Sofija")

pozdravna_poruka("Marija")


def prikazi_informacije(ime, poeni=0):
    print(f"Student: {ime}, poeni: {poeni}")

prikazi_informacije("Nikola", 154)
prikazi_informacije("Marija")

def saberi(a=0, b=0):
    print(a, b)
    print(a + b)

saberi(10, 55)
saberi()
saberi(10) # automatski dodeljuje vrednost u a
saberi(b = 20) # podrazumeva vrednost za a da je 0 i dodaje 20 u b
saberi(b = 20, a = 10) # direktno se postavlja pozicija i rednost, bez obzira na redosled u definisanoj funkciji

#prvi sabirak, drui, operacij
def kalkulator(a, b, o):
    if o == "+":
        print(a + b)
        return a + b
    elif o == "-":
        print(a - b)
        return a - b
    elif o == "*":
        print(a * b)
        return a * b
    elif o == "/":
        if b == 0:
            print("Nije dozvoljeno deljenje sa nulom")
        else:
            print("Proverite operaciju (+, -, *, /)")

# povratna vrednost funkcije: return, koja se moze smestiti u neku promenljivu i koristiti se dalje u kodu


# kalkulator(int(input("Unesite broj:"))), int(input("Unesite drugi broj:")), input("Unesite operaciju (+, -, *, /)")

