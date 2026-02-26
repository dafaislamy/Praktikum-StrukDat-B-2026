#pendeklarasian class
class MyClass:
  x = 6
p1 = MyClass()
print(p1.x)

del p1 #menghapus p1

#objek dapat dibuah sebanyak mungkin
q1 = MyClass()
q2 = MyClass()
q3 = MyClass()
print(q1.x)
print(q2.x)
print(q3.x)

#Kelas tidak boleh kosong, tetapi karena suatu alasan kelas perlu dibuat tanpa isi atau konten,
#tambahkan pass statement untuk menghindari kesalahan.
class Person:
  pass