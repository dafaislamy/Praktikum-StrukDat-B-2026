# Deskripsi: 
# Gabungkan semua komponen dari soal 1 hingga 4 menjadi satu program lengkap PyBook 
# Store dengan menu interaktif berbasis teks. Pada soal ini, semua fungsi dan prosedur yang 
# telah dibuat di soal1.py hingga soal4.py ditulis ulang dan digabungkan dalam satu file 
# soal5.py. 

# Ketentuan Program: 
# Program menampilkan menu berikut dan berjalan dalam perulangan hingga user memilih 
# menu 5: 
# === PyBook Store === 
# 1. Tambah Buku 
# 2. Tampilkan Semua Buku 
# 3. Beli Buku 
# 4. Laporan Penjualan 
# 5. Keluar 

# 1. Menu 1 - Tambah Buku: Gunakan fungsi tambah_buku() dan simpan hasilnya ke 
# dalam list katalog. 


# 2. Menu 2 - Tampilkan Semua Buku: Tampilkan seluruh isi katalog dalam format 
# tabel yang rapi menggunakan f-string. 


# 3. Menu 3 - Beli Buku: Gunakan prosedur proses_transaksi(). Simpan setiap 
# transaksi berhasil sebagai tuple (nama_buku, jumlah, total) ke list log_transaksi. 


# 4. Menu 4 - Laporan Penjualan: Iterasi log_transaksi, tampilkan total pemasukan 
# keseluruhan dan buku terlaris menggunakan dictionary untuk menghitung 
# frekuensi. 


# 5. Menu 5 - Keluar: Hentikan program dengan menampilkan pesan perpisahan 
# kepada user.


def tambah_buku(nama, harga, stok):

    if harga <= 0 or stok < 0:
        print("Input tidak valid")
        return None
    
    return {
        "nama" : nama,
        "harga" : harga,
        "stok" : stok
    }

list_buku = []
for buku in range(3):
    print(f"Masukkan buku ke-{buku + 1}")
    nama = str(input("Masukkan nama buku : "))
    harga = float(input("Masukkan harga buku : "))
    stok = int(input("Masukkan stok buku : "))

    data_buku = tambah_buku(nama, harga, stok)
    if data_buku:
        list_buku.append(data_buku)

print("Daftar Buku")
print(list_buku)



katalog = [ 
{'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
]

def cari_buku(katalog, keyword):
    hasil_cari = []
    for buku in katalog:
        if keyword in buku:
            hasil_cari.append(buku)
    return hasil_cari

key = input("Masukkan buku yang ingin dicari : ")
hasil = cari_buku(katalog, key)

if not hasil:
    print("Buku tidak ditemukan")
else:
    print(hasil)