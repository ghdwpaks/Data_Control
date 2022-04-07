
import threading
import copy as c
import csv
from queue import Queue
import time

secs = time.time()
globali = 0
from cv2 import RNG_NORMAL
table = Queue()

def get_table(filepath) :
    with open(filepath,'r') as f :
        reader = csv.DictReader(f)
        for row in reader : table.put(row)
result_file_path = "result.txt"
def print_table() :
    global globali
    #scope,filepath="result.txt",thread_prinum = 1
    #scope : 반복문의 길이
    #thread_prinum : 오류검출시 필요한 변수. 스레드의 고유번호를 뜻한다.
    '''
    # writedata.py
    f = open("C:/doit/새파일.txt", 'w')
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()
    '''
    print("scope :",scope)
    
    for i in range(scope) :
        
        try :
            row = table.get()
            globali+=1
            #f.write(str(row)+"\n")
            #print("print_table type(row) :",type(row)) # <Class 'dict'>
            table.put(row)
            
        except :
            break
    
def get_scope(thread_count) :
    len_table = table.qsize()
    print("len_table :",len_table)
    scope = len_table//thread_count
    len_else = len_table%scope
    return scope,len_else
get_table("table.csv")
thread_count = 20
scope,len_else = get_scope(thread_count)
print(scope,len_else)

for i in range(thread_count) :
    thread = threading.Thread(target=print_table)
    thread.start()
    thread.join()
thread = threading.Thread(target=print_table)
thread.start()
print("globali :",globali)
print(time.time()-secs)

