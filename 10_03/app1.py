import http.server as server
from urllib import parse

def proveri(uname,pwd):
    fajl = open("users.txt","r")
    while linija := fajl.readline():
        un,pw = linija.strip().split(",")
        if un == uname:
            if pwd == pw:
                return 0
            else:
                return -1
    else:
        return -2


class Hendler(server.SimpleHTTPRequestHandler):
    def do_POST(self):
        duzina = int(self.headers["Content-Lenght"])
        podaci = self.rfile.read(duzina)
        podaci = dict(parse.parse_qsl(podaci))
        res = proveri(podaci["username"],podaci["password"])
        if res == 0:
            self.wfile.write(b"HTTP/1. 200 OK\r\nContent-Type: text/html\r\n\r\nSve ok")
        elif res == -1:
            self.wfile.write(b"HTTP/1. 200 OK\r\nContent-Type: text/html\r\n\r\nNije ispravna lozinka")
        else:
            self.wfile.write(b"HTTP/1. 200 OK\r\nContent-Type: text/html\r\n\r\nNepostojeci korisnik")

server.HTTPServer(("0.0.0.0",8000), Hendler).serve_forever()
