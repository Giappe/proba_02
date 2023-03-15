import csv

fajl = open("podaci2.csv", "r+") # ne znam zasto ne radi...
sadrzaj_fajla = fajl.read()
print(sadrzaj_fajla)

fajl.write("proba")

fajl.close()