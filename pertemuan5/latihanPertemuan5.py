# 1. Diberikan list nilai mahasiswa: nilai_tugas = [70, 85, 90, 65, 80] 
# a. Ganti nilai 65 menjadi 75 menggunakan pencarian indeks. 
# b. Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke 
# terkecil. 
# c. Tampilkan jumlah total seluruh nilai dalam list tersebut. 
# d. Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak 
# tampilkan "Tidak ada”.

nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas[3] = 75
print(nilai_tugas)

nilai_tugas.append(95)
nilai_tugas.sort()
print(nilai_tugas)

rata_rata = sum(nilai_tugas) / len(nilai_tugas)
print(rata_rata)

for i in nilai_tugas:
    if i == 100:
        print("Ada nilai sempurna")
    else:
        print("Tidak ada")


# 2. Diberikan sebuah list yang berisi beberapa tuple. Setiap tuple berisi (Nama, Nilai): 
# kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)] 
# a. Gunakan perulangan untuk memproses setiap tuple tersebut. Jika nilai >= 75, 
# tampilkan: "Selamat [Nama], Anda Lulus!". Jika di bawah 75, tampilkan: "Maaf 
# [Nama], Anda harus remidi."

kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

for nama, nilai in kumpulan_nilai:
    if nilai >= 75:
        print(f"Selamat {nama}, Anda lulus!")
    else:
        print(f"Maaf {nama}, Anda harus remidi")


# 3. Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:  
# sesi_pagi = {"Andi", "Budi", "Cici"} sesi_siang = {"Budi", "Deni", "Eka"} 
# a. Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang) 
# b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua 
# sesi tanpa duplikat). 
# c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.

sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

hadir_semua = sesi_pagi & sesi_siang
print(hadir_semua)

nama_unik = sesi_pagi | sesi_siang
print(nama_unik)

sesi_pagi.update(sesi_siang)
print(sesi_pagi)


# 4. Diberikan data buku dalam bentuk dictionary: 
# transaksi = [ 
# {"produk": "Buku", "harga": 10000, "jumlah": 3}, 
# {"produk": "Pena", "harga": 5000, "jumlah": 10}, 
# {"produk": "Penghapus", "harga": 2000, "jumlah": 2} 
# ] 
# a. Ubah jumlah buku menjadi 8. 
# b. Tambahkan 2 produk baru. 
# c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan 
# perulangan. 
# Tampilkan ringkasan seperti ini: 
# Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.

transaksi = [ 
{"produk": "Buku", "harga": 10000, "jumlah": 3}, 
{"produk": "Pena", "harga": 5000, "jumlah": 10}, 
{"produk": "Penghapus", "harga": 2000, "jumlah": 2} 
]

transaksi[0] = {"produk": "Buku", "harga": 10000, "jumlah": 8}
print(transaksi)

transaksi.append({"produk": "Penggaris", "harga": 5000, "jumlah": 6})
transaksi.append({"produk": "Pensil", "harga": 3000, "jumlah": 5})
print(transaksi)

for x in range(len(transaksi)):
    total = transaksi[x]["harga"] * transaksi[x]["jumlah"]
    print(f"Produk: {transaksi[x]["produk"]} | Total: {total}")