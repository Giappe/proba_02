# tip (string) broj korisnika (int) mockup (bool) preuzeta za rad

class Aplikacija:
    def __init__(self, tip, broj_korisnika, mockup, preuzeta_za_rad):
        self.tip = tip
        self.broj_korisnika = broj_korisnika
        self.mockup = mockup
        self.preuzeta_za_rad = preuzeta_za_rad

app1 = Aplikacija("Webb app", 1000, True, False )
app2 = Aplikacija("iOS app", 1500, False, False)
app3 = Aplikacija("Android app", 2000, True, False)

class Firma:
    def __init__(self, naziv, broj_zaposlenih, registrovana = False):
        self.naziv = naziv
        self.broj_zaposlenih = broj_zaposlenih
        self.registrovana = registrovana
    
    def zaposli_nove(self, broj_novih):
        if broj_novih <= 0:
            print("prosledite broj veci od 0")
        else:
            self.broj_zaposlenih += broj_novih
            print(f"Zaposleno je novih {broj_novih}, trenutni broj je {self.broj_zaposlenih}")
    
    # def daj_otkaze(self, broj_otkazanih):
    #     if broj_otkazanih > self.broj_zaposlenih:
    #         print("Previse za otpustanje")
    #     else:
    #         if broj_otkazanih > 0:
    #             self.broj_zaposlenih -= broj_otkazanih
    #         else:
    #             print("Proverite broj, mora biti veci od 0")
    #             print(f"Otkazano je: {broj_otkazanih}, preostalih radnika je {self.broj_zaposlenih}")

    def daj_otkaze(self, broj_otkazanih):
        if broj_otkazanih > self.broj_zaposlenih or broj_otkazanih < 0:
            print("Previse za otpustanje")
        else:
            self.broj_zaposlenih -= broj_otkazanih
            print(f"Otkazano je: {broj_otkazanih}, preostalih radnika je {self.broj_zaposlenih}")


moja_firma = Firma("IT Akademija", 300, True)
moja_firma.zaposli_nove(10)
print(moja_firma.broj_zaposlenih)

moja_firma.daj_otkaze(20)
print(moja_firma.broj_zaposlenih)