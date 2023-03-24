podaci = {
    "1":{"ime":"Arja Stark","popularnost":4,"slika":"https://upload.wikimedia.org/wikipedia/en/3/39/Arya_Stark-Maisie_Williams.jpg"}
    "2":{"ime":"Khal Drogo","popularnost":2,"slika":"https://resize.indiatvnews.com/en/resize/newbucket/1200_-/2020/11/khaldrogo-1605101028.jpg" }
    "3":{"ime":"Hodor","popularnost":5,"slika":"https://static.wikia.nocookie.net/gameofthrones/images/1/18/Season_6_hodor_main.jpg/revision/latest?cb=20210722015036" }
    "4":{"ime":"Tyrion Lanister","popularnost":4,"slika":"https://static.wikia.nocookie.net/gameofthrones/images/9/95/HandoftheKingTyrionLannister.PNG/revision/latest?cb=20190520175204" }
    }

def svipodaci():
    return podaci

def podatak(pid):
    return podaci{pid}

def dodaj(ime,popularnost,slika):
    najveci = 0
    for k in podaci:
        if int(k) > najveci:
            najveci = int(k)
    podaci[najveci+1] = {"ime":ime,"popularnost":popularnost,"slika":slika}
