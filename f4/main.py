import copy as c
import csv

from numpy import append


def get_table(filepath) :
        table = []
        with open(filepath,'r') as f :
            reader = csv.DictReader(f)
            for row in reader :
                table.append(row)
                #print(row)
        return table

table = get_table("table.csv")
#for i in table : print(i)

#{'1': '[파인애플]파인애플(수입)', '2': '12kg', '3': '특(1등)', '4': '20000', '5': '필리핀', '6': '일반', '7': '20210331'}
#"품목명","단위","등급","가격","산지","친환경구분","입력일"

#품목명, 단위, 등급, 가격, 입력일만을 담은 테이블 생성
table_min_ops = []
#print([table[1]["1"],table[1]["2"],table[1]["3"],table[1]["7"]])
for i in range(len(table)):
    table_min_ops.append([table[i]["1"],table[i]["2"],table[i]["3"],table[i]["4"],table[i]["7"]])

print("len(table) :",len(table))
print("len(table_min_ops) :",len(table_min_ops))

#for i in table_min_ops : print(i)

#평균 가격 테이블
avgs = []

#품목명, 단위, 등급 이 동일한 값끼리 모아놓은 테이블
collected_ops = []

#['[고추]꽈리고추', '.2kg', '특(1등)', '2200', '20210401']
temp_same = [table_min_ops[0]]
print("temp_same :",temp_same)
print('temp_same[-1][-1] :',temp_same[-1][-1])
counts = 0
for i in range(len(table_min_ops)) :
    try :
        if (str(temp_same[-1][0])+str(temp_same[-1][1])+str(temp_same[-1][2])==str(table_min_ops[i][0])+str(table_min_ops[i][1])+str(table_min_ops[i][2]) and not i == 20-1) :
            #print(str(temp_same[-1][0])+str(temp_same[-1][1])+str(temp_same[-1][2])==str(table_min_ops[i][0])+str(table_min_ops[i][1])+str(table_min_ops[i][2]))
            #print("str(temp_same[-1][0])+str(temp_same[-1][1])+str(temp_same[-1][2]) :",str(temp_same[-1][0])+str(temp_same[-1][1])+str(temp_same[-1][2]))
            #print("str(table_min_ops[i][0])+str(table_min_ops[i][1])+str(table_min_ops[i][2]) :",str(table_min_ops[i][0])+str(table_min_ops[i][1])+str(table_min_ops[i][2]))
            #print("temp_same :")
            #for j in temp_same : print(j)
            temp_same.append(table_min_ops[i])
            counts+=1
        else :
            #print("active else")
            temp_same.append(table_min_ops[i])
            collected_ops.append(temp_same)
            temp_same = [table_min_ops[i+1]]
            counts+=1
    except :
        #print("오류 발생")
        #print("i :",i)
        #print('str(temp_same[-1]["1"])+str(temp_same[-1]["2"])+str(temp_same[-1]["3"]) :',str(temp_same[-1]["1"])+str(temp_same[-1]["2"])+str(temp_same[-1]["3"]))
        #print("table_min_ops[i] :",table_min_ops[i])
        continue
print("collected_ops :")
for i in collected_ops : print(i)

#try except문으로 빠져서 collected_ops에 담기지 않은 값이 있는지 길이를 비교하기
print("len(table_min_ops) :",len(table_min_ops))
print("counts :",counts)

    




