# Recursion : function call by itself
# wap to print addition of factors of numbers

def sum(num):
    if num == 0:
        return 0
    else:
        return num+sum(num-1)


num = int(input(" Enter the number : "))
Sum = sum(num)
print(" Addition of factors : ", Sum)
