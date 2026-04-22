# Deskripsi: 
# PyBook Store memberlakukan diskon bertingkat bagi pelanggan yang berbelanja 
# melebihi nominal tertentu. Data diskon disimpan dalam bentuk tuple of tuple. 

# Ketentuan Program: 
# Gunakan data level diskon berikut: 
# level_diskon = ( 
# (500000, 15),   # belanja >= 500.000 -> diskon 15% 
# (300000, 10),   # belanja >= 300.000 -> diskon 10% 
# (100000,  5),   # belanja >= 100.000 -> diskon  5% 
# (0,        0),  # default            
# ) -> tidak ada diskon 

# 1. Buat fungsi hitung_diskon(total_belanja, level_diskon, index=0) secara rekursif 
# yang memeriksa level diskon dari index ke-0. 


# 2. Fungsi mengembalikan tuple berisi (persen_diskon, nominal_diskon, total_bayar). 


# 3. Di program utama, minta input nama dan total belanja dari user, lalu tampilkan 
# rincian diskon yang diperoleh. 


# 4. Hitung dan tampilkan ringkasan: total belanja, persen diskon, nominal diskon, dan 
# total yang harus dibayar. 


# 5. Gunakan if-else untuk menampilkan pesan "Tidak ada diskon" jika total belanja 
# kurang dari Rp 100.000. 

def hitung_diskon(total_belanja, level_diskon, index=0):
    
    return (persen_diskon, nominal_diskon, total_bayar)