# Loops #
# ===== #

Programs = ['Java', 'Scala', 'Javascript', 'R', 'Python', 'C', 'Python', 'C++']

for item in Programs:
    print("The Program name is: ", item)

# While loop

run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1
