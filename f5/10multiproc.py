import multiprocessing
import time
from queue import Queue

print("1")
s_t = time.time()
print("2")
t = Queue()
print("3")

def count(n) :
    global t
    print("4")
    for i in range(1,501) :
        t.put(str(str(n)+" "+str(i)))
        print(n,i)
        #print(n,i,"t.get() :",t.get())
        print("count",n,"t.qsize() :",t.qsize())

def printer():
    global t
    print("printer t.qsize() :",t.qsize())
    for i in range(500):
        print(t.get())

print("5")
n_l = ['p1','p2','p3','p4']
print("6")
if __name__ == "__main__" :
    print("7")
    p = multiprocessing.Pool(processes=4)
    print("8")
    p.map(count,n_l)
    print("9")
    p.close()
    print("10")
    p.join()
    print("11")
    print("t get ready")
    
    #for i in range(1000*4) :
    #print(t.get())
    print("t.qsize() :",t.qsize())
    printer()
        
print("12")



print("sec : ",(time.time()-s_t))
'''
map에 도달하면 다시 시작한다.
map에 도달해서 다시 시작하면 __main__은 건너뛴다.
map(함수명, 리스트) 형식으로 넣으면 리스트 내용 갯수에 맞춰서 만들어진다.

'''
'''
C:\workspace\control_data\f5>python 10multiproc.py
1
2
3
5
6
7
8
1
2
3
5
6
12
sec :  0.000997781753540039
4
4
4
4
9
10
11
12
sec :  0.6563031673431396
'''