#deklarasi __init__() method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person('Dafa', 18)
print(p1.name)
print(p1.age)

#metode __init__() dipanggil secara oromatis setiap kali kelas digunakan untuk membuat objek baru
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
p1 = Person('Dafa')
p2 = Person('Islamy', 26)

#parameter pada metode __init__() dapat diatur menggunakan nilai default.
#pada contoh program dibawah, parameter age diberi nilai default 18
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
p1 = Person('Dafa')
p2 = Person('Islamy', 26)
print(p1.name, p1.age)
print(p2.name, p2.age)