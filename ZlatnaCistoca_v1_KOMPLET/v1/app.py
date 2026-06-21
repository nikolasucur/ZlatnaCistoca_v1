
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import sqlite3
from openpyxl import Workbook
from datetime import datetime

app = Flask(__name__)
app.secret_key = "zlatna_cistoca_secret"

DB = "zlatna_cistoca.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS zahtevi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ime TEXT,
        email TEXT,
        telefon TEXT,
        opis TEXT,
        status TEXT,
        datum TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posalji", methods=["POST"])
def posalji():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO zahtevi(ime,email,telefon,opis,status,datum) VALUES(?,?,?,?,?,?)",
        (
            request.form["ime"],
            request.form["email"],
            request.form["telefon"],
            request.form["opis"],
            "Novo",
            datetime.now().strftime("%d.%m.%Y %H:%M")
        )
    )
    conn.commit()
    conn.close()
    flash("Zahtev je uspešno sačuvan.")
    return redirect(url_for("index"))

@app.route("/admin")
def admin():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM zahtevi ORDER BY id DESC")
    zahtevi = cur.fetchall()
    conn.close()
    return render_template("admin.html", zahtevi=zahtevi)

@app.route("/excel")
def excel():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM zahtevi")
    rows = cur.fetchall()
    conn.close()

    wb = Workbook()
    ws = wb.active
    ws.append(["ID","Ime","Email","Telefon","Opis","Status","Datum"])

    for r in rows:
        ws.append(list(r))

    file = "zahtevi.xlsx"
    wb.save(file)
    return send_file(file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
