import threading
import time

num = 0
class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName(),"num :",num)
        if num == 1 :
            print("1")
            funcs.f1(num)
        elif num == 2:
            print("2")
            funcs.f2(num)
        time.sleep(3)
        print("sub thread end ", threading.currentThread().getName())
class funcs() :
    def f1(n=1) :
        print("f1 n :",n)
    def f2(n=2) :
        print("f2 n :",n)


print("main thread start")
for i in range(5):
    name = "thread {}".format(i)
    t = Worker(name)                # sub thread 생성
    num = 1
    t.start()                    # sub thread의 run 메서드를 호출
num =2
t.start()
print("main thread end")