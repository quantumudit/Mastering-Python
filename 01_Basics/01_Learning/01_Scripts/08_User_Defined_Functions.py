# Functions in Python #
# =================== #

def NothingMuch():
    print("This function does nothing")


NothingMuch()

# Functions with arguments


def StringConcat(str1, str2):
    print(str1 + ", " + str2)


StringConcat("Apple", "Banana")

# Function with default values


def DescribePerson(name="YOUR NAME", age="YOUR AGE"):
    print("My name is ", name, "and my age is ", age)


DescribePerson("Udit", 26)

# Calling just the age with keyword argument

DescribePerson(age=35)

# Infinite number of arguments in a function


def PrintPeople(*people):
    for person in people:
        print("This person is ", person)


PrintPeople("Nick", "Jack", "Solomon", "Darwin", "Gordon")
