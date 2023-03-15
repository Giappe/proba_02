class WrongOperation(Exception):
    pass

def kalkulator(broj1, broj2, operacija):
    dostupne_operacije = ["+","-","*","/"]
    if operacija not in dostupne_operacije:
        raise WrongOperation
    else:
        if operacija == "+":
            print(int(broj1) + int(broj2))
        elif operacija == "-":
            print(broj1 - broj2)
        elif operacija == "*":
            print(broj1 * broj2)
        elif operacija == "/":
            print(broj1 / broj2)

try:
    kalkulator("a", "b", "+")
except WrongOperation:
    print("Pogresili ste operaciju")
except ZeroDivisionError:
    print("Ne mozete deliti sa nulom.")
except ValueError:
    print("Greska prilikom konverzije vrednosti.")
except Exception:
    print("Neka greska.")
        