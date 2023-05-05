from django.http import HttpResponse
from django.shortcuts import render

def proba(request):
    odgovor = render(request,"proba.html")
    return odgovor

def naslovnastrana(request):
    odgovor = render(request,"index.html", {})
    return odgovor

def detalji(request):
    odgovor = HttpResponse("Pozdrav iz strane sa detaljima")
    return odgovor


# pitanja za framework engine-a
# kako se radi detekcija kolizije
# kako se pomeraju sprajtovi
# kako se krece

# baza, parametrizacija, upload, html 

