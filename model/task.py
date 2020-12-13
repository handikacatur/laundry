class Task:
    def __init__(self):
        self.urutan = []

    def setUrutan(self, data):
        self.urutan.append(data)
    
    def getUrutan(self, kode=None):
        if kode == None:
           for urutan, cucian in enumerate(self.urutan):
               kode = cucian.getKodeCucian()
               namaPelanggan = cucian.getNama()

               print(f'''{urutan+1}. \tKode: {kode}
\tPelanggan: {namaPelanggan}''')
        else:
            for urutan, cucian in enumerate(self.urutan):
                if cucian.getKodeCucian() == kode:
                    kode = cucian.getKodeCucian()
                    namaPelanggan = cucian.getNama()

                    print(f'Cucian yang anda cari pada urutan ke: {urutan}')

    def setSelesai(self, kode):
        for urutan, cucian in enumerate(self.urutan()):
            if cucian.getKodeCucian() == kode:
                self.urutan.pop(urutan)