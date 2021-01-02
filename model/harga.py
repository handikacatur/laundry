import sqlite3
# from abc import ABC, abstractmethod

# class TemplateHarga(ABC):
#     @abstractmethod
#     def insert(self):
#         pass

#     @abstractmethod
#     def update(self):
#         pass

class Harga:
    def __init__(self):
        self.harga = {
            'cuci': 0,
            'cuci_setrika': 0
        }
        self.createTableHarga()

    def createTableHarga(self):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS harga(idHarga INTEGER PRIMARY KEY AUTOINCREMENT, cuci INT NOT NULL, cuci_setrika INT NOT NULL)")
        conn.commit()
        conn.close()

    def insert(self, cuci, cuciSetrika):
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO harga(cuci, cuci_setrika) VALUES(?,?)", (cuci, cuciSetrika))
        conn.commit()
        conn.close()

        self.harga['cuci'] = cuci
        self.harga['cuci_setrika'] = cuciSetrika

    def update(self, cuci=None, cuciSetrika=None):
        self.harga['cuci'] = cuci if cuci != None else self.harga['cuci']
        self.harga['cuci_setrika'] = cuciSetrika if cuciSetrika != None else self.harga['cuci_setrika']

        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute("UPDATE harga SET cuci=?, cuci_setrika=? WHERE idHarga=1", (self.harga['cuci'], self.harga['cuci_setrika']))
        conn.commit()
        conn.close()

    def getHarga(self):
        return self.harga

    def setHarga(self, cuci, cuci_setrika):
        self.harga['cuci'] = cuci
        self.harga['cuci_setrika'] = cuci_setrika