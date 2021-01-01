import sqlite3

class Pelanggan:
    def __init__(self, nama, alamat, noHp, idPelanggan=None):
        self._id = idPelanggan
        self._nama = nama
        self._alamat = alamat
        self._noHp = noHp
        self.createTablePelanggan()

    def createTablePelanggan(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS pelanggan(idPelanggan INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT NOT NULL, alamat TEXT NOT NULL, noHp TEXT NOT NULL)")
        conn.commit()
        conn.close()

    def getPelanggan(self):
        return [self._nama, self._alamat, self._noHp]
    
    def updatePelanggan(self, nama, alamat, noHp):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("UPDATE pelanggan SET nama=?, alamat=?, noHp=? WHERE idPelanggan=?", (nama, alamat, noHp, self._id))
        conn.execute()
        conn.close()

        self._nama = nama
        self._alamat = alamat
        self._noHp = noHp