class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
car1 = Car('Toyota', 'Corolla')
print(car1.brand)
print(car1.model)

#nilai dari properti dapat diubah pada objek      
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person('Tobias', 25)
print(p1.age)
p1.age = 26
print(p1.age)

#properti dari objek juga dapat dihapus menggunakan del keyword
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person('Linus', 30)
del p1.age
print(p1.name)

#properti baru dapat ditambahkan ke objek yang sudah ada
class Person:
  def __init__(self, name):
    self.name = name
p1 = Person('Tobias')
p1.age = 25
p1.city = 'Oslo'
print(p1.name)
print(p1.age)
print(p1.city)