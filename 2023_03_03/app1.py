import http.server as srv



class Rukovalac(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers

        parametri = self.path.split("?")[1]
        if len(parametri) > 1:
            parametri = dict(parse.parse_qsl(parametri))
            pid = parametri["id"]
            gitara = model[pid]
            izlaz = f"<h3>{gitara[naziv]}</h3><img width=200 src='{gitara['slika']}'/><br>'"
        
        izlaz = ""
        for kljuc, vrednost in model.items():
            izlaz += f"<a href+''>{vrednost['naziv']}</a><br>"
        
        self.wfile.write(izlaz.encode())

srv.HTTPServer(("0.0.0.0",8000),Rukovalac).serve_forever()