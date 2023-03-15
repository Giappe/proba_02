import mysql.connector as conn

konekcija = conn.connect(host="localhost",username="root",passwd="",database="telefoni_01")

cur = konekcija.cursor()
cur.execute("de si mysql serveru")

# deklarativni jezik je onaj kojim se izdaju komande u frontend-u, dok su imperativne u backend-u