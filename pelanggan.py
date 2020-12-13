class Pelanggan:
    def __init__(self, nama, alamat, noHp, statusCucian):
        self.__nama = nama
        self.__alamat = alamat
        self.__noHp = noHp
        self.__statusCucian = statusCucian

    def getNama(self):
        return self.__nama

    def setNama(self, namaBaru):
        self.__nama = namaBaru

    def getAlamat(self):
        return self.__alamat

    def setAlamat(self, alamatBaru):
        self.__alamat = alamatBaru

    def getNoHp(self):
        return self.__noHp

    def setNoHp(self, noBaru):
        self.__noHp = noBaru

    def getStatus(self):
        return self.__statusCucian

    def setStatus(self, status):
        self.__statusCucian = status