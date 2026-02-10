#sub-bab 'python tuples'

mytuple = ("apple", "banana", "cherry") #contoh deklarasi tuple dengan menggunakan ()

'''
tuple memiliki sifat ordered, unchangeable dan allow duplicate
- ordered berarti berurutan, tuple dapat diakses melalui indeks
- unchangeable berarti tidak dapat diubah, tuple tidak dapat ditambah maupun dikurangi isinya
- allow duplicate berarti isi tuple dapat memiliki isi yang sama
'''

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #tuple bersifat allow duplicate

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #fungsi len berguna untuk mengetahui panjang tuple

tuple1 = ("abc", 34, True, 40, "male") #tuple dapat berisi dengan tipe data yang berbeda

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #fungsi type berguna untuk mengetahui tipe data dari tuple

thistuple = tuple(("apple", "banana", "cherry")) #gunakan tuple() untuk membuat tuple
print(thistuple)


#sub-bab 'access tuples'

thistuple = ("apple", "banana", "cherry") #tuple dapat diakses dengan menggunakan indeks, indeks mulai dari 0
print(thistuple[1]) #output : banana

thistuple = ("apple", "banana", "cherry") #indeks negatif akan menghitung indeks dari data paling akhir
print(thistuple[-1]) #output : cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") #range indeks akan menampilkan range tuple dari awal hingga akhir range
print(thistuple[2:5]) #output : cherry, orange, kiwi

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #output : apple, banana, cherry, orange

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #output : cherry, orange, kiwi, melon, mango

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") #range indeks akan menampilkan range tuple dari awal hingga akhir range dengan perhitungan dari akhir data
print(thistuple[-4:-1]) #output : orange, kiwi, melon

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple: #untuk mengecek data didalam tuple apakah ada atau tidak, dengan menggunakan fungsi 'in'
  print("Yes, 'apple' is in the fruits tuple")


#sub-bab 'update tuples'

#tuple tidak dapat diubah, tetapi dapat diakali dengan mengubahnya menjadi list terlebih dahulu, lalu mengubah data, lalu kembalikan menjadi tuple kembali
x = ("apple", "banana", "cherry") #x berupa tuple
y = list(x) #y berupa list dari x
y[1] = "kiwi" #indeks pertama diganti menjadi kiwi
x = tuple(y) #x diubah menjadi tuple dari y
print(x) #output akan menghasilkan indek pertama yang telah diganti menjadi kiwi, sehingga berisi apple, kiwi, cherry

#tuple bersifat unchangeable sehingga tidak dapat diubah, ditambah maupun dikurang
#untuk menambah data tuple, tuple perlu diubah menjadi list dan menggunakan fungsi append. lalu diubah kembali menjadi tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#tuple dapat ditambha dengan tuple lainnya
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#untuk mengurang data tuple, tuple perlu diubah menjadi list dan menggunakan fungsi remove. lalu diubah kembali menjadi tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#tuple dapat dihapus menggunakan fungsi del
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)


#sub-bab 'unpack tuples'

#mendeklarasikan tuple dapat disebut juga dengan packing a tuple
fruits = ("apple", "banana", "cherry")

#nilai tuple juga dapat diekstrak kembali ke dalam variabel yang disebut sebagao unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits #masing-masing variabel akan menyimpan kembali data didalam tuple dengan catatan banyak variabel sama dengan banyak data
print(green)
print(yellow)
print(red)

#jika banyak variabel tidak sama dengan banyak data, maka perlu menggunakan arteisk (*), yang dimana variabel yang menggunakannya akan menjadi tuple yang menyimpan sisa data
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


#sub-bab 'loop tuples'

#loop pada tuple dapat dilakukan dengan menggunakan perulangan for
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#loop juga dapat digunakan dengan menggunakan indeks numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): #menggunakan fungsi range dan len
    print(thistuple[i])

#loop juga dapat menggunakan perulangan while
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


#sub-bab 'join tuples'

#untuk menggabungkan tuple, dapat menggunakan operator +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#tuple juga dapat dikalikan dengan menggunakan operator *
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)