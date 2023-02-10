import socket

s = socket.socket()
s.bind(("0.0.0.0",9000))
s.listen()


c,a = s.accept()
fajl = open("dota.txt", "r")