import re

# 3 mala slova, 3 broja, tacka, mala slova (jedno ili vise)
# ita22.proba

# sablon = re.compile("^[a-z]{3}[0-9]{2}\.[a-z]+$")
# proba = "ita22.proba"

# if sablon.search(proba):
#     print("OK")
# else:
#     print("Nije u redu kor ime")

# proba.probic2020@gmail.com
# sablon = re.compile("^[a-zA-Z0-9.]+\.+[a-zA-Z0-9]+[0-9]{4}+@+[a-zA-Z0-9]+\.+[a-zA-Z.]+$")
# proba = "proba.probic2020@gmail.com"

# if sablon.search(proba):
#     print("OK")
# else:
#     print("Nije taj mejl")

# -------------------------------------------------------------

# brojevi = [1, 3, 5]
# try:
#     print(brojevi[6])
#     print("Ispisan broj")
# except:
#     print("Doslo je do neke greske")

# print("Nastavak programa")
# print("Kraj programa")

# -------------------------------------------------------------

# uzimam od korisnika 2 broja
# delim ih

# try:
#     # pokusaj izvrsavanja
#     prvi_broj = int(input("Prvi broj: ")) # rizicno
#     drugi_broj = int(input("Drugi broj: ")) # rizicno

#     print("Deljenje:")
#     print(prvi_broj/drugi_broj)
#     print("Rezultat je: ", prvi_broj / drugi_broj)
# except:
#     # obrada greske - izuzetka
#     print("Doslo je do greske, uhvacen je izuzetak")

def deljenje(a, b):
    if a > 5:
        print(a/b)
    else:
        raise Exception("a mora biti vece od 5")

try:
    deljenje(3, 2)
except Exception as ex:
    print(ex)

# except ZeroDivisionError as greska1: # hvata izuzetak samo za deljenje sa nulom
#     print(greska1)
# except ValueError as greska2:
#     print(greska2)
#     print("Ne mozete uneti tekst u broj")
# except Exception as greska3:
#     print(greska3)
#     print("Izgleda da je neka durga greska")