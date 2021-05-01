# Basic Calculator #
# =============== #

# ----- Importing Libraries ----- #

import re

# ----- Welcome Message ----- #

print("\n", "The Magical Calculator ", "\n", "======================\n")
print(" Type 'quit' to exit.... \n\n")

# ------ Start of Program ----- #

previous = 0
run = True


def PerformMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input(" Enter Your Equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print(" Have a good day :)")
        run = False
    else:
        equation = re.sub("[a-zA-Z,.%()" "]", "", equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print(" Result: ", previous)


while run:
    PerformMath()


# ------ End of Program ----- #
