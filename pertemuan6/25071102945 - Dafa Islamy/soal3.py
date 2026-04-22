# Deskripsi: 
# PyBook Store membutuhkan prosedur untuk memproses transaksi pembelian dan 
# mencatat riwayat buku yang pernah dibeli tanpa data duplikat. 

# Ketentuan Program: 

# 1. Buat prosedur proses_transaksi(katalog, nama_buku, jumlah_beli) yang mencari 
# buku di katalog berdasarkan nama (exact match, case-insensitive). 


# 2. Jika buku ditemukan dan stok mencukupi, kurangi stok buku tersebut dan cetak 
# total harga yang harus dibayar. 


# 3. Jika stok tidak mencukupi, cetak pesan peringatan kepada user. 


# 4. Jika buku tidak ditemukan di katalog, cetak pesan error. 


# 5. Gunakan set bernama riwayat_transaksi untuk menyimpan nama buku yang 
# pernah dibeli tanpa duplikat. Lakukan 3 transaksi di program utama dan tampilkan 
# isi riwayat_transaksi di akhir.

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    for buku in katalog: