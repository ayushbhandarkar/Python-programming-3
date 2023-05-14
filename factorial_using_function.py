# Recursion : function call by itself
# wap to print Factorial of numbers

def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)


num = int(input(" Enter the number : "))
Fact = fact(num)
print(" Factorial of Number : ", Fact)
