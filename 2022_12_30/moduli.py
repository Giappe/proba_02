import os
import time

print(os.cpu_count())
# os.system('clear')

import sys

print(sys.platform)

# vreme = int(input())

# for vrednost in range(vreme):
#     while vrednost <= 0:
#         print(f"preostalo je: ", vrednost)
#         vreme -= 1
#         time.sleep(1)
#     else:
#         print("Cao")


# ----------------------------------------------------------
# zadatak:

# poruka = input("Unesite poruku: ")
# broj_sekundi = int(input("Unesite broj sekundi: "))

# while broj_sekundi > 0:
#     print(f"Preosatalo je: {broj_sekundi}")
#     broj_sekundi -= 1
#     time.sleep(1)

# for i in range(10):
#     print(poruka)

# -----------------------------------------------------------

print(time.time())

vreme = time.gmtime()
print(vreme.tm_wday)
print(vreme.tm_year)

datum = time.localtime()
print(time.strftime("Mesec: %m, Godina: %Y, Dan u nedelji: %w", datum))

kor = "ita22.proba"
novi_kor = kor.replace("22", "23")
print(novi_kor)

prisutni = "nikola,nemanja,jovan,dragan"
spisak = prisutni.split(",")
print(spisak)