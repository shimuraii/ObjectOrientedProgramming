class Dog:
    def __init__(self, name, age):
        self.name = name # attribute, self denotes itself
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
dog1 = Dog("Naaaa", 10)
print(dog1.get_name())
print(dog1.get_age())
dog1.set_age(102)
print(dog1.get_age())