import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

app = Flask(__name__)
app.secret_key = 'zlatna_cistoca_v1_secret_key_demo'

DB_NAME = 'zlatna_cistoca.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS odvoz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum TEXT NOT NULL,
            rejon TEXT NOT NULL,
            vrsta_otpada TEXT NOT NULL,
            kolicina_kg REAL NOT NULL,
            napomena TEXT,
            kreirano_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Inicijalizacija baze pri pokretanju
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dodaj', methods=['POST'])
def dodaj_unos():
    datum = request.form.get('datum')
    rejon = request.form.get('rejon')
    vrsta_otpada = request.form.get('vrsta_otpada')
    kolicina_str = request.form.get('kolicina_kg')
    napomena = request.form.get('napomena', '').strip()

    # Validacija polja
    if not datum or not rejon or not vrsta_otpada or not kolicina_str:
        flash('Molimo vas da popunite sva obavezna polja.', 'error')
        return redirect(url_for('index'))

    try:
        kolicina_kg = float(kolicina_str)
        if kolicina_kg <= 0:
            flash('Količina mora biti pozitivan broj.', 'error')
            return redirect(url_for('index'))
    except ValueError:
        flash('Količina mora biti ispravan broj (npr. 150 ili 12.5).', 'error')
        return redirect(url_for('index'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO odvoz (datum, rejon, vrsta_otpada, kolicina_kg, napomena)
        VALUES (?, ?, ?, ?, ?)
    ''', (datum, rejon, vrsta_otpada, kolicina_kg, napomena))
    conn.commit()
    conn.close()

    flash('Unos je uspešno sačuvan u bazi!', 'success')
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    conn = get_db_connection()
    unosi = conn.execute('SELECT * FROM odvoz ORDER BY datum DESC, id DESC').fetchall()
    
    # Statistika za admin dashboard
    total_kg = sum(u['kolicina_kg'] for u in unosi) if unosi else 0
    total_unosa = len(unosi)
    
    conn.close()
    return render_template('admin.html', unosi=unosi, total_kg=total_kg, total_unosa=total_unosa)

@app.route('/export/excel')
def export_excel():
    conn = get_db_connection()
    unosi = conn.execute('SELECT datum, rejon, vrsta_otpada, kolicina_kg, napomena FROM odvoz ORDER BY datum DESC').fetchall()
    conn.close()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Evidencija Odvoza"

    # Stilovi za profesionalan izgled
    header_fill = PatternFill(start_color="1E40AF", end_color="1E40AF", fill_type="solid") # Tamno plava
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    total_font = Font(name="Calibri", size=11, bold=True)
    border_thin = Border(
        left=Side(style='thin', color='D1D5DB'),
        right=Side(style='thin', color='D1D5DB'),
        top=Side(style='thin', color='D1D5DB'),
        bottom=Side(style='thin', color='D1D5DB')
    )

    headers = ["ID", "Datum odvoza", "Rejon / Lokacija", "Vrsta otpada", "Količina (kg)", "Napomena"]
    ws.append(headers)

    # Formatiranje zaglavlja
    for col_num in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_num)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Unos podataka
    total_kolicina = 0
    for idx, row in enumerate(unosi, start=1):
        total_kolicina += row['kolicina_kg']
        ws.append([idx, row['datum'], row['rejon'], row['vrsta_otpada'], row['kolicina_kg'], row['napomena']])
        
        row_num = idx + 1
        for col_num in range(1, len(headers) + 1):
            c = ws.cell(row=row_num, column=col_num)
            c.border = border_thin
            if col_num in [1, 2]:
                c.alignment = Alignment(horizontal="center")
            elif col_num == 5:
                c.alignment = Alignment(horizontal="right")
                c.number_format = '#,##0.00'

    # Dodavanje sumarnog reda na dnu
    total_row = len(unosi) + 2
    ws.cell(row=total_row, column=4, value="UKUPNO:").font = total_font
    ws.cell(row=total_row, column=4).alignment = Alignment(horizontal="right")
    
    total_cell = ws.cell(row=total_row, column=5, value=total_kolicina)
    total_cell.font = total_font
    total_cell.number_format = '#,##0.00'
    total_cell.alignment = Alignment(horizontal="right")

    # Automatsko prilagođavanje širine kolona
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

    filename = f"Zlatna_Cistoca_Izvestaj_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    file_path = os.path.join('/tmp', filename) if os.path.exists('/tmp') else filename
    wb.save(file_path)

    return send_file(file_path, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(debug=True)