from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)
#Koneksi ke database
app.secret_key = 'test'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'uts_python'
mysql = MySQL(app)

now = datetime.datetime.now()

@app.route('/')
def home():
    return render_template('index.html')

#proses input peminjaman buku oleh mhs
@app.route('/', methods=['POST'])
def mahasiswaInsert():
    if request.method == 'POST':
        KodeBuku = request.form['kodeBuku']
        nim = request.form['nim']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tpinjam (KodePinjam, KodeBuku, NIM, TglPinjam) VALUES (%s, %s, %s, %s)",
                    ('', KodeBuku, nim, now))
        mysql.connection.commit()
        return redirect(url_for('home'))
        
#Read data mahasiswa
@app.route('/admin')
def mahasiswaTampilData():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tanggota ORDER BY NIM ASC")
    datatampil = cur.fetchall()
    cur.close()
    return render_template('mahasiswa.html', datapemesan=datatampil)

#proses delete data mhs
@app.route('/hapusmahasiswa/<int:nim>', methods=["GET"])
def deleteMahasiswa(nim):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tanggota WHERE NIM=%s", (nim,))
    mysql.connection.commit()
    flash("data Berhasil di Hapus")
    return redirect( url_for('mahasiswaTampilData'))

#Read data buku
@app.route('/buku')
def dataBuku():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbuku ORDER BY Judul ASC")
    datatampil = cur.fetchall()
    cur.close()
    return render_template('books.html', datapemesan=datatampil)

#proses delete data buku
@app.route('/hapusbuku/<int:kodeBuku>', methods=["GET"])
def deleteBooks(kodeBuku):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbuku WHERE KodeBuku=%s", (kodeBuku,))
    mysql.connection.commit()
    flash("data Berhasil di Hapus")
    return redirect( url_for('dataBuku'))
    
#Read data pengembalian
@app.route('/pengembalian')
def dataPengembalian():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tkembali ORDER BY NIM ASC")
    datatampil = cur.fetchall()
    cur.close()
    return render_template('pengembalian.html', datapemesan=datatampil)

#proses delete data pengembalian
@app.route('/hapuspengembalian/<int:kodeKembali>', methods=["GET"])
def deletePengembalian(kodeKembali):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tkembali WHERE KodeKembali=%s", (kodeKembali,))
    mysql.connection.commit()
    flash("data Berhasil di Hapus")
    return redirect( url_for('dataPengembalian'))

#Read data peminjaman
@app.route('/peminjaman')
def dataPeminjaman():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tpinjam ORDER BY NIM ASC")
    datatampil = cur.fetchall()
    cur.close()
    return render_template('peminjaman.html', datapemesan=datatampil)

#proses delete data peminjaman
@app.route('/hapuspeminjaman/<int:kodePeminjaman>', methods=["GET"])
def deletePeminjaman(kodePeminjaman):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tpinjam WHERE kodePinjam=%s", (kodePeminjaman,))
    mysql.connection.commit()
    flash("data Berhasil di Hapus")
    return redirect( url_for('dataPeminjaman'))

#proses update data mhs
@app.route('/updatemahasiswa', methods=['POST'])
def updateMahasiswa():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['NamaMhs']
        jurusan = request.form['Jurusan']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE tanggota SET NamaMhs=%s, Jurusan=%s WHERE NIM=%s", (nama, jurusan, nim))
        mysql.connection.commit()
        flash("Data Berhasil di Update")
        return redirect(url_for('mahasiswaTampilData'))

#proses update data buku
@app.route('/updatebuku', methods=['POST'])
def updateBooks():
    if request.method == 'POST':
        Kode = request.form['kodeBuku']
        Judul = request.form['judulBuku']
        stock = request.form['stock']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbuku SET Judul=%s, Stok=%s WHERE KodeBuku=%s", (Judul, stock, Kode))
        mysql.connection.commit()
        flash("Data Berhasil di Update")
        return redirect(url_for('dataBuku'))

#proses update data pengembalian
@app.route('/updatepengembalian', methods=['POST'])
def updatePengembalian():
    if request.method == 'POST':
        kodeKembali = request.form['kodeKembali']
        kodeBuku = request.form['kodeBuku']
        nim = request.form['nim']
        tglPengembalian = request.form['tglPengembalian']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE tkembali SET KodeBuku=%s, NIM=%s, TglKembali=%s WHERE KodeKembali=%s", (kodeBuku, nim, tglPengembalian, kodeKembali))
        mysql.connection.commit()
        flash("Data Berhasil di Update")
        return redirect(url_for('dataPengembalian'))

#proses update data peminjaman
@app.route('/updatepeminjaman', methods=['POST'])
def updatePeminjaman():
    if request.method == 'POST':
        kodePeminjaman = request.form['kodePeminjaman']
        kodeBuku = request.form['kodeBuku']
        nim = request.form['nim']
        tglPeminjaman = request.form['tglPeminjaman']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE tpinjam SET KodeBuku=%s, NIM=%s, TglPinjam=%s WHERE KodePinjam=%s", (kodeBuku, nim, tglPeminjaman, kodePeminjaman))
        mysql.connection.commit()
        flash("Data Berhasil di Update")
        return redirect(url_for('dataPeminjaman'))

# proses input mahasiswa oleh admin
@app.route('/insertmhs', methods=['POST'])
def inputMahasiswa():
    if request.method == 'POST':
        nim = request.form['nim']
        namaMhs = request.form['namaMhs']
        jurusan = request.form['jurusan']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tanggota (NIM, NamaMhs, Jurusan) VALUES (%s, %s, %s)", (nim, namaMhs, jurusan))
        mysql.connection.commit()
        flash("Data Berhasil di tambah")
        return redirect(url_for('mahasiswaTampilData'))

# proses input buku oleh admin
@app.route('/inputbuku', methods=['POST'])
def inputBuku():
    if request.method == 'POST':
        kodeBuku = request.form['kodeBuku']
        judulBuku = request.form['judulBuku']
        stok = request.form['stok']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbuku (KodeBuku, Judul, Stok) VALUES (%s, %s, %s)", (kodeBuku, judulBuku, stok))
        mysql.connection.commit()
        flash("Data Berhasil di tambah")
        return redirect(url_for('dataBuku'))

#proses input peminjaman buku oleh admin
@app.route('/inputpeminjaman', methods=['POST'])
def inputPeminjaman():
    if request.method == 'POST':
        KodeBuku = request.form['kodeBuku']
        nim = request.form['nim']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tpinjam (KodePinjam, KodeBuku, NIM, TglPinjam) VALUES (%s, %s, %s, %s)",
                    ('', KodeBuku, nim, now))
        mysql.connection.commit()
        flash("Data Berhasil di tambah")
        return redirect(url_for('dataPeminjaman'))

#proses input pengembalian buku oleh admin
@app.route('/inputpengembalian', methods=['POST'])
def inputPengembalian():
    if request.method == 'POST':
        KodeBuku = request.form['kodeBuku']
        nim = request.form['nim']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tkembali (KodeKembali, KodeBuku, NIM, TglKembali) VALUES (%s, %s, %s, %s)",
                    ('', KodeBuku, nim, now))
        mysql.connection.commit()
        flash("Data Berhasil di tambah")
        return redirect(url_for('dataPengembalian'))

if __name__ == '__main__':
    app.run(debug=True)