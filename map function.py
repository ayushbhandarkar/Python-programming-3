Nike = [("shirts", 20.00),
        ("jeans", 30.00),
        ("t-shirts", 18.00),
        ("jacket", 35.00)]

to_rupee = lambda data: (data[0], data[1]*82)

Nike_Store = list(map(to_rupee, Nike))

for i in Nike_Store:
    print(i)
