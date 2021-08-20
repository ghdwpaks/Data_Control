from os import rename
import threading
import time
import csv







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

    def setting_column(table) :
        res = []
        for i in table :
            temp_li = [i["품목명"],i["단위"],i["등급"],i["가격"]]
            #print("setting_column tmp_li :",temp_li)
            if not i in res :
                #print(i)
                res.append(temp_li)
        return res

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정
    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(5)
        print("sub thread end ", threading.currentThread().getName())
    def thread_setting_column(self,table) :
        res = []
        print("start thread_setting_column self : ",self)
        for i in table :
            temp_li = [i["품목명"],i["단위"],i["등급"],i["가격"]]
            #print("setting_column tmp_li :",temp_li)
            if not i in res :
                #print(i)
                res.append(temp_li)
                
        time.sleep(3)
        print("end thread_setting_column self : ",self)
        return res
        pass





res = []
thread_count = 6
for i in range(1) :
    start = time.time()  # 시작 시간 저장
    table = []
    table = setting.get_table("ttable.csv")
        
    temp_tables = []
    for j in range(thread_count) :
        temp_tables.append([])
    
    for j in range(thread_count) :
        name = "thread {}{}".format(j,j)
        t = Worker(name)
        #t.daemon = True
        temp_res = t.thread_setting_column(table)
        temp_tables[j] = temp_res

    table = []
    for j in temp_tables :
        table += j

        

    #table = setting.setting_column(table)
    big_cat = selects.select_lv1_category(table)

    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    res.append(round(time.time() - start,2))
'''print("table :")
prints.print_list(table)'''
for i in res :
    print(i)
