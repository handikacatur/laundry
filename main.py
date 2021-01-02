from model.cucian import Cucian
from model.harga import Harga
from model.task import Task
import sqlite3
from datetime import datetime

def menu():
    global pertamakali
    global harga
    
    if pertamakali:
        print('Selamat datang!')
        print('Silakan atur harga terlebih dahulu')
        
        cuci = int(input('Masukkan harga paket cuci: '))
        cuci_setrika = int(input('Masukkan harga paket cuci dan setrika: '))
        print()

        harga = Harga()
        harga.insert(cuci, cuci_setrika)

        pertamakali = False

        return 0
    else:
        print('Masukkan pilihan menu berikut')
        return int(input('''1. Tambah data cucian
2. Lihat urutan cucian
3. Cucian selesai
4. Lihat Harga
5. Edit Harga
6. Keluar
=> '''))

def tambahData():
    print('Isi data berikut ini!')
    idPelanggan = input('Masukkan id pelanggan: (biarkan kosong jika pelanggan belum terdaftar) ')
    namaPelanggan = None
    alamat = None
    noHp = None

    if idPelanggan == '':
        namaPelanggan = input('Masukkan nama pelanggan: ')
        alamat = input('Masukkan alamat pelanggan: ')
        noHp = input('Masukkan nomor HP pelanggan: ')

    jenis = input('Masukkan jenis:\n1. Perbiji\n2. Perkilo\n=> ')

    while True:
        if jenis == '1':
            hargaPerbiji = input('Masukkan harga perbijinya: ')
            jumlah = input('Masukkan jumlah: ')
            jenis = 'perbiji'
            break
        elif jenis == '2':
            jumlah = input('Masukkan berat cucian: ')
            jenis = 'perkilo'
            break
        else:
            jenis = input('Harap masukkan jenis yang sesuai:\n1. Perbiji\n2. Perkilo\n=> ')
    
    paket = input('Masukkan paket:\n1. Cuci\n2. Cuci + Setrika\n=> ')

    while True:
        if paket == '1' and jenis == 'perkilo':
            biayaTotal = int(jumlah) * (harga.getHarga()['cuci'])
            paket = 'cuci'
            break
        elif paket == '2' and jenis == 'perkilo':
            biayaTotal = int(jumlah) * (harga.getHarga()['cuci_setrika'])
            paket = 'cuci+setrika'
            break
        elif paket == '1' and jenis != 'perkilo':
            biayaTotal = int(jumlah) * int(hargaPerbiji)
            paket = 'cuci'
            break
        elif paket == '2' and jenis != 'perkilo':
            biayaTotal = int(jumlah) * int(hargaPerbiji)
            paket = 'cuci+setrika'
            break
        else:
            paket = input('Harap masukkan paket yang sesuai:\n1. Cuci\n2. Cuci + Setrika\n=> ')

    tanggal = datetime.now()

    task.setUrutan(Cucian(jenis, paket, tanggal, jumlah, biayaTotal, namaPelanggan, alamat, noHp))
    cucian = task.urutan[len(task.urutan)-1]
    cucian.insert(idPelanggan)

    return cucian

def fetchCucian():
    conn = sqlite3.connect("laundry.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pelanggan(idPelanggan INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT NOT NULL, alamat TEXT NOT NULL, noHp TEXT NOT NULL)")
    cur.execute("""CREATE TABLE IF NOT EXISTS cucian(
                        kodeCucian TEXT NOT NULL PRIMARY KEY,
                        jenis TEXT,
                        paket TEXT,
                        biayaTotal INT,
                        tanggal TEXT,
                        jumlah INT,
                        idPelanggan INTEGER NOT NULL,
                        FOREIGN KEY (idPelanggan)
                            REFERENCES pelanggan (idPelanggan)
                    )""")
    cur.execute("SELECT * FROM cucian INNER JOIN pelanggan USING(idPelanggan)")
    rows = cur.fetchall()
    return rows

def fetchHarga():
    global pertamakali
    global harga
    
    conn = sqlite3.connect("laundry.db")
    cur = conn.cursor()
    try:
        cur.execute("SELECT cuci, cuci_setrika FROM harga")
        row = cur.fetchall()
        conn.close()
        harga = Harga()
        harga.setHarga(row[0][0], row[0][1])
        pertamakali = False
    except:
        pertamakali = True

harga = None
task = Task()
pertamakali = False

for i in fetchCucian():
    task.setUrutan(Cucian(kodeCucian=i[0], jenis=i[1], paket=i[2], biayaTotal=i[3], tanggal=i[4], jumlah=i[5], idPelanggan=i[6], nama=i[7], alamat=i[8], noHp=i[9]))

fetchHarga()

while True:
    pilihan = menu()

    if pilihan == 0:
        continue

    elif pilihan == 1:
        cucian = tambahData()
        cucian = cucian.getDetail()
        jumlah = str(cucian['jumlah'])+' Kg' if cucian['jenis'] == 'perkilo' else str(cucian['jumlah'])+' Biji'
        print(f'''\n{'='*30}
Kode cucian\t: {cucian['kode']}
Id pelanggan\t: {cucian['idPelanggan']}
Nama pelanggan\t: {cucian['nama']}
Alamat pelanggan: {cucian['alamat']}
No. Hp pelanggan: {cucian['noHp']}
Jenis cucian\t: {cucian['jenis']}
Paket\t\t: {cucian['paket']}
Tanggal masuk\t: {cucian['tanggal']}
Jumlah\t\t: {jumlah}
Biaya total\t: Rp. {cucian['biayaTotal']}
{'='*30}\n''')

    elif pilihan == 2:
        task.getUrutan()
        print()

    elif pilihan == 3:
        kode = input('Masukkan kode cucian: ')
        task.setSelesai(kode)

    elif pilihan == 4:
        data = harga.getHarga()
        print(f"Cuci: Rp. {data['cuci']}\nCuci + Setrika: Rp. {data['cuci_setrika']}\n")

    elif pilihan == 5:
        cuci = input('Masukkan harga paket cuci: (kosongi jika tidak diubah) ')
        cuci_setrika = input('Masukkan harga paket cuci + setrika: (kosongi jika tidak diubah) ')

        if cuci == '':
            cuci = None
        else:
            cuci = int(cuci)

        if cuci_setrika == '':
            cuci_setrika = None
        else:
            cuci_setrika = int(cuci_setrika)

        harga.update(cuci, cuci_setrika)

    elif pilihan == 6:
        break
