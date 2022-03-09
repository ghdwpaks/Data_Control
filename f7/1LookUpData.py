from Set import SetClass
import csv
import time

start = time.time()  # 시작 시간 저장

table = SetClass.get_table("table.csv")
#for i in table : print(i)
#print("type(table) :",type(table))
#print("type(table[0]) :",type(table[0]))
LocationList = []
for i in table :
    LocationList.append(str(i["시군구명"])+"."+str(i["읍면동명"]))
LocationList = set(LocationList)
LocationList = list(LocationList)
LocationList.sort()
for i in LocationList :
    print(i)
print(table[0].keys())
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
