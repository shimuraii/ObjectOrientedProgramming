class Pet: # Parent Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self): # Is overrided by the local class if inherited
        print("idk what i say")
class Cat(Pet): # Child 1
    def __init__(self, name, age, color):
        super().__init__(name, age) # super = class we inherited from
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
class Dog(Pet): # Child 2 
    def speak(self):
        print("Bark")
class Fish(Pet):
    pass
p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "blue")
c.speak()
c.show()
d = Dog("Clint", 10)
d.speak()
