































# --------------------------------

# def levi_klik():
#     print("Levi klik misa")
# def desni_klik():
#     print("Desni klik misa")



# def upotreba_aplikacije(klik):
#     print("Prikazujem UI")
#     print("Izvrsavam instrukciju")
#     klik()
#     print("Nastavljam da koristim program")


# ----------------------------------------

def rezervoar_lamica():
    print("Na rezervi ste")
    print("Zuta lampica")

import time
def vozi(gorivo, indikator_goriva):
    rezerva_limit = 10
    while gorivo >= 0:
        print("Voznja")
        time.sleep(1)
        gorivo -= 5
        if gorivo <= rezerva_limit:
            indikator_goriva()

vozi(40, rezervoar_lamica)
