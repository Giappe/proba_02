import model

def index(params={}):
    a = int(params=["a"])
    b = int(params=["b"])
    return f"rezultat {a+b}"

def proba(params={}):
    izlaz = ""
    karakteri = model.svipodaci()
    for k,v in karakteri.items():
        izlaz += f"<a href='/nikola/detalji?id={k}'><div style='background-color:red;padding:4px;margin:4px;color:white;'>{v['ime']}</div></a>"
    return izlaz

def detalji(params={}):
    karakter = model.podatak(params["id"])
    izlaz = "Podaci o karakteru su: <br>"
    izlaz += f"Ime: {karakter['ime']}<br>"
    izlaz += f"Popularnost: {karakter['popularnost']}<br>"
    izlaz += f"Ime: {karakter['']}<br>"
    izlaz += f"Ime: {karakter['']}<br>"