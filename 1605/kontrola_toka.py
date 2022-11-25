import random
x = 10

if x> 0: 
    print("Broj x je pozitivan")

print("Izvrasava se u svakom slucaju")

vozilo_u_pokretu = True
brzina= 60
if vozilo_u_pokretu== True:
    print("Vozilo se krece")
    print("Proverite brzinu")
    if brzina >50:
        print("Prekoracena brzina")
    print("Ovo izvrsava bez obzira na brzinu")
    if brzina <= 50:
        print("brzina je okej")

if vozilo_u_pokretu == False:
    print("vozilo se ne krece")
proizvod = "duks"
cena = 3000

# komanda = int(input("Unesite komandu: "))
# if komanda == 1:
#     print("Prikazi proizvode")
#     print("Proivod:", proizvod, "Cena:", cena)
# if komanda == 2: 
#     print("Kupovina")
#     stanje = int(input("Unesite stanje na racunu: "))
#     if stanje >= cena: 
#         print("Uspesna kupovina!")
#     if stanje < cena:
#         print("Neuspesna kupovina")
# if komanda == 3: 
#     print("Izlaz")


broj = 5
if broj > 0:
    print("Broj je veci od 0")
else:
    print("Broj je 0 ili manji od 0")

marija = False
ksenija = True
katarina = False
devojka_na_dejtu = ""
if marija:
    devojka_na_dejtu= "marija:"
elif katarina:
    devojka_na_dejtu= "katarina"
elif ksenija:  
    devojka_na_dejtu = "ksenija" 
else:
    devojka_na_dejtu= "sofija:"
print("Izlazi sa mnnom:", devojka_na_dejtu)

automobil_polovan = False
godiste = 2021
boja = "crna"

if (automobil_polovan == True or godiste > 2017) and boja == "crna":
    print("Kupujem")

if not automobil_polovan:
        print("Automobil je nov")
prisutan = True # NIJE NA CASU
if prisutan:
    print("Na casu je")
if not prisutan:
    print("Nije na casu")

# trenutni_rezultat = random.randint(1,90)
# novi_rezultat = int(input("Unesite novi broj (od 1 do 90):")) 
# if novi_rezultat > 100 or novi_rezultat < 1:
#     print("Proverite bro, dozvoljeno od 1 do 90")
# elif trenutni_rezultat< novi_rezultat:
#     print("Pobedilo ste")
# else: 
#     if trenutni_rezultat < novi_rezultat:
#         print("Pobedili ste!")
#     elif trenutni_rezultat == novi_rezultat:
#         print("Identicne vrednosti")
#     else:
#         print("Izgubili ste")
# pol = input("Unesite pol")
# poruka = ""

# if pol == "m" :
#     print = "hello mister"
# else:
#     poruka = "Hey miss"
    
# poruka = "Hey mister" if pol == "m" else "hey miss"

popularan_prizvod = "ajvar" if "jesen" else "sladoled"
