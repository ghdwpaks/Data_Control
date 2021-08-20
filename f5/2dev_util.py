table = []
div_code = []
thread_count = 6

from queue import Queue


queue = Queue()  
for k in range(len(table)+1) :
    if k == thread_count :
        queue.put(table[0:thread_count])
    elif k >= len(table) :
        queue.put(table[len(table)-thread_count:])
    elif k%thread_count == 0 and k != 0 :
        queue.put(table[k-(thread_count-1):k+1])