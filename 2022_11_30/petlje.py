import random


# # x                   cilj
# pozicija_automobila = 0
# pozicija_cilja = 10

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)


# for ime in ["marko", "milos", "marija", "ana", "sofija"]:
#     print("Hello", ime)
# print("Prva sledeca linija...")

# for broj in [1, 2, 3, 4, 5]:
#     print("Ovo je broj: ", broj)


# for broj in range(5, 10, 2):
#     print("Stampanje broja", broj)

# for broj in range(100, 0, -5):
#     print("Prikaz", broj)


# pozicija_automobila = 0
# pozicija_cilja = 10

# for trenutna_pozicija in range(pozicija_cilja + 1):
#     pozicija_automobila = trenutna_pozicija
#     print(pozicija_automobila == pozicija_cilja)



# startDate = 2002
# endDate = 2022

# for godine in range(startDate, endDate, 5):
#     print("Dozvoljene godine: ", godine)


# for zvezda in range(100):
#     print("*", end="")


# \t je kao da pritisnem tab na tastaturi
# \n ce prebaciti u novi red

# print("Ovo je kurs \"Python\"")
# print("Ovo je deljenje, delim brojeve: a\\b") # backslash potire samog sebe i pojavljuje se u ovom primeru kao samo jedan \

# print("1\t2\t3\t")
# print("*********************")
# print(1*1, end="\t")
# print(1*2, end="\t")
# print(1*3)

# print(2*1, end="\t")
# print(2*2, end="\t")
# print(2*3)

# print(3*1, end="\t")
# print(3*2, end="\t")
# print(3*3)

# print("1\t2\t3\t")
# print("*********************")

# zeljeni_broj = int(input("Unesite broj: "))
# for brojac in range(1, zeljeni_broj +1):
#     print(brojac*1, end="\t")
#     print(brojac*2, end="\t")
#     print(brojac*3)


# for x in range(5):
#     for y in range(3):
#         print("Ovo je X: ", x, "Ovo je Y: ", y)


'''
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #

'''

# for x in range(6):
#     print("# " * 5, end="\n")


# for x in range(6):
#     print("Crtam visinu, sprat ", x)
#     for y in range(6):
#         print("*", end= " ")


# for x in range(6):
#     for y in range(6):
#         print("*", end= " ")
#     print()

# for x in range(6):
#     print(x, end=" ")
#     for y in range(6):
#         print("*", end= " ")
#     print()



# for x in range(6):
#     for y in range(6):
#         print("#", end=" ")
#     if x == y:
#         print("*")
#     else:
#         print("#", end=" ")
#     print()


# for x in range(6):
#     for y in range(6):
#         if x == y:
#             print("*", end=" ")
#         else:
#             print("#", end=" ")
#     print()


# print("*" if x == y else "#", end" ")


for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()


# sekunde = 10

# while sekunde > 0:
#     print(sekunde)
#     sekunde -= 1


# baterija = 100

# while baterija > 0:
#     print("Mozes koristiti telefon.", baterija, "%")
#     baterija -= random.randint(5, 10)

# print("Baterija je prazna.")

# for broj in range(11):
#     if broj == 5:
#         break
#     print(broj)

# for broj in range(11):
#     if broj == 2:
#         continue
#     print(broj)

