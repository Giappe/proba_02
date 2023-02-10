import socket

s = socket.socket()
s.connect(("jadnik.com", 7878))

s.send(b"Ko je najlepsi?")