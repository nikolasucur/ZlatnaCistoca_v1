[README.md](https://github.com/user-attachments/files/34490642/README.md)
# 🟢 Zlatna Čistoća – v1.0

> **Web aplikacija za komunalna preduzeća** – prijem zahteva građana, upravljanje evidencijom i Excel izvoz podataka.

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x%2B-lightgrey)
![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red)

---

## 📋 O projektu

**Zlatna Čistoća v1** je prva verzija poslovnog softvera namenjenog komunalnim preduzećima i servisima za odvoz i reciklažu otpada.

### Funkcionalnosti:
- 📝 **Online forma** za podnošenje zahteva građana (ime, email, telefon, opis)
- 🗄️ **SQLite baza podataka** – automatsko čuvanje svih zahteva
- 🖥️ **Admin panel** – pregled svih pristiglih zahteva
- 📊 **Excel izvoz** – preuzimanje kompletne evidencije u `.xlsx` formatu
- ⚡ Flash notifikacije o uspešnom slanju zahteva

---

## 🛠️ Tehnologije

| Tehnologija | Uloga |
|---|---|
| Python 3 | Backend jezik |
| Flask | Web framework |
| SQLite | Baza podataka |
| openpyxl | Excel generisanje |
| HTML/CSS | Frontend |

---

## 🚀 Pokretanje projekta

### Preduslovi
- Python 3.8+
- pip

### Instalacija

```bash
# 1. Kloniraj repozitorijum
git clone https://github.com/tvoj-username/zlatna-cistoca-v1.git
cd zlatna-cistoca-v1

# 2. Instaliraj zavisnosti
pip install -r requirements.txt

# 3. Pokreni aplikaciju
python app.py
```

### Pristup aplikaciji
- **Korisnički interfejs:** http://127.0.0.1:5000
- **Admin panel:** http://127.0.0.1:5000/admin
- **Excel izvoz:** http://127.0.0.1:5000/excel

---

## 📁 Struktura projekta

```
zlatna_cistoca_v1/
│
├── app.py                  # Glavni Flask server
├── requirements.txt        # Python zavisnosti
├── zlatna_cistoca.db       # SQLite baza (auto-generiše se)
│
├── templates/
│   ├── index.html          # Korisnička stranica sa formom
│   └── admin.html          # Admin panel
│
└── static/
    └── css/
        └── style.css       # Stilovi
```

---

## 💼 Kupovina licence

Ova aplikacija je **komercijalni softver** u razvoju.  
Kod je javno dostupan isključivo u svrhu **evaluacije i prezentacije**.

Za kupovinu licence ili prilagođavanje vašim potrebama:

📧 **rfs.srbija@gmail.com**

---

## 🤝 Saradnja na razvoju

Tražimo developere koji žele da doprinesu razvoju projekta!

Ako si zainteresovan/a za saradnju:
1. Pogledaj otvorene zadatke u [Issues](../../issues) tabu
2. Pročitaj [CONTRIBUTING.md](CONTRIBUTING.md)
3. Javi se na **rfs.srbija@gmail.com**

---

## 🗺️ Roadmap

- [x] Osnovna forma za zahteve
- [x] SQLite baza podataka
- [x] Admin panel
- [x] Excel izvoz
- [ ] Autentifikacija za admin panel
- [ ] Email notifikacije
- [ ] Mobilni dizajn (responsive)
- [ ] REST API
- [ ] Prebacivanje na PostgreSQL

---

## ⚖️ Licenca

Copyright © 2026 RFS Srbija | rfs.srbija@gmail.com  
Sva prava zadržana. Pogledaj [LICENSE](LICENSE) fajl za detalje.
