
def find_sum(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum+i
    return sum


result = find_sum(5)
print(" Sum of number ", result)
