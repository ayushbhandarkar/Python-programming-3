from threading import Thread, currentThread


def disp():
    print(" Child Thread Name: ", currentThread().getName())


t = Thread(target=disp)
t.start()

print(" Main Thread Name: ", currentThread().getName())

# Output:

