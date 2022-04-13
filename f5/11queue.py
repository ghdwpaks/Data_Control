from queue import Queue

q = Queue()

q.put(1)
print(q.get())


def fp():
    q.put(2)

fp()
print(q.get())


