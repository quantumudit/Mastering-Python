
# Creating functions within the class:

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def fullName(self):
        return f'{self.first_name} {self.last_name}'

    def Is_Above_18(self):
        return self.age > 18

# Creating objects/instance:

p1 = Person('Udit', 'Chatterjee', 16)

full_name = p1.fullName()
age_valid = p1.Is_Above_18()

print(full_name)
print(age_valid)

# ===========================
# Creating a class for Laptop:
# ============================

class Laptop:
    def __init__(self, name, model, price ):
        self.name = name
        self.model = model
        self.price = price
        self.laptopspecs = name + "-" + model
    
    def DiscountedPrice(self, discount):
        off_price = self.price * (discount /100)
        return self.price - off_price

# Using the class:

laptop1 = Laptop('HP', 'au114tx', 63000)
laptop2 = Laptop('Lenovo', 'ThinkPad', 58000)

l1_discounted_price = laptop1.DiscountedPrice(15)
print(f'The {laptop1.laptopspecs} price is: {laptop1.price} and the price fall to {l1_discounted_price} on sale')

# NOTE: Instance variables are defined with 'self.' in __init__ method and then, we can write functions and other transformation.
# We can pass additional variables in functions that needs to be passed during the function call ( no need of 'self.')
# 'self' needs to be there as the first argument in any function; defined within the class
# The name 'self' is just a convention and can be given any other name but, its the first variable that is taken as "instance variable"