# def add(a, b):
#     print(a + b)
#
#
# add(10, 20, 30)

def add(*args):
    sum = 0
    for value in args:
        sum += value
        print(value)
    print("Addition : ", sum)


add(10, 20, 30)
