import sqlite3

class Harga:
    def __init__(self, kilo, cuci, cuciSetrika):
        self.harga = {
            'per_kilo': kilo,
            'cuci': cuci,
            'cuci_setrika': cuciSetrika
        }

    def createTableHarga(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS harga(id INT NOT NULL PRIMARY KEY, per_kilo INT NOT NULL, cuci INT NOT NULL, cuci_setrika INT NOT NULL)", (self.harga['per_kilo'], self.harga['cucian'], self.harga['cuci_setrika']))

    def setHarga(self, kilo, cuci, cuciSetrika):
        self.harga['per_kilo'] = kilo,
        self.harga['cuci'] = cuci,
        self.harga['cuci_setrika'] = cuciSetrika

    def getHarga(self, pencarian):
        return self.harga[pencarian]