from multiprocessing import Process, Queue
import csv
import queue
import time
from multiprocessing import Process,Queue
from queue import Queue

secs = time.time()
table = Queue()
globali = 0
with open("table.csv",'r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        table.put(row)
def work() :
    print("th")
    global globali,table
    lentable = table.qsize()
    print("table.qsize :",table.qsize())
    while globali < lentable:
        #row = table.get()
        globali+=1
        print(globali)
        #table.put(row)

if __name__ == "__main__":
    
    '''
    print("start")
    procs = []
    for i in range(20) :
        th = Process(target=work)
        procs.append(th)
    for i in range(20) :
        procs[i].start()
        procs[i].join()
    '''
    th1 = Process(target=work)
    th2 = Process(target=work)
    th3 = Process(target=work)
    th4 = Process(target=work)
    th5 = Process(target=work)
    th6 = Process(target=work)

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
    th6.join()

    print("globali :",globali)





    print(time.time()-secs)
#137.5068919658661
#137.4435727596283