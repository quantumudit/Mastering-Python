# The difference between class method and instance method

class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def CountIns(cls):
        return f'You have created {cls.count_instance} of {cls.__name__} class'


    def FullName(self):
        return f'{self.first_name} {self.last_name}'
    
    def IsAbove18(self):
        return self.age > 18
    
p1 = Person('Udit', 'Chatterjee', 16)
p2 = Person('John', 'Mercer', 24)

print(Person.CountIns())