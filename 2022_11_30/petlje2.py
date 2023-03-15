# for x in range(1, 7):
#     for y in range(6):
#         print("#", end="")
#     print()

# for x in range(10):
#     for y in range(10):
#         if x <= y:
#              print("#", end="")
#         else:
#              print(" ", end="")
#     print()



automobil = 0
cilj = 100

brzina = 10
gorivo = 40

while automobil < cilj:
    print("voznja je u toku")
    automobil += brzina
    gorivo -= 5
    if gorivo == 0:
        print("Cao")
        break
else:
    print("Stigli ste na cilj")