class Person:
    number_of_people = 0
    GRAVITY = -9.8
    def __init__(self, name):
        self.name = name
        Person.add_person()
#        Person.number_of_people += 1
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
p1 = Person("Tim")
p2 = Person("Gustavo")
p3 = Person("Ubial")
print(Person.number_of_people_())
