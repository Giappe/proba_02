import socket

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9000))
partije = {
    "filip":"",
    "dovla":""
}

while True:
    paket,adresa = s.recvfrom(128)
    paket = paket.decode().strip().split("|")
    ime = paket[0]
    klik = paket[1]
    partije[ime] = klik
    izlaz = ""
    for k,p in partije.items():
        izlaz+=f"{k}:p|"
    izlaz = izlaz.rstrip("|")
    s.sendto(izlaz.encode(),adresa)
    print(paket,adresa)


# paket = s.recv(128)
# print(paket)