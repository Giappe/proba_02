import re

# sablon = re.compile("ita") # sablon - sta ocekujem ili sta pretrazujem
# tekst_za_proveru = "korisnicko ime korisnika pocinje sa ita." # predmet provere

# print(sablon.search(tekst_za_proveru))
# print(sablon.findall(tekst_za_proveru))
# print(sablon.match(tekst_za_proveru))

# if sablon.search(tekst_za_proveru):
#     print("Nadjeno")
# else:
#     print("Nema sadrzaja")


# --------------------------------------------------------------

sablon = re.compile("[a-zA-Z0-9]")
tekst_za_proveru = "123"

if sablon.search(tekst_za_proveru):
    print("Poseduje slova ili brojeve")
else:
    print("Ne poseduje slova, ni brojeve")

# --------------------------------------------------------------

#1234567891011 - mora da ima 13 BROJEVA

iskaz = re.compile("[0-9]{13}")
jmbg = "1234567891011"

if sablon.search(tekst_za_proveru):
    print("OK je")
else:
    print("Proverite JMBG")