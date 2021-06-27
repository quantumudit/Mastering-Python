
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