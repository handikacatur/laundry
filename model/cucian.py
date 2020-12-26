import sqlite3
from model.pelanggan import Pelanggan
from random import randint

class Cucian(Pelanggan):
    def __init__ (self, nama, alamat, noHp, jenis, paket, tanggal, jumlah, biayaTotal):
        super().__init__(nama, alamat, noHp)
        self._jenis = jenis
        self._paket = paket
        self._biayaTotal = biayaTotal
        self._tanggal = tanggal
        self._kodeCucian
        self._jumlah = jumlah
        self._statusCucian = False

        self.createTableCucian()
        self.createTablePelanggan()

    def getCucian(self):
        return [self._nama, self._tanggal, self._kodeCucian]

    def createTableCucian(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS cucian(
                        jenis TEXT,
                        paket TEXT,
                        biayaTotal INT,
                        dibayar INT
                        tanggal TEXT,
                        jumlah INT,
                        statusCucian BOOLEAN,
                        kodeCucian TEXT NOT NULL PRIMARY KEY,
                        idPelanggan INT NOT NULL,
                        FOREIGN KEY (idPelanggan)
                            REFERENCES pelanggan (idPelanggan)
                    )""")
        conn.commit()
        conn.close()

    def insert(self):
        if self.paket == 1:
            self._kodeCucian = 'A' + str(randint(1, 900)).zfill(3)
        else:
            self._kodeCucian = 'B' + str(randint(1, 900)).zfill(3)

        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO cucian(jenis, paket, biayaTotal, tanggal, kodeCucian, jumlah, statusCucian) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            self._jenis,
            self._paket,
            self._biayaTotal,
            self._tanggal,
            self._kodeCucian,
            self._jumlah,
            self._statusCucian
        ))
        conn.commit()
        cur.execute("INSERT INTO pelanggan(nama, alamat, noHp) VALUES(?, ?, ?)", (
            self._nama,
            self._alamat,
            self._noHp
        ))
    
    def updateCucian(self, jenis, paket, tanggal, jumlah, biayaTotal):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("UPDATE cucian SET jenis=?, paket=?, tanggal=?, jumlah=?, biayaTotal=? WHERE kodeCucian=?", (jenis, tanggal, jumlah, biayaTotal, self._kodeCucian))
        conn.commit()
        conn.close()

        self._jenis = jenis
        self._paket = paket
        self._tanggal = tanggal
        self._jumlah = jumlah
        self._biayaTotal = biayaTotal

    def deleteCucian(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("DELETE from cucian WHERE kodeCucian=?", (self._kodeCucian))
        conn.commit()
        conn.close()