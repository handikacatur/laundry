from model.cucian import Cucian
from model.harga import Harga
from model.task import Task
import sqlite3

def menu(pertamakali):
    print('Selamat datang!')
    print('Masukkan pilihan menu berikut')
    if pertamakali:
        print('Silakan atur harga terlebih dahulu')
    else:
        return int(input('''1. Tambah data cucian
2. Edit data cucian
3. Lihat urutan cucian
4. Lihat urutan berdasarkan kode cucian
5. Tambah data cucian selesai
6. Keluar
Pilihan: '''))

def fetchCucian():
    conn = sqlite3.connect("laundry.db")
    conn.cursor

ulangi = True

while ulangi:
    pilihan = menu(False)
