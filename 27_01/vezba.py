import csv

fajl = open("korisnici.csv")
reader = csv.reader(fajl)

for red in reader:
    print(red)