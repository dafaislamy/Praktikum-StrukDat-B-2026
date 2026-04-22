# Deskripsi: 
# PyBook Store memerlukan fitur pencarian buku agar pelanggan dapat menemukan buku 
# berdasarkan kata kunci tanpa mengetahui nama lengkapnya. 

# Ketentuan Program: 
# Gunakan data katalog berikut (dapat ditulis langsung di kode): 
# katalog = [ 
# {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
# {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
# {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
# ] 
katalog = [ 
{'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
]

# 1. Buat fungsi cari_buku(katalog, keyword) yang mencari buku berdasarkan 
# keyword, yaitu substring dari nama buku yang bersifat case-insensitive. 
    

# 2. Fungsi mengembalikan list semua buku yang sesuai dengan keyword tersebut. 


# 3. Jika tidak ada buku yang ditemukan, kembalikan list kosong dan tampilkan pesan: 
# "Buku tidak ditemukan." 


# 4. Di program utama, minta user memasukkan keyword pencarian dan tampilkan 
# hasilnya dengan format yang rapi. 

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