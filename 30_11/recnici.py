osoba = ("Sofija", 25, True)
print(osoba[0])

# kljuc : vrednost, kljuc : vrednost, kljuc : vrednost (parovi se formulisu sa : izmedju dve reci, mogu biti svi tipovi vrednosti: string, int, float...)

osoba_recnik = {"ime":"Sofija", "godine":25, "plava":True}
print(osoba_recnik)
print(osoba_recnik ["ime"])
print(osoba_recnik ["godine"])
print()

for i in osoba_recnik:
    print(osoba_recnik[i])

#ovde len i indeks ne rade kao kod sekvenci

for(kljuc, vrednost) in osoba_recnik.items():
    print("Ovo je kljuc:", kljuc)
    print("Ovo je vrednost:", vrednost)


osoba_2 = {}

osoba_2["ime"] = "Marija"
print(osoba_2)

osoba_2["ime"] = "Sofija"
print(osoba_2)

del osoba_2["ime"]
print(osoba_2)

poruke = {"en": "Hello", "sr":"Zdravo", "de":"Hallo"}


#jezik = input("Unesite jezik: ")

# if jezik == "en" or jezik == "sr" or jezik == "de":
#     print(poruke[jezik])
# else:
#     print("Nemamo ovaj prevod...")

# ENGLESKI: Hello
# SRPSKI: Zdravo
# NEMACKI: Hallo

for(jezik, prevod) in poruke.items():
    if jezik == "en":
        print(f"ENGLESKI: {prevod}")
    elif jezik == "sr":
        print(f"SRPSKI: {prevod}")
    else:
        print(f"NEMACKI: {prevod}")


selekcija = {
    "drzava": "Srbija",
    "broj_pobeda": 0,
    "boje_dresova": ["crvena", "bela"],
    "brojevi_igraca": [9, 5, 13, 20]
    }

for (kljuc, vrednost) in selekcija.items():
    print("KLJUC:", kljuc)
    print("VREDNOST:", vrednost)
    if kljuc == "boje_dresova":
        for boja in vrednost:
            print("Boja:", boja)
    if kljuc == "brojevi_igraca":
        for broj in vrednost:
            print(f"Igrac broj: {broj}") #formatirani string sa f
    else:
        print(f"{kljuc}: {vrednost}")

# ime = "Sofija"
# godine = 25
# plava = True
# slobodna = False

# opis_devojke = f"Ime {ime} je {slobodna} i ima {godine} godina"
# print(opis_devojke)


automobil = {
    "marka": "Citroen",
    "model": "C3",
    "boja": ["crvena", "bela", "crna"],
    "alu_felne": False,
    "godiste": 2017,
    "kubikaza": 1.6
}


# for (kljuc, vrednost) in automobil.items():
#     if kljuc == "marka":
#         print(f"Marka: {vrednost}"),
#     if kljuc == "model":
#         print(f"Model: {vrednost}"),
#     if kljuc == "boja":
#         print(f"Boja: {vrednost}"),
#     if kljuc == "alu_felne":
#         if vrednost == False:
#             print(f"Nema alu felne: nema")
#         else:
#             print(f"Nema alu felne: ima")
#     if kljuc == "godiste":
#         print(f"Godiste: {vrednost}")
#     if kljuc == "kubikaza":
#         print(f"Kubikaza: {vrednost}")


# resenje:

# for kljuc, vrednost in automobil.items():
#     if kljuc == "marka":
#         print(f"Marka automobila: {vrednost}")
#     elif kljuc == "model":
#         print(f"Model {vrednost}")
#     elif kljuc == "boja":
#         for boja in vrednost:
#             print(f"Boja: {boja}")
#     elif kljuc == "alu_felne":
#         if vrednost == False:
#             print(f"Nema alu felne: nema")
#         else:
#             print(f"Nema alu felne: ima")
#     elif kljuc == "godiste":
#         print(f"Godiste: {vrednost}")
#     elif kljuc == "kubikaza":
#         print(f"Kubikaza: {vrednost}")

'''
# automobili = {
#     "BG-123": {
#         "marka": "Citroen",
#         "model": "C3",
#         "kubikaza": 1.6,
#         "boje": ["crvena", "bela", "crna"]
#     },
#     "BG-456":{
#         "marka": "Opel",
#         "model": "Astra",
#         "kubikaza": 2.0,
#         "boje": ["plava", "metalik"]
#     },
#     "BG-456":{
#         "marka": "Audi",
#         "model": "Q2",
#         "kubikaza": 2.0,
#         "boje": ["srebrna", "metalik"]
#     }
# }
'''

automobili = {
    "BG-123": {
        "marka": "Citroen",
        "model": "C3",
        "kubikaza": 1.6,
        "boje": ["crvena", "bela", "crna"]
    },
"BG-456":{
        "marka": "Opel",
        "model": "Astra",
        "kubikaza": 2.0,
        "boje": ["plava", "metalik"]
    },
"BG-456":{
        "marka": "Audi",
        "model": "Q2",
        "kubikaza": 2.0,
        "boje": ["srebrna", "metalik"]
    }
}


# for reg, detalji in automobili.items():
#     print("REGISTRACIJA", reg)
#     print("DETALJI", detalji)


for reg, detalji in automobili.items():
    for key, value in detalji.items():
        print(f"kljuc: {key}: {value}")
    print("--------------------------------")




kursevi = {
    "PPF": {
        "naziv": "Python Fundamentals",
        "semestar": 1
    },
    "OOP": {
        "naziv": "Python Object Oriented",
        "semestar": 1
    },
    "OPP": {
        "naziv": "Python Project Oriented",
        "semestar": 1
    }
}

for id_kursa, detalji in kursevi.items():
    for k, v in detalji.items():
        print(k, v)


# LISTA []

# RECNIK {kljuc: vrednost}
# SKUP {} - clanovi se ne mogu ponavljati, ene moze sadrzati dve iste vrednosti

boje_u_ponudi = {"bela", "plava", "crvena", "crvena"}
print(boje_u_ponudi)

boje_u_ponudi.add("zuta")
boje_u_ponudi.remove("bela")
print(boje_u_ponudi)