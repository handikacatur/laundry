import sqlite3

class Pelanggan:
    countPelanggan = 0
    def __init__(self, nama, alamat, noHp):
        self._id = countPelanggan + 1
        self._nama = nama
        self._alamat = alamat
        self._noHp = noHp
        self.createTablePelanggan()

        countPelanggan += 1

    def createTablePelanggan(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS pelanggan(idPelanggan INT NOT NULL PRIMARY KEY, nama TEXT NOT NULL, alamat TEXT NOT NULL, noHP TEXT NOT NULL)")
        conn.commit()
        conn.close()

    def getPelanggan(self):
        return [self._nama, self._alamat, self._noHp, self._kodeCucian]
    
    def updatePelanggan(self, nama, alamat, noHp):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("UPDATE pelanggan SET nama=?, alamat=?, noHp=? WHERE idPelanggan=?", (nama, alamat, noHp, self._id))
        conn.execute()
        conn.close()

        self._nama = nama
        self._alamat = alamat
        self._noHp = noHp