import enum

# enumeracija

class TipoviSkolovanja(enum.Enum):
    ONLINE = 1
    TRADICIONALNO = 2

print(TipoviSkolovanja.ONLINE.value)
print(TipoviSkolovanja.TRADICIONALNO.name)


class Korisnik:
    def __init__ (self, ime, tipSkolovanja):
        self.ime = ime
        self.tipSkolovanja = tipSkolovanja

kor1 = Korisnik("Sofija", TipoviSkolovanja.ONLINE)
print(kor1.ime, kor1.tipSkolovanja.value)

class Pol(enum.Enum):
    MUSKI = "m"
    ZENSKI = "z"

odabran_pol = Pol.MUSKI
# odabran_pol -> name Muski value m
print(odabran_pol.value)

'''
POZADINA 000000
TASTER 150050
NAVIGACIJA 3F0071
FOOTER FB2576
'''
'<div style=""background-color: {POZADINA.value}"> SUBMIT </div>'

'''
LAKO green
SREDNJE orange
TESKO red
'''

# boje
# navigacija, main, footer

# Boja navigacije jeL #FFFFFF

class Boje(enum.Enum):
    NAVIGACIJA = "#FFEA20"
    MAIN = "#8DCBE6"
    FOOTER = "#9DF1DF"

print(Boje.NAVIGACIJA.value)
print(Boje.MAIN.value)
print(Boje.FOOTER.value)

class TipoviPlacanja(enum.Enum):
    KES = 1
    KARTICA = 2
    CEKOVI = 3

    def __str__ (self):
        return f"Naziv: {self.name}, vrednost: {self.value}"

print(TipoviPlacanja.KES)

for tip in TipoviPlacanja:
    print(tip)

odabrano = int(input("Odaberite tip placanja - Kes 1, Kartica 2, Cek 3: "))

for tip in TipoviPlacanja:
    if tip.value == odabrano:
        print(tip)