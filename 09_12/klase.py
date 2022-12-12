# Osoba
# ime, prezime, godine - osobine
# trci, predstavi se - funkcionalnosti

class Osoba:
    ime = ""
    prezime = ""
    godine = 0

osoba1 = Osoba()
print(osoba1.godine)

osoba1.ime = "Sofija"
osoba1.prezime = "Jovanovic"
osoba1.godine = 25

print(osoba1.ime, osoba1.prezime, osoba1.godine)

print(type(osoba1))

osoba2 = Osoba()
osoba2.ime = "Milovan"
osoba2.prezime = "Saric"
osoba2.godine = 29

print(osoba2.ime, osoba2.prezime, osoba2.godine)

prisutni = [osoba1, osoba2]
for o in prisutni:
    print(f"Ime: {o.ime}")
    print(f"Ime: {o.prezime}")

# metod je funkcija unutar klase
# polja klase
# 