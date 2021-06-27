
# Creating a class:

class Enemy:
    def __init__(self, AtkLow, AtkHigh):
        self.AttackLow = AtkLow
        self.AttackHigh = AtkHigh


# Using the class #

Enemy1 = Enemy(30, 80)
Enemy2 = Enemy(20, 60)

print(Enemy1.AttackLow)
print(Enemy2.AttackLow)
print(Enemy1.AttackHigh)
print(Enemy2.AttackHigh)

# NOTE:  "Self" is the short-cut way to refer to the current object

# ===========================
# Creating a class for Laptop:
# ============================

class Laptop:
    def __init__(self, name, model, price ):
        self.name = name
        self.model = model
        self.price = price
        self.laptopspecs = name + "-" + model

# Using the class:

laptop1 = Laptop('HP', 'au114tx', 63000)
laptop2 = Laptop('Lenovo', 'ThinkPad', 58000)

print(f'Laptop1 Name: {laptop1.laptopspecs} and its price is : {laptop1.price}')
print(f'Laptop2 Name: {laptop2.laptopspecs} and its price is : {laptop2.price}')

# NOTE : We can create dervied attributes, for example: 'laptopspecs'; even without defining it in __intt__