import http.server as server

class ObradaZahteva(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        sadrzaj = "Pozdrav!!!"

        sadrzaj = open("dovla.html","r").read()

        self.wfile.write(f"HTTP/1.1 200\r\nfsadsf: sdasda\r\nsdafds: asdadsd\r\n\r\nPozdrav i tebi!!!\r\n\{sadrzaj}".encode())
        print("Hello")

s = server.HTTPServer(("0.0.0.0",8000),ObradaZahteva)
s.serve_forever()
