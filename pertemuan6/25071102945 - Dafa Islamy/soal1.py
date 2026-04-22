# Deskripsi: 
# Toko buku PyBook Store membutuhkan sebuah fungsi untuk menambahkan buku baru ke 
# dalam sistem. Fungsi ini harus memvalidasi data masukan sebelum menyimpannya. 

# Ketentuan Program: 
# 1. Buat fungsi tambah_buku(nama, harga, stok) yang menerima tiga parameter: 
# nama buku (string), harga (int/float), dan stok (int). 

# 2. Validasi input: harga harus lebih besar dari 0 dan stok tidak boleh bernilai negatif. 
# Jika tidak valid, cetak pesan error dan kembalikan nilai None. 

# 3. Jika data valid, kembalikan sebuah dictionary dengan key: "nama", "harga", dan 
# "stok". 

# 4. Di program utama, gunakan perulangan untuk meminta input data 3 buku dari 
# user, simpan ke dalam list, dan tampilkan seluruh isi list di akhir. 

# 5. Program menampilkan daftar buku yang berhasil ditambahkan beserta seluruh 
# datanya di akhir eksekusi.

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