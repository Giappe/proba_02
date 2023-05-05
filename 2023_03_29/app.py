from flask import Flask
from flask import request
from mysql import connector as conn

app = Flask("Moja Web Aplikacija")
baza = conn.connect(host = "localhost",)

@app.route("/")
def login():
    if request.method.lower() == "get":
        formica = """
        <from method="post">
            Username: <br>
            <input type="text" name="username" /><br>
            PAssword: <br>
            <input type="text" name="pass" /><br>
            <input type="submit" value="login" />
            </form>

        """
        return formica
    else:
        username = request.from.get("username")
        password = request.from.get("pass")

        cur = baza.cursor()
        cur.execute()

        return f"{username} {password}"


app.run(debug=True)