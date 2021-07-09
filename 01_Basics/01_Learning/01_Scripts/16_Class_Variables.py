
# Class Variable #
# ============== #

# Creating a 'Circle' Class

class Circle:

    pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    def Circumference(self):
        return 2 * self.radius * Circle.pi

# Creating object:

c1 = Circle(4)
print(c1.Circumference())

# NOTE: Here 'pi' is class variable and called as 'ClassName.' in any function

# ===========================
# Creating a class for Laptop:
# ============================

class Laptop:

    SaleDiscount = 10

    def __init__(self, name, model, price ):
        self.name = name
        self.model = model
        self.price = price
        self.laptopspecs = name + "-" + model
    
    def DiscountedPrice(self):
        off_price = self.price * (Laptop.SaleDiscount /100)
        return self.price - off_price

# Using the class:

laptop1 = Laptop('HP', 'au114tx', 63000)
laptop2 = Laptop('Lenovo', 'ThinkPad', 58000)

l1_discounted_price = laptop1.DiscountedPrice()
print(f'The {laptop1.laptopspecs} price is: {laptop1.price} and the price fall to {l1_discounted_price} on sale')

# Changing the class variable
# ===========================

# We can change the defined class variable during execution:

Laptop.SaleDiscount = 30

laptop3 = Laptop('Dell', 'alienware', 89000)

l3_disc = laptop3.DiscountedPrice()
print(f'The changes discount for laptop3 is {l3_disc}')

# NOTE: We can define the class variable in such a way that will only be used if there is no self (instace) declaration; for example:

class Person:

    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Amit', 'Dash', 27)
p2 = Person('Udit', 'Chatterjee', 26)
p3 = Person('Sacchi', 'Dehury', 26)

print(f'No. of person: {Person.count_instance}')
