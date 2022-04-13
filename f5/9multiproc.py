from multiprocessing import Process, Queue
from time import time
def f(q,start):
    print("start :",start)
    for j in range(200) :
        print("j :",j)
        q.put([str(time()-start)[:4], "ghd", j])
    

if __name__ == '__main__':
    q = Queue()
    start = time()
    p = Process(target=f, args=(q,start,))
    p1 = Process(target=f, args=(q,start,))
    p2 = Process(target=f, args=(q,start,))
    p3 = Process(target=f, args=(q,start,))
    p4 = Process(target=f, args=(q,start,))
    p5 = Process(target=f, args=(q,start,))

    p.start()
    p1.start()
    p2.start()  
    p3.start()
    p4.start()
    p5.start()


    p.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()


    print("main while true start")
    while True :
        try :
            print(q.get())    # prints "[42, None, 'hello']"
        except :
            print("끝")
            break