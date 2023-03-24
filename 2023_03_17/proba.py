# import urllib.parse

import pomoc
from string import Template

tekst = "<h3>$ime je najjaci student</h3>"

sablon = Template(tekst)

tekst = sablon.substitute({"[ime]":"Djape"})

print(tekst)

# k,v,p = pomoc.parsiraj_putanju("/dovla/is?hello=world")

# class A:
#     x = 10

# obj = A()
# b = input("Unesi polje: ")


# import model
# svi = model.svipodaci()

# print(svi)
# jedan = model.podatak("5")
# print(jedan)
# model.dodaj("Dovla",10,"nema")
# svi = model.svipodaci()
# print(svi)

# putanja = "/shop/products?dovla=ricma"
# putanja = putanja.lstrip("/") #shop/products
# putanja_i_parametri = putanja.split("?")
# putanja = putanja_i_parametri[0]
# putanja_delovi = putanja.split("/") #['shop','products']

# broj_delova_putanje = len(putanja_delovi)

# kontroler = "mojkontroler"
# funkcionalnost = "mojafunkcionalnost"

# if broj_delova_putanje == 2:
#     kotroler = putanja_delovi[0]
#     funkcionalnost = putanja_delovi[1]
# elif broj_delova_putanje == 1 and putanja_delovi[0]:
#     kontroler = putanja [0]

# parametri = {}
# if len(putanja_i_parametri) == 2:
#     parametri = dict(urllib.parse.parse_qsl(putanja_i_parametri[1]))

# print(kotroler,funkcionalnost)

