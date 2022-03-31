class Person:

    def __init__ (self, name, age):

        if not isinstance(name, str):
            raise TypeError("Name must be string")
        if not isinstance(age, int):
            raise TypeError("Age must be integer")

        self.name = name
        self.age = age



    def compare_age(self, another_person):
        if self.age < another_person.age:
            return f'{another_person.name} is older than me'
        elif self.age == another_person.age:
            return f'{another_person.name} is the same age as me'
        elif self.age > another_person.age:
            return f'{another_person.name} is younger than me'
