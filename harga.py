class Harga:
    def __init__(self, kilo, cuci, cuciSetrika):
        self.harga = {
            'per-kilo': kilo,
            'cuci': cuci,
            'cuci+setrika': cuciSetrika
        }

    def setHarga(self, kilo, cuci, cuciSetrika):
        self.harga['per-kilo'] = kilo,
        self.harga['cuci'] = cuci,
        self.harga['cuci+setrika'] = cuciSetrika

    def getHarga(self, pencarian):
        return self.harga[pencarian]