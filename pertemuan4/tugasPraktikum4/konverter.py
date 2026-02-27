from kurs import data_kurs

class Konverter:
    def __init__(self):
        self.kurs = data_kurs #Encapsulation: Menyimpan data kurs di dalam atribut objek

    def convert(self, dari, ke, jumlah):
        #Jika mata uang asal adalah IDR
        if dari == "IDR":
            if ke == "IDR":
                return jumlah
            return jumlah / self.kurs[ke]
        
        #Jika mata uang tujuan adalah IDR
        elif ke == "IDR":
            return jumlah * self.kurs[dari]
        
        #Jika antar mata uang asing
        else:
            #Konversi dulu ke IDR baru ke mata uang tujuan
            jumlah_dalam_idr = jumlah * self.kurs[dari]
            return jumlah_dalam_idr / self.kurs[ke]