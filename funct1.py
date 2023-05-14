# Function with no argument & no return value

def display():
    a = int(input(" Enter the value of a : "))
    b = int(input(" Enter the value of b : "))
    print(" A : ", a)
    print(" B : ", b)
    print(" Addition : ", a + b)


choice = int(input(" Enter your choice : "))
for i in range(choice):
    print("")
    display()
