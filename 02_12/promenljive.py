# broj_poena = 100 #int
# ime_i_prezime = "Predrag Sanader" #string
# plata = 999.99 #float
# zaposlen = True

# print(broj_poena, ime_i_prezime, plata, zaposlen)
# print()

# print(broj_poena); print(ime_i_prezime) # ; prebacuje u novi red
# print(plata)
# print(zaposlen)

# print("Broj poena: ",broj_poena)
# print("Ime zaposlenog", ime_i_prezime)
# print()

# model = "A51"
# proizvodjac = "Samsung"
# cena = 150.67
# dostupno = True

# print(model, proizvodjac, cena, dostupno)
# print()


# --------------------------------------------

# RPG igra:

# ime_igraca = "Stojan"
# health = 200
# mana = 50
# xp = 4200
# level = 5

# print("Ime igraca: ", ime_i_prezime)
# print("Health: ", health)
# print("Mana: ", mana)
# print("Experience: ", xp); print("Level: ", level)
# print()

# --------------------------------------------

# male/female

# print("Set your appearance")
# z = input("Male or female (male/female)?")
# if z=="male":
#     print("You choose male")
# else:
#     print("You choose female")
# print()

# -------------------------------------
# calc:

# print("Unesite prvi broj: ")
# x = int(input())
# print("Unesite drugi broj:")
# y = int(input())
# print("Rezultat je:", (x + y)) # sabiranje se vrsi u zagradama! Bez zagrada on samo pripoji jedan broj drugom, ne sabira ih
# print()

# ---------------------------------------
# Earth

# print("The earth was nearly wiped clean of life.")
# print("A great cleansing, an atomic spark struck by human hands, quickly raged out of control. Spears of nuclear fire rained from the skies.")
# print("Continents were swallowed in flames and fell beneath the boiling oceans. Humanity was almost extinguished, their spirits becoming part of the background radiation that blanketed the earth.")
# print()

# ---------------------------------------

# Setup

'''
One of the northern tribes claims they are descended from one such Vault. They hold that their founder and ancestor, one known as the "Vault Dweller," once saved the world from a great evil. According to their legend, this evil arose in the far south. It corrupted all it touched, twisting men inside, turning them into beasts. Only through the bravery of this Vault Dweller was the evil destroyed.
But in so doing, he lost many of his friends and suffered greatly, sacrificing much of himself to save the world. When at last he returned to the home he had fought so hard to protect, he was cast out. Exiled. In confronting that which they feared, he had become something else in their eyes...and no longer their champion.
'''
# print("Set your appearance")

# ---------------------------------------

# War:

# print("War. War never changes. The end of the world occurred pretty much as we had predicted. Too many humans, not enough space or resources to go around. The details are trivial and pointless, the reasons, as always, purely human ones.")

# ---------------------------------------

# Window:

# from tkinter import * 
# import tkinter.messagebox

# window = Tk()

# window.title("Hello Python!!!")
# window.resizable(False,False)
# window.geometry("%dx%d+%d+%d" % (600, 400, (window.winfo_screenwidth()/2)-300, window.winfo_screenheight()/2-200))

# lbl = Label(window, text="START GAME") 
# lbl.place(x=300, y=200, anchor="center")
# lbl.config(width=400)

# def start(event):
#     tkinter.messagebox.showwarning('Sorry bro!',"The game will start, as soon as you implement her",parent=window) 

# lbl.bind("<Button-1>", start)

# window.mainloop()
# ovaj kod sam sredio, ali mi ne importuje tkinter datoteku...

# ---------------------------------------

# Age:

# allowed_age = 13

# print("Unesite vase godine:")
# x = int(input())

# if x >= allowed_age:
#     print("Mozete pristupiti podacima!")
# else:
#     print("Nemate dovoljno godina, pristup zabranjen")
# if i else jos nismo radili u ovom trenutku, pa je resenje:

# allowed_age     = 13
# age             = int(input("Enter your age: "))
# print("Allowed - ", (allowed_age <= age))
# rezultat je ovde True ili False!

# ---------------------------------------

# username - password:

# db_username = "Peter"
# db_password = "123"

# username = input("Unesite korisnicko ime: ")
# password = input("Unesite lozinku: ")

# if db_username == username or db_password == password:
#     print(True)
# else:
#     print(False)
# print()

# ---------------------------------------

# menjacnica:

# eur = 1.3
# usd = 1.1

# svota = float(input("Unesite zeljenu svotu: "))

# print("Evro: ", (svota * eur))
# print("Dolar: ", (svota * usd))
# print()

# ---------------------------------------

# cena:

# porez = 1.2

# cena = float(input("Unesite cenu: "))
# print("Cena sa porezom je: ", (porez * cena))
# print()

# ---------------------------------------

# povrsina kruga:

# self note: operacija deljenja automatski pretvara broj u float!

# pi = 3.14

# precnik = float(input("Unesite precnik: "))
# print("Povrsina kruga je:", (pi * (precnik ** 2)))
# print()

# ---------------------------------------

# stao sam kod vezbe 5 ITA22PPFVM_3.pdf

