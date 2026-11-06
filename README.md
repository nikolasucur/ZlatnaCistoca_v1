# ♻️ Zlatna Čistoća (v1)

> Moderan web sistem za komunalna preduzeća i operatere upravljanja otpadom, kreiran sa ciljem digitalizacije evidencije reciklaže i terenskog odvoza.

[![Flask](https://img.shields.io/badge/Flask-Framework-black.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-blue.svg)](https://www.sqlite.org/)
[![openpyxl](https://img.shields.io/badge/Export-Excel%20openpyxl-green.svg)](https://openpyxl.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 O projektu

**Zlatna Čistoća** je namensko softversko rešenje prilagođeno potrebama komunalnih preduzeća i privatnih operatera za sakupljanje i reciklažu otpada. Aplikacija premošćuje jaz između terenskih podataka i administrativne obrade, obezbeđujući pouzdano čuvanje podataka, sigurne forme za unos i brzu generaciju zvaničnih izveštaja.

Prva verzija (**V1**) fokusirana je na stabilan backend, jednostavnost korišćenja bez obuke zaposlenih i trenutni izvoz podataka u tabelarni format.

---

## 📸 Prikaz aplikacije

### Admin Dashboard i Statistika
![Admin Dashboard](screenshots/admin-dashboard.png)

### Unos novog odvoza sa terena
![Forma za unos](screenshots/form-input.png)

### Automatski generisan Excel izveštaj
![Excel Izveštaj](screenshots/excel-report.png)

---

## ✨ Ključne funkcionalnosti (V1)

* **📝 Interaktivni unos sa terena:** Intuitivne web forme za evidentiranje datuma, rejona, vrste otpada (PET, papir, staklo, metal, komunalni otpad) i količine u kilogramima.
* **🛡️ Robustna validacija i obaveštenja:** Zaštita od pogrešnih unosa uz vizuelne povratne informacije (flash poruke) za korisnika.
* **🗄️ Relaciona baza podataka:** Pouzdano skladištenje podataka u lokalnoj **SQLite** bazi sa automatskom inicijalizacijom.
* **📊 Profesionalni Excel Export:** Generisanje uredno formatiranih Excel izveštaja jednim klikom, sa prilagođenim zaglavljima, automatskim širinama kolona i sračunatim ukupnim količinama (sumarnom linijom).
* **📈 Admin Dashboard:** Centralni pregled istorije odvoza, ukupnog broja unosa i ukupne mase odvezenog otpada.

---

## 🛠️ Korišćene tehnologije

* **Backend:** Python, Flask
* **Baza podataka:** SQLite3
* **Obrada i izvoz podataka:** OpenPyXL
* **Frontend:** HTML5, CSS3 (Responsive dizajn)

---

## 🚀 Pokretanje projekta (Installation)

Slede koraci za brzo lokalno pokretanje aplikacije u razvojne svrhe:

1. Klonirajte repozitorijum:
   ```bash
   git clone https://github.com/nikolasucur/ZlatnaCistoca_v1.git
   ```
2. Idite u direktorijum projekta:
   ```bash
   cd ZlatnaCistoca_v1
   ```
3. Instalirajte potrebne zavisnosti:
   ```bash
   pip install -r requirements.txt
   ```
4. Pokrenite aplikaciju:
   ```bash
   python app.py
   ```
5. Otvorite pretraživač i posetite: `http://127.0.0.1:5000`

---

## 📄 Licenca

Projekat je razvijen kao vlasničko rešenje / portfolio prezentacija.
