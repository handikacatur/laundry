import sqlite3
if __name__ == '__main__':
    from pelanggan import Pelanggan
else:
    from model.pelanggan import Pelanggan

def createTable():
    conn = sqlite3.connect("laundry.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS cucian(nama TEXT NOT NULL,
alamat TEXT NOT NULL,
noHp TEXT NOT NULL,
jenis TEXT,
paket TEXT,
tanggal TEXT,
kodeCucian TEXT NOT NULL PRIMARY KEY)""")
    conn.commit()
    conn.close()

class Cucian(Pelanggan):
    def __init__ (self, nama, alamat, noHp, jenis, paket, tanggal, kodeCucian):
        super().__init__(nama, alamat, noHp)
        self.__jenis = jenis
        self.__berat = 0
        self.__paket = paket
        self.__biayaTotal = 0
        self.__dibayar = 0
        self.__tanggal = tanggal
        self.__kodeCucian = kodeCucian
        self.__jumlah = 0
        createTable()

    def getJenis(self):
        return self.__jenis

    def setJenis(self, jenisBaru):
        self.__jenis = jenisBaru
    
    def getBerat(self):
        return self.__berat

    def setBerat(self, beratBaru):
        self.__berat = beratBaru

    def getPaket(self):
        return self.__paket

    def setPaket(self, paketBaru):
        self.__paket = paketBaru

    def getBiayaTotal(self):
        return self.__biayaTotal

    def setJumlah(self, jumlahBaru):
        self.__jumlah = jumlahBaru

    def setPembayaran(self, bayar):
        self.__dibayar = bayar

    # def getDetailCucian(self):

    # def hitungBiaya(self,):

    # def hitungPembayaran(self, ):

    # def cetakStruk(self, ):

    def getKodeCucian(self):
        return self.__kodeCucian

    def setKodeCucian(self, kodeBaru):
        self.__kodeCucian = kodeBaru
