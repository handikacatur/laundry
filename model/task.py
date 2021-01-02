class Task:
    def __init__(self):
        self.urutan = []

    def setUrutan(self, data):
        self.urutan.append(data)
    
    def getUrutan(self, kode=None):
        for urutan, cucian in enumerate(self.urutan):
            data = cucian.getDetail()
            jumlah = str(data['jumlah'])+' Kg' if data['jenis'] == 'perkilo' else str(data['jumlah'])+' Biji'
            print(f'''{urutan+1}. Kode cucian\t: {data['kode']}
Id pelanggan\t: {data['idPelanggan']}
Nama pelanggan\t: {data['nama']}
Alamat pelanggan: {data['alamat']}
No. Hp pelanggan: {data['noHp']}
Jenis cucian\t: {data['jenis']}
Paket\t\t: {data['paket']}
Tanggal masuk\t: {data['tanggal']}
Jumlah\t\t: {jumlah}
Biaya total\t: Rp. {data['biayaTotal']}\n''')

    def setSelesai(self, kode):
        for urutan, cucian in enumerate(self.urutan):
            if cucian.getKodeCucian() == kode:
                cucian.deleteCucian()
                self.urutan.pop(urutan)
                print('Cucian berhasil dihapus!')
                break
        else:
            print('Cucian tidak ditemukan!\n')

    def getCucian(self, kode):
        for cucian in self.urutan:
            if cucian.getKodeCucian() == kode:
                return cucian
        else:
            print('Cucian tidak ditemukan!\n')