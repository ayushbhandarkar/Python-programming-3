from threading import Thread, currentThread


def disp():
    print(" Child Thread ", currentThread())


t = Thread(target= disp)
t.start()

print(" Main Thread", currentThread())
