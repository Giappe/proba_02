import random

# #           0       1     2       3
# osoba = ["Sofija", 20, "plava", True]

# print(osoba)

# clanovi u sekvenci su indeksirani: 0 1 2 3 4

# print(osoba[0])
# print("Godine:", osoba [1])

# automobili = ["Opel", "Citroen", "Mercedes"]

# print(automobili [1])

# for x in range(5, 10, 2):
#     print(x)

#        #012345
# kurs = "python"
# print(kurs[2])
# print(kurs[5])
# print(kurs[4])
# print(kurs[1])
# print(kurs[0])

# duzina = len(kurs)
# print(duzina)

# ustanova = "IT Academy"

# for x in range(len(kurs)):
#     print("Na poziciji:", x, kurs[x])

# for index in range(len(ustanova)):
#     print(ustanova [index])


# primer = "zadatak1"

# # for slovo in range(len(primer)):
# #     print(primer[slovo])

# # for slovo in range(len(primer)):
# #     print(primer[slovo], end="")
# # print()

# broj_karaktera = len(primer)
# indeks = 0

# while indeks < broj_karaktera:
#     print(primer[indeks])
#     indeks += 1

# print(broj_karaktera)

'''
stringovi
'''

# korisnicko_ime = "admin"
# uneto_kor_ime = input("Unesi korisnicno ime:")

# if korisnicko_ime == uneto_kor_ime.lower():
#     print("Dobrodosli")
# else:
#     print("Pogresni podaci")



'''
liste
'''


# osoba = ["Sofija", 25, "plava", False]

# for x in range(len(osoba)):
#     print(osoba[x])

# for osobina in osoba:
#     print(osobina)


# voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]

# for stavka in voce_i_povrce:
#     print(stavka)

# for i in range(len(voce_i_povrce)):
#     print("Na indeksu:", i, "nalazi se", voce_i_povrce[i])


# automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Opel", "Opel"]

# for indeks, auto in enumerate(automobili):
#     if auto == "Opel":
#         print(indeks, auto)
#     #print("Pozicija:", indeks, "Marka:", auto)

# for indeks, auto in enumerate(automobili):
#     if len(auto) == 3:
#         print(auto)

# automobili.append("Mercedes")
# automobili[2] = "Opel Corsa"
# automobili[3] = "Kia Sportage"

# del automobili[3]
# automobili.remove("BMW")
# automobili.pop(0)

# print(automobili)

# broj_opela = 0
# for indeks in range(len(automobili)):
#     if automobili[indeks] == "Opel":
#         print("Evo ga Opel")
#         broj_opela += 1
# print("Imam", broj_opela, "na placu.")

# automobili.clear
# print(automobili)

# prazan_plac = []

'''
Slajsovi
'''

# #               1           2      3      4       5        6        7          8
# automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Peugeot", "Audi", "Mercedes"]

# automobili_akcija = []

# for i in range(len(automobili)):
#     if i == 1 or i == 2 or i == 3:
#         automobili_akcija.append(automobili[i])
# print(automobili_akcija)

# automobili_akcija = automobili [1:9:2]
# print(automobili_akcija)

# lista
# prazne liste, parni neparni
# for
# %
# if else

brojevi = [2, 4, 5, 9, 1, 0, 6, 8]

# parni = []
# neparni = []

# for broj in brojevi:
#     if broj % 2==0:
#         parni.append(broj)
#     else:
#         neparni.append(broj)
# print(parni, neparni)


# brojevi.sort()
# brojevi.reverse()
# print(brojevi)



