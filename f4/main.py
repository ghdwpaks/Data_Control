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

#{'1': '[파인애플]파인애플(수입)', '2': '12kg', '3': '특(1등)', '4': 'x000', '5': '필리핀', '6': '일반', '7': '20210331'}
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
for i in range(100) :
    try :
        if (str(temp_same[-1][0])+str(temp_same[-1][1])+str(temp_same[-1][2])==str(table_min_ops[i][0])+str(table_min_ops[i][1])+str(table_min_ops[i][2])) :
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
            temp_avgs_pri = 0
            print("temp_same :",temp_same)
            #print("temp_avgs_pri 1:",temp_avgs_pri)
            for k in range(len(temp_same)):
                print("temp_same[k] :",temp_same[k])
                print("temp_same[k][3] :",temp_same[k][3])
                temp_avgs_pri += int(temp_same[k][3])
            print("temp_avgs_pri 2:",temp_avgs_pri)
            
            collected_ops.append([temp_same[0][0],temp_same[0][1],temp_same[0][2],temp_avgs_pri,temp_same[0][4]])
            temp_same = [table_min_ops[i+1]]
            counts+=1
    except :
        
        print("오류 발생")
        print("i :",i)
        print('str(temp_same[-1][0])+str(temp_same[-1][1])+str(temp_same[-1][2]) :',str(temp_same[-1][0])+str(temp_same[-1][1])+str(temp_same[-1][2]))
        print("str(table_min_ops[i][0])+str(table_min_ops[i][1])+str(table_min_ops[i][2]) :",str(table_min_ops[i][0])+str(table_min_ops[i][1])+str(table_min_ops[i][2]))
        print("table_min_ops[i] :",table_min_ops[i])
        break
print("collected_ops :")
for i in collected_ops : print(i)

#try except문으로 빠져서 collected_ops에 담기지 않은 값이 있는지 길이를 비교하기
print("len(table_min_ops) :",len(table_min_ops))
print("counts :",counts)

'''
지금 현재 보면 뭔가 이상하다는것을 볼 수 있다.
'[쪽파]쪽파(일반)'의 경우에는 중간에 중복이 많이 들어간것도 보이고
10kg 하던게 1kg이 중간에 껴버리니까 양쪽으로 나뉘어져서 값이 여러개 또 들어간것을 볼 수 있다.
최초정렬했을때의 컬럼들이 이름순으로 일정하지 않은건지는 몰라도 이러한 양분화를 다시 정리하는 코드가 필요할거같다.

그리고 가장 마지막에 입력된 날짜를 기준으로만 출력하는 기능도 필요해보인다.

이렇다면 '서로 다른 날짜에 입력된 데이터'의 평균이 아니라 '서로 다른 무게'의 평균으로 내야할거같다.


collected_ops :
['[쪽파]쪽파', '1kg', '특(1등)', 42900, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 315700, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 111000, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 74500, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 34400, '20210331']
['[쪽파]쪽파(일반)', '1kg', '특(1등)', 23600, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 50000, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 44600, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 199000, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 131000, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 68000, '20210331']
['[쪽파]쪽파(일반)', '10kg', '특(1등)', 86000, '20210331']
['[쪽파]포장쪽파', '10kg', '특(1등)', 252500, '20210331']
['[쭈꾸미국산]쭈꾸미국산', '5kg', '보통(3등)', 208000, '20210331']
['[쭈꾸미수입]쭈꾸미수입', '2kg', '보통(3등)', 44000, '20210331']
['[쭈꾸미수입]쭈꾸미수입', '2kg', '보통(3등)', 55400, '20210331']
['[쭈꾸미수입]쭈꾸미수입', '2kg', '보통(3등)', 108700, '20210331']
['[참나물]참나물', '4kg', '특(1등)', 31000, '20210331']
['[참나물]참나물(일반)', '4kg', '특(1등)', 29000, '20210331']
['[참다래(키위)]참다래(키위)', '10kg', '특(1등)', 587000, '20210331']
len(table_min_ops) : 466088
counts : 100
'''


