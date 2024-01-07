# Creating a class and object with class and instance attributes

class Dog:
  attr1 = "mammal"

  def __init__(self, name):
    self.name = name


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print(f"Rodger is a {Rodger.attr1}")
print(f"Tommy is also a {Tommy.attr1}")

print(f"My name is {Rodger.name}")
print(f"My name is {Tommy.name}")

# Creating Class and objects with methods


class Dog:
  attr1 = "mammal"

  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"My name is {self.name}")


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.speak()
Tommy.speak()
