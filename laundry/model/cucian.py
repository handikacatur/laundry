import sqlite3
from model.pelanggan import Pelanggan
from random import randint
from datetime import datetime

class Cucian(Pelanggan):
    def __init__ (self, jenis, paket, tanggal, jumlah, biayaTotal, idPelanggan=None, nama=None, alamat=None, noHp=None, kodeCucian=None):
        super().__init__(idPelanggan, nama, alamat, noHp)
        self._jenis = jenis
        self._paket = paket
        self._biayaTotal = biayaTotal
        self._tanggal = tanggal
        self._kodeCucian = kodeCucian
        self._jumlah = jumlah

        self.createTableCucian()
        self.createTablePelanggan()

    def getDetail(self):
        return {
            'kode': self._kodeCucian,
            'idPelanggan': self._id,
            'nama': self._nama,
            'alamat': self._alamat,
            'noHp': self._noHp,
            'jenis': self._jenis,
            'paket': self._paket,
            'tanggal': self._tanggal,
            'jumlah': self._jumlah,
            'biayaTotal': self._biayaTotal,
        }

    def getKodeCucian(self):
        return self._kodeCucian

    def createTableCucian(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS cucian(
                        kodeCucian TEXT NOT NULL PRIMARY KEY,
                        jenis TEXT,
                        paket TEXT,
                        biayaTotal INT,
                        tanggal TEXT,
                        jumlah INT,
                        idPelanggan INTEGER NOT NULL,
                        FOREIGN KEY (idPelanggan)
                            REFERENCES pelanggan (idPelanggan)
                    )""")
        conn.commit()
        conn.close()

    def insert(self, idPelanggan):
        if self._paket == '1':
            self._kodeCucian = 'A' + str(randint(1, 900)).zfill(3)
        else:
            self._kodeCucian = 'B' + str(randint(1, 900)).zfill(3)

        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        if idPelanggan == '':
            cur.execute("INSERT INTO pelanggan(nama, alamat, noHp) VALUES(?, ?, ?)", (
                self._nama,
                self._alamat,
                self._noHp
            ))
            conn.commit()
            cur.execute("SELECT idPelanggan FROM pelanggan WHERE nama=? AND noHp=?", (self._nama, self._noHp))
            idPelanggan = cur.fetchone()
            self._id = int(idPelanggan[0])
        else:
            cur.execute("SELECT nama, alamat, noHp FROM pelanggan WHERE idPelanggan=?", (idPelanggan,))
            row = cur.fetchone()

            self._id = idPelanggan
            self._nama = row[0]
            self._alamat = row[1]
            self._noHp = row[2]

        cur.execute("INSERT INTO cucian(jenis, paket, biayaTotal, tanggal, kodeCucian, jumlah, idPelanggan) VALUES(?, ?, ?, ?, ?, ?, ?)", (
            self._jenis,
            self._paket,
            self._biayaTotal,
            self._tanggal,
            self._kodeCucian,
            self._jumlah,
            self._id
        ))
        conn.commit()
        conn.close()

    def deleteCucian(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM cucian WHERE kodeCucian=?", (self._kodeCucian,))
        conn.commit()
        conn.close()