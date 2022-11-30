brojevi = [2, 4, 5, 9, 1, 0, 6, 8]

sortirani_brojevi = [2, 4, 5, 9, 1, 0, 6, 8]

#BUBBLE SORT#

# for i in range(1, len(brojevi)):
#     print(brojevi[i], "poredim sa", brojevi[i-1])

# while True:
#     izvrsena_zamena = False
#     for i in range(1, len(brojevi)):
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break
# print(brojevi)


#zadatak:
# products = ["iPhone", "TV", "Computer"]
# price = [100, 200, 300]

'''
# for x in range(len(products)):
#     for y in range(len(price)):
#         if products[x] == price[y]:
#             print("Proizvod:", x, "Cena:", y, end="")
#     print()

NEMAM POJMA OVO!!!
'''

#resenje:

# for i in range(len(products)):
#     print(products[i], price[i])


#zadatak
#automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugeot"]

# Automobil: ...
# 
# for i in range(len(automobili)):
    # if i == 3:
        # print("Aleksandra vozi utomobil:", automobili[i])
# 



# VISEDIMENZIONE LISTE

# proizvodi = ["iphone 11", "samsung s22", "xiaomi x3", "acet", "macbook", "lenovo"]

# proizvodi = [
#                 ["iphone 11", "samsung s22", "xiaomi x3"],
#                 ["acet", "macbook", "lenovo"],
#                 ["ipad", "samsung galaxy tab", "xiaomi tablet"]
#             ]

# telefoni = ["iphone 11", "samsung s22", "xiaomi x3"]
# laptopovi = ["acer", "macbook", "lenovo"]
# tableti = ["ipad", "samsung galaxy tab", "xiaomi tablet"]

# print(proizvodi[0][2])
# print(proizvodi[1][1])

# for i in range(len(proizvodi)):
#     print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print(proizvodi[i][j])


# hrana = [
#             ["cokolada", "bombone", "palacinke"],
#             ["sarma", "musaka", "kiseli kupus"],
#             ["pecena paptika", "ajvar", "sopska"]

#         ]

# for kategorija in hrana:
#     for jelo in kategorija:
#         print(jelo)



#Formatirani stringovi!
# a = 10
# b = 5

# sabiranje = f"Sabiranje brojeva {a} i {b} je {a + b}"
# print(sabiranje)



# biblioteka = [
#               ["uvod u pajton", "nepoznat autor", 123]
#               ["uvod u racunare", "aleksandra lazarevic", 321]
#              ]

# biblioteka = []
# while True:
#     print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
#     komanda = int(input("Unesite komandu: "))

#     if komanda == 1:
#         naslov = input("Unesite naslov: ")
#         autor = input("Unesite autora: ")
#         isbn = int(input("Unesite isbn: "))
#         biblioteka.append([naslov, autor, isbn])
#         print("Dodata knjiga")
#     if komanda == 2:
#         for knjiga in biblioteka:
#             for detalj in knjiga:
#                 print(detalj)
#     if komanda == 3:
#         kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem: ")
#         for knjiga in biblioteka:
#             for detalj in knjiga:
#                 if detalj == kljucna_rec:
#                     biblioteka.remove(knjiga)
#                     print("Knjiga je obrisana.")
#     if komanda > 3:
#         break



# TUPLE
# osoba = ("sofija", 25, "python")
# print(osoba[0])

# ime, godine, smer = osoba
# print(osoba)


