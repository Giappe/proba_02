import socket

c = socket.socket()
c.connect(("gresnik.com",7880))

broj1 = 65
broj2 = 15
znak = "*"

poruka = f"{broj1}|{broj2}|{znak}\n"
c.send(poruka.encode()) # encode je poruka tipa string

odgovor = c.recv(512).decode().strip()
print(odgovor)