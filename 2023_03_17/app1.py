import pomoc
import http.server as server
import importlib

class Hendler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        modeul,funkcija,p = pomoc.parsiraj_putanju(self.path)
        m = importlib.import_module(f"kontroleri.{modul}")
        f = getattr(m,funkcija)
        izlaz = f(p)
        self.send_response(200)
        self.send_response