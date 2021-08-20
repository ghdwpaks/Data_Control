from os import rename
import threading
import time
import csv
from queue import Queue


queue = Queue()  # 크기가 1인 버퍼


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
                queue.put(table[0:div_size])
            elif k >= len(table) :
                queue.put(table[len(table)-div_size:])
            elif k%div_size == 0 and k != 0 :
                queue.put(table[k-div_size:k])
        pass

    def setting_column_on_queue() :
        res = []
        table = queue.get()
        #print("setting column on queue table :")
        #prints.print_list(table)
        for i in table :
            #print("i :",i)
            try:
                # 무언가를 수행한다.
                print('i :',i)
                temp_li = [i["품목명"],i["단위"],i["등급"],i["가격"]]
                #print("temp_li :",temp_li)
            finally:
                pass
            #print("setting_column tmp_li :",temp_li)
            if not i in res :
                #print(i)
                res.append(temp_li)
        queue.put(res)
        #return res




res = []
thread_count = 6
table = []
for i in range(1) :
    start = time.time()  # 시작 시간 저장
    table = []
    table = setting.get_table("ttable.csv")
    setting.setting_queue(table)
        
    for j in range(thread_count) :
        print("thread {} entered ".format(j))
        thread = threading.Thread(target=setting.setting_column_on_queue)
        thread.start()
    thread.join()

    table = []
    '''
    for j in temp_tables :
        table += j
    '''
    
    big_cat = selects.select_lv1_category(table)

    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    res.append(round(time.time() - start,2))
print("table :")
prints.print_list(table)
for i in res :
    print(i)
