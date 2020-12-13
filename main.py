from model.cucian import Cucian
from model.harga import Harga
from model.task import Task

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


ulangi = True

while ulangi:
    pilihan = menu(False)

    if pilihan == 1:
        pass
    elif pilihan == 2:
        pass
    elif pilihan == 3:
        pass
    elif pilihan == 4:
        pass
    elif pilihan == 5:
        pass
    elif pilihan == 6:
        ulangi = False
    else:
        print('''Pilihan tidak sesuai!
Masukkan pilihan angka 1-6 \n''')