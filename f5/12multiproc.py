import multiprocessing
import time
s_t = time.time()

def count(n) :
    print("4")
    for i in range(10) :
        print(n,i)


n_l = ['p1','p2','p3','p4']
p = multiprocessing.Pool(processes=1)
p.map(count,n_l)
p.close()
p.join()