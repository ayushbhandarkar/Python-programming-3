# Function with no argument & return value

def sum():
    a = int(input(" Enter the first number "))
    b = int(input(" Enter the second number "))
    add = a + b
    return add      # value of add will get stored in sum()


sum = sum()
print(" Addition : ", sum)
