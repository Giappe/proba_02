
#digitron:

# def digitron(broj1, broj2, operacija):
#     if operacija == "+":
#         print(broj1 + broj2)
#         return broj1 + broj2
#     elif operacija == "-":
#         print(broj1 - broj2)
#         return broj1 - broj2
#     elif operacija == "*":
#         print(broj1 * broj2)
#         return broj1 * broj2
#     elif operacija == "/":
#         print(broj1 / broj2)
#         return broj1 / broj2
#     else:
#         print("Pogresna operacija")

# rezultat = digitron(10, 5, "+")
# # rezultat_sabiranja
# # povratna vrednost!
# print(rezultat)
# brojevi = [1, 2, 3]
# broj_clanova = (len(brojevi)) #funkcija len daje povrtnu vrednost koju kada pozovem dobijemo neki rezultat

# print(broj_clanova)

# "return" napusta funkciju, "break" napusta petlju, "exit" je samo izlazak bez icega

# rezultat_oduzimanja = digitron(10, 5, "-")
# print(rezultat_oduzimanja)

#----------------------------------------------------------------------------------

# ime = input("Unesite ime: ")
# prezime = input("Unesite prezime: ")
# godina = input("Godina (21, 22, 23...): ")

# korisnicno_ime = ""

# def kreiraj_kor_ime(ime, prezime, godina):
#     kor_ime = f"ita{godina}.{ime.lower()}{prezime.lower()}"
#     print("Uspesno kreirano korisnicko ime!")
#     return kor_ime

#funkcija stringa ima tacku, funkciju i zagrade "ime.lower()", string "ime" je vlasnik funkcije .lower()

# korisnicno_ime = kreiraj_kor_ime(ime, prezime, godina)
# print("Prikupljeni podaci o korisniku:")
# print(ime, prezime, korisnicno_ime)

# funkcija - menjacnica
# parametar - eur
# POVRATNA VREDNOST: rezultat u dinarima

# def menjacnica(eur):
#     dinari = eur * 118
#     return dinari

# dobijeni_dinari = menjacnica(int(input("Unesite vrednost u evrima: ")))
# print("Rezultat:", dobijeni_dinari)

#svaka funkcija treba da ima svoj ulazni karakter, da bi dobili povratnu vrednost

#--------------------------------------------------------------------------------------

# registracija
# licna karta, cist automobil, saobracajnu
# registrovana kola "Uspesno!", "Neuspesno, dodjite opet!"

# def registracija(licna_karta, cist_auto, saobracajna):
#     if cist_auto == False:
#         return "Neuspesno, dodjite opet!"
#     if licna_karta == False:
#         return "Neuspesno, dodjite opet!"
#     if saobracajna == False:
#         return "Neuspesno, dodjite opet!"
    
#     return "Uspesno!"

# skracena verzija:
# def registracija(licna_karta, cist_auto, saobracajna):
#     if cist_auto == False or licna_karta == False or saobracajna == False:
#         return "Neuspesno, dodjite opet!"
#     else:
#         return "Uspesno!"


# print(registracija(True, True, False))

# funkcija - bankomat
# paramertri - stanje, zeljeni_iznos
# stanje >= zeljeni zinos -> "Uspesno izvrseno, stanje: ???"
# -> Neuspesno! stanje: ???


#----------------------------------------------------------------
# moj pokusaj:
# stanje = 25000
# zeljeni_iznos = int(input("Unesite zeljeni iznos:"))

# def bankomat(stanje):
#     if stanje >= zeljeni_iznos:
#         print("Uspesno izvrseno, stanje:")
#         return stanje
#     else:
#         print("Neuspesno, stanje:", stanje)

# print(bankomat(zeljeni_iznos))


# resenje:

# def bankomat(stanje, zeljeni_iznos):
#     if stanje >= zeljeni_iznos:
#         return f"Uspesno!!! Novo stanje je: {stanje - zeljeni_iznos}"
#     else:
#         return "Neuspesno!"
    
# print(bankomat(500, 200))
# rezultat = bankomat(100, 80)
# print(rezultat)

#-----------------------------------------------------------------------

# slova = "asf57"
# for slovo in slova:
#     if slovo.isnumeric():
#         print("Sadrzi brojeve")

#-----------------------------------------------------------

# jedna * je tuple, dve ** su recnik(dictionary)

# def registracija(*dokumenti):
#     print("Doneli ste dokumenta:")
#     print(dokumenti)
#     print(dokumenti[0])
#     print(type(dokumenti))

# registracija("vozacka dozvola", "obavio tehnicki pregled", "licna karta")

# # --------------------------------------------------------------------------

# def upis(**podaci):
#     print("Uneli ste podatke")
#     print(podaci["ime"])
#     print(type(podaci))

# upis(ime="Pedja", prezime="Sanader", godiste=1983, ustanova="Filip Visnjic")

# # ----------------------------------------------------------------------
# def skolovanje(predavac_predaje):
#     print("Skolska godina je u toku...")
#     print("Ucionica A22")
#     # Odavde nastupa predavac
#     predavac_predaje()

# def predavac_vm():
#     print("Uvod u mreze")
#     print("Danas radimo novu temu")
#     print("Da li ste igrali lol ili dotu")

# def predavac_al():
#     print("Opet imamo predavanje sredom")
#     print("radimo funkcije")

# def predavac_vn():
#     print("Krecemo sa kursom HTML i CSS")

# skolovanje(predavac_al)

# -------------------------------------------------------------------------

# def priprema_obroka(spremanje):
#     print("Dolazak u kuhinju")
#     print("Perem ruke")
#     spremanje()

# def dorucak():
#     print("Idem po burek")
#     print("To je to od kuvanja")

# def rucak():
#     print("Pohovanje")
#     print("Restovan krompir")

# def vecera():
#     print("Tuna salata")
#     print("Sladoled")

# priprema_obroka(dorucak)

# pozivanje jedne od funkcija (dorucak, rucak, vecera) se nadovezuje na osnovnu funkciju "priprema_obroka". To se radi zbog toga da se ne bi komplikovao kod i rucno menjao ishod
# --------------------------------------------------------------------------------------------

# funkcija: lambda

# res = lambda a, b: a + b
# res(10, 5)

#jednolinijska funkcija koja nije imenovana, definise se u jednoj linij koda i koristi se da skratimo vreme, ono sto je definisano je povratna informacija

# ----------------------------------------------------------------------------------------

# Rekurzivna funkcija, mozemo doci u mrtvu petlju, funkcija koja u svom telu poziva samu sebe

# def tajmer(sekunde):
#     print(sekunde)
#     sekunde -= 1
#     if sekunde > 0:
#         tajmer(sekunde)


# tajmer(60)

# ---------------------------------------------------------------------------

# Dekoratori

def provera(funkcija):
    def unutrasnja_funkcija(a, b):
        if b == 0:
            print("Nije dozvoljeno deljenje sa nulom")
            return
        funkcija()
    return unutrasnja_funkcija


@provera

def deljenje(a, b):
    print(a/b)

deljenje(10, 5)


# ---------------------------------------------------------------------------

# Generatori:
# omogucava parcijalno, sekvencijalno izvrsavanje delova funkcije
# yield

def brojevi():
    yield 1
    yield 2
    yield 3

dobijeni_broj = brojevi()
print(dobijeni_broj)
print(next(dobijeni_broj))
print(next(dobijeni_broj))
print(next(dobijeni_broj))

for broj in brojevi():
    print(broj)