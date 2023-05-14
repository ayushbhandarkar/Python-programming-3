# wap to implement active_count()  function
import threading
from threading import Thread

def disp1(num1, num2):
    for i in range(5):
        print(" This function is executed by user-define thread ", num1 + num2)

def disp2():
    print(" This function is executed by main thread")


t_obj = Thread(target=disp1, args=(10, 30))
t_obj.start()

count = 0

for j in range(5):
    disp2()
    count = threading.active_count()

print(" No. of threads active : ", count)
