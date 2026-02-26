class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error

#properti privat tidak dapat diakses langsung dari luar kelas.
#untuk mengakses properti privat tersebut dapat menggunakan metode getter.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())

#untuk memodifikasi properti privat, dapat menggunakan metode setter.
#metode setter juga dapat memvalidasi nilai sebelum menetapkannya.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

#python juga memiliki konvensi untuk properti yang dilindungi dengan menggunakan awalan garis bawah tunggal (_)
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't

#metode juga dapat dibuat menjadi privat dengan menggunakan awalan garis bawah ganda (__)
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error

#name Mangling adalah cara Python mengimplementasikan properti dan metode privat.
#saat menggunakan garis bawah ganda (__), Python secara otomatis mengubah namanya
#secara internal dengan menambahkan _ClassName didepannya.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!