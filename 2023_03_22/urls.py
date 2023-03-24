from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

import mysql.connector as conn

konekcija = conn.connect(host="localhost",username="root",passwd="",database="albumi")

def naslovna(req):
    sesija = konekcija.cursor()
    upit = "select id,naziv,brojpesama,godina,zanr,slika from albumi"
    sesija.execute(upit)
    svi_redovi = sesija.fetchall()
    izlaz = ""
    for aid,naziv,pesama,godina,tip,slika in svi_redovi:
        izlaz += f"<div style='width:150px;float:left;border:1px solid black;height:200px;padding:10px;margin:10px;text-align:center;'><h3>{naziv}</h3><img src='{slika}' width=130 /></div>"
    #(1, 'Quest for Fire', 10, 2023, 'electronic')
    sesija.close()
    odgovor = HttpResponse(izlaz)
    return odgovor

def obrada(req):
    odgovor = HttpResponse("Hello man!!!")
    return odgovor

def pancevci(req):
    return HttpResponse("De ste pancevci!!!")

urlpatterns = [
    path('dota',obrada),
    path("pancevci",pancevci),
    path("",naslovna)
]
