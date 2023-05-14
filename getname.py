from threading import Thread, current_thread


def disp():
    pass


t = Thread(target=disp, name="New Thread")
print(t.name)

# Output:
# New Thread
