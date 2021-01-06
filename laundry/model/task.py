class Task:
    def __init__(self):
        self.urutan = []

    def setUrutan(self, data):
        self.urutan.append(data)
    
    def getUrutan(self, kode=None):
        print(f'''\n{'='*71}
|{'No.'.center(8)}|{'Kode'.center(8)}|{'Nama Pelanggan'.center(30)}|{'Tanggal'.center(20)}|\n{'='*71}''')
        for urutan, cucian in enumerate(self.urutan):
            data = cucian.getDetail()
            jumlah = str(data['jumlah'])+' Kg' if data['jenis'] == 'perkilo' else str(data['jumlah'])+' Biji'
            urutan = str(urutan+1) + '.'
            print(f'''|{urutan.center(8)}| {data["kode"].ljust(7)}| {data["nama"].ljust(29)}| {data["tanggal"].ljust(19)}|\n{'-'*71}''')

    def setSelesai(self, kode):
        for urutan, cucian in enumerate(self.urutan):
            if cucian.getKodeCucian() == kode:
                data = cucian.getDetail()
                print(f"""{'='*40}\n{'Cucian'.center(40)}\n{'='*40}
{'Kode'.ljust(25)}: {data['kode']}
{'Id Pelanggan'.ljust(25)}: {data['idPelanggan']}
{'Pelanggan'.ljust(25)}: {data['nama']}
{'Alamat'.ljust(25)}: {data['alamat']}
{'No. Hp'.ljust(25)}: {data['noHp']}
{'Jenis'.ljust(25)}: {data['jenis']}
{'Paket'.ljust(25)}: {data['paket']}
{'Jumlah'.ljust(25)}: {data['jumlah']}
{'='*40}
{'Total'.rjust(25)}: Rp. {data['biayaTotal']}""")
                dibayarkan = int(input(f"{'Dibayar'.rjust(25)}: Rp. "))
                kembalian = dibayarkan - data['biayaTotal']
                if kembalian < 0:
                    print('Uang tidak cukup!')
                    self.setSelesai(kode)
                else:
                    print(f"{'Kembalian'.rjust(25)}: Rp. {kembalian}")
                    cucian.deleteCucian()
                    self.urutan.pop(urutan)
                    print('='*40)
                    print()
                    print('Terimakasih!'.center(40))
                break
        else:
            print('Cucian tidak ditemukan!\n')

    def getCucian(self, kode):
        for cucian in self.urutan:
            if cucian.getKodeCucian() == kode:
                return cucian
        else:
            print(f'Cucian dengan kode {kode} tidak ditemukan!\n')

    def getPelanggan(self, idPelanggan):
        for cucian in self.urutan:
            if cucian.getDetail()['idPelanggan'] == idPelanggan:
                return cucian
        else:
            print(f'Cucian dengan id pelanggan {idPelanggan} tidak ditemukan!')