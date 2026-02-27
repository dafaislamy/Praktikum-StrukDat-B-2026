from tabulate import tabulate
from kurs import data_kurs
from konverter import Konverter #Mengimport Class yang baru dibuat

def main():

    def tampilkan_tabel():
        headers = ["Kode", "Kurs"] #Menentukan nama kolom yang akan muncul dibagian paling atas
        tabel_data = [[k, f"{v:,}"] for k, v in data_kurs.items()]
        print("\n=== KONVERTER MATA UANG ===")
        print(tabulate(tabel_data, headers=headers, tablefmt="fancy_grid"))

    tampilkan_tabel()
    
    konverter_obj = Konverter() #Membuat Objek (Instansiasi), membuat (benda) nyata dari cetakan Konverter
    
    try:
        #Mengambil input user
        dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper() #Fungsi .upper() berguna untuk mengubah input user menjadi huruf besar
        ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
        jumlah = float(input("Jumlah: "))
        
        #Memanggil Method 'convert' dari objek yang tadi dibuat
        hasil = konverter_obj.convert(dari, ke, jumlah)
        
        #Menampilkan hasil
        print(f"{dari} {jumlah:,.2f} = {ke} {hasil:,.2f}")
        
    except ValueError:
        print("Error: Harap masukkan angka yang valid.")
    except:
        print("Terjadi kesalahan")

if __name__ == "__main__":
    main()