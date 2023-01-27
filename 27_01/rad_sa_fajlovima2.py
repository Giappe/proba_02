import csv

fajl = open("podaci2.csv")

reader = csv.reader(fajl)

broj_python_smer = 0

for red in reader:
    # for i in range(len(red)):
    #     if i == 2
    #     print(red[i])
    # if red[2] != None:
    #     if red[2] == "python":
    #         broj_python_smer += 1
    # if red[2] == "python":
    #     broj_python_smer += 1
    for podatak in red:
        if podatak.lower() == "python":
            broj_python_smer += 1

print(broj_python_smer)

