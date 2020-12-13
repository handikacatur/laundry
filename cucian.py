import pelanggan as Pelanggan

class Cucian(Pelanggan):
    def __init__ (self, nama, alamat, noHp, statusCucian, jenis, berat, paket, biayaTotal, dibayar = 0, tanggal, kodeCucian, jumlah):
        super().__init__(nama,alamat,noHp,statusCucian)
        self.__jenis = jenis
        self.__berat = berat
        self.__paket = paket
        self.__biayaTotal = biayaTotal
        self.__dibayar = dibayar
        self.__tanggal = tanggal
        self.__kodeCucian = kodeCucian
        self.__jumlah = jumlah

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

    
