import time
import threading


def calc_square(nums):
    print("Calculate square of numbers ")
    for n in nums:
        time.sleep(0.2)
        print("Square:", n*n)


def calc_cube(nums):
    print("Calculate Cube of numbers ")
    for n in nums:
        time.sleep(0.2)
        print("Cube:", n*n*n)


arr = [2, 3, 8, 9]

t = time.time()     # here we are calculating how much time functions will take to run the code / execute
# calc_square(arr)
# calc_cube(arr)
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Done in :", time.time() - t, " sec")
