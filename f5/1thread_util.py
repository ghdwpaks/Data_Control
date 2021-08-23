from os import rename, truncate
import os
import threading
import time
import csv
from queue import Queue
import copy


table_queue = Queue()  # 크기가 1인 버퍼


class prints :
    def print_list(table) :
        for i in table :
            print(i)
    
class selects :

    def select_lv1_category(table) :
        res = []
        for i in table :
            temp_li = str(i[0]).split("]")
            temp_li = list(temp_li)
            del temp_li[0]
            temp_li = "".join(temp_li)
            if temp_li not in res :
                res.append(temp_li)
        return res
    
    def select_lv2_category(table,cat_name) :
        res = []
        for i in table :
            #print("select lv2 category i:",i)
            if cat_name in i[0] :
                if i not in res :

                    print("select lv2 category appending culomn :",i)
                    res.append(i)

        #prints.print_list("select lv2 category res :",res)
        return res

class setting :

    def get_table(filepath) :
            #table.csv
            table = []
            with open(filepath,'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    table.append(row)
                    #print(row)
            return table

    def setting_queue(table) :
        global thread_count
        div_size = len(table)//thread_count
        for k in range(len(table)) :
            if k == div_size :
                table_queue.put(table[0:div_size])
            elif k >= len(table) :
                table_queue.put(table[len(table)-div_size:])
            elif k%div_size == 0 and k != 0 :
                table_queue.put(table[k-div_size:k])
        pass

    def synchronization_queue_to_table(table) :
        for i in table :
            table_queue.put(i)
        pass

    def setting_column_on_queue() :
        while True :
            #whatget = 0
            try :
                #print("queue.qsize() :",queue.qsize())
                table_tuple = table_queue.get()
                #whatget = copy.deepcopy(table_tuple)
                #print("setting column on queue table_tuple :",table_tuple)
                #temp_li = [table[i]["품목명"],table[i]["단위"],table[i]["등급"],table[i]["가격"]]
                table_queue.put([table_tuple["품목명"],table_tuple["단위"],table_tuple["등급"],table_tuple["가격"]])
            except :
                #print("whatget :",whatget)
                break
        #return res

os.system("cls")


res = []
thread_count = 12
table = []
for i in range(1) :
    start = time.time()  # 시작 시간 저장
    table = []
    table = setting.get_table("ttable.csv")
    #setting.setting_queue(table)
    setting.synchronization_queue_to_table(table)
    lentable = len(table)
    print("main queue.qsize() :",table_queue.qsize())
    for j in range(thread_count) :
        #print("thread {} entered ".format(j))
        thread = threading.Thread(target=setting.setting_column_on_queue)
        thread.start()
    for j in range(table_queue.qsize() % thread_count) :
        setting.setting_column_on_queue()

    
    table = []
    '''
    for j in temp_tables :
        table += j
    '''
    
    big_cat = selects.select_lv1_category(table)

    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    res.append(round(time.time() - start,2))
queueres = []
for i in range(table_queue.qsize()) :
    queueres.append(table_queue.get())
#print("queueres :")
#prints.print_list(queueres)
for i in res :
    print(i)
