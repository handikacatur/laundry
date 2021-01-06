from model.cucian import Cucian
from model.harga import Harga
from model.task import Task
import sqlite3
from datetime import datetime

def menu():
    global pertamakali
    global harga

    if pertamakali:
        print('='*70)
        print('Selamat datang di Laundry Kuy!'.center(70))
        print('Silakan atur harga terlebih dahulu'.center(70))
        print('='*70)
        
        cuci = int(input('Masukkan harga paket cuci\t: Rp. '))
        cuci_setrika = int(input('Masukkan harga paket cuci dan setrika: Rp. '))
        print()

        harga = Harga()
        harga.insert(cuci, cuci_setrika)

        pertamakali = False

        return 0
    else:
        print(f'''\n{'-'*40}
|{'Laundry Kuy!'.center(38)}|''')
        print(f'''|{'Masukkan pilihan menu berikut'.center(38)}|\n{'-'*40}''')
        return int(input(f'''{'|  [1] Tambah data cucian'.ljust(39) + '|'}
{'|  [2] Lihat detail cucian'.ljust(39)+'|'}
{'|  [3] Lihat urutan cucian'.ljust(39)+'|'}
{'|  [4] Cucian selesai'.ljust(39)+'|'}
{'|  [5] Edit Pelanggan'.ljust(39)+'|'}
{'|  [6] Lihat Harga'.ljust(39)+'|'}
{'|  [7] Edit Harga'.ljust(39)+'|'}
{'|  [8] Keluar'.ljust(39)+'|'}
{'-'*40}
=> '''))

def tambahData():
    print('\nIsi data berikut ini!')
    idPelanggan = input('Masukkan id pelanggan: (biarkan kosong jika pelanggan belum terdaftar) ')
    namaPelanggan = None
    alamat = None
    noHp = None

    if idPelanggan == '':
        namaPelanggan = input('Masukkan nama pelanggan: ')
        alamat = input('Masukkan alamat pelanggan: ')
        noHp = input('Masukkan nomor HP pelanggan: ')
    else:
        conn = sqlite3.connect("laundry.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM pelanggan WHERE idPelanggan=?', (idPelanggan,))
        row = cur.fetchone()
        conn.close()

        if row == None:
            print(f'Pelanggan dengan id {idPelanggan} tidak ditemukan!')
            return None

    jenis = input('Masukkan jenis:\n1. Perbiji\n2. Perkilo\n=> ')

    while True:
        if jenis == '1':
            hargaPerbiji = input('Masukkan harga perbijinya: Rp. ')
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

    tanggal = datetime.now().date()

    task.setUrutan(Cucian(jenis, paket, tanggal, jumlah, biayaTotal, idPelanggan, namaPelanggan, alamat, noHp))
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
        if cucian == None:
            continue

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
        kode = input('Masukkan kode cucian: ')
        cucian = task.getCucian(kode)
        detail = cucian.getDetail()
        jumlah = str(detail['jumlah'])+' Kg' if detail['jenis'] == 'perkilo' else str(detail['jumlah'])+' Biji'

        print(f'''\n{'='*30}
Kode cucian\t: {detail['kode']}
Id pelanggan\t: {detail['idPelanggan']}
Nama pelanggan\t: {detail['nama']}
Alamat pelanggan: {detail['alamat']}
No. Hp pelanggan: {detail['noHp']}
Jenis cucian\t: {detail['jenis']}
Paket\t\t: {detail['paket']}
Tanggal masuk\t: {detail['tanggal']}
Jumlah\t\t: {jumlah}
Biaya total\t: Rp. {detail['biayaTotal']}
{'='*30}\n''')

    elif pilihan == 3:
        task.getUrutan()
        input('\nTekan enter untuk kembali ke menu utama...')

    elif pilihan == 4:
        kode = input('Masukkan kode cucian: ')
        task.setSelesai(kode)

    elif pilihan == 5:
        idPelanggan = int(input('Masukkan Id Pelanggan: '))
        pelanggan = task.getPelanggan(idPelanggan)
        nama = input('Masukkan nama pelanggan: (biarkan kosong jika tidak diubah) ')
        alamat = input('Masukkan alamat pelanggan: (biarkan kosong jika tidak diubah) ')
        noHp = input('Masukkan no. Hp pelanggan: (biarkan kosong jika tidak diubah) ')

        data = pelanggan.updatePelanggan(nama, alamat, noHp)
        print('\nData berhasil diubah!')
        print(f"""{'='*30}\nId pelanggan\t: {data['idPelanggan']}
Nama pelanggan\t: {data['nama']}
Alamat pelanggan: {data['alamat']}\n{'='*30}""")

    elif pilihan == 6:
        data = harga.getHarga()
        print(f"""{'='*30}
|{'Paket'.center(17)}|{'Harga'.center(10)}|\n{'='*30}
|{'Cuci'.ljust(17)}|Rp. {str(data['cuci']).ljust(6)}|\n|{'Cuci + Setrika'.ljust(17)}|Rp. {str(data['cuci_setrika']).ljust(6)}|\n{'-'*30}""")

    elif pilihan == 7:
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

    elif pilihan == 8:
        break
    else:
        print('Masukkan pilihan menu yang benar!')
