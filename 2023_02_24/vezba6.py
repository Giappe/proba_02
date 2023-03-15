import http.server as server
import urllib.parse as parse

class Obrada(server.SimpleHTTPRequestHandler):
    def do_GET(self):

        parametri = self.path.split("?")[1]
        parametri = dict(parse.parse_qsl(parametri))

        a= int(parametri["a"])
        b=int(parametri["b"])
        c = a + b
        odgovor = f"Rezultat sabiranja {a} i {b} jednako je {c}"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(odgovor.encode())

server.SimpleHTTPRequestHandler(("0.0.0.0",8000),Obrada).serve_forever()