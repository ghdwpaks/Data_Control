import turtle
from numpy import true_divide
from Set import SetClass
from KeyList import KeyList
from Log import Log
import csv

table = SetClass.GetTable("table.csv")
#for i in table :print(i)
print("type(table) :",type(table))
print("type(table[0]) :",type(table[0])) 


class Func :
    def PrintToDate(table) :
        print("기간별 출력을 선택하셨습니다.")
        kl = KeyList.ReturnList()
        #print("kl 1 :",kl)
        for i in range(len(kl[0])) :
            print(kl[0][i],end="\n")
        
        while True :
            StartPoint = input("출력을 원하는 시작기간(ex.201904)을 입력해주세요.(미입력시 2019년 4월부터)\n")
            if StartPoint == "" :
                print("시작기간을 미응담 2019년 05월까지로 설정하였습니다.")
                StartPoint="2019-04"
                break
            elif (int(StartPoint[:4]) <= 2020 and int(StartPoint[:4]) >= 2019) and (int(StartPoint[4:]) <= 12 and int(StartPoint[4:]) >= 00) :
                StartPoint = str(StartPoint[:4])+"-"+str(StartPoint[4:])
                break
            else :
                print("다시 입력해주세요")
                continue
                
        while True :
            EndPoint = input("출력을 원하는 종단기간(ex.202011) 입력해주세요.(미입력시 2020sus 11월까지)\n")
            if EndPoint == "" :
                print("종단기간을 미응답 2020년 07월까지로 설정하였습니다.")
                EndPoint="2020-11"
                break
            elif (int(EndPoint[:4]) <= 2020 and int(EndPoint[:4]) >= int(StartPoint[:4]) and int(EndPoint[4:]) <= 12 and int(EndPoint[4:]) >= 00)or(EndPoint[:4]>StartPoint[:4]):
                EndPoint = str(EndPoint[:4])+"-"+str(EndPoint[4:])
                break
            else :
                print("다시 입력해주세요")
                continue
        print("StartPoint :",StartPoint)
        print("EndPoint :",EndPoint)
        Times=[]

        Result = []
        for i in range(len(table)) :
            if (table[i]["기준년월"].split("-")[1] >= StartPoint.split("-")[1]) or (table[i]["기준년월"].split("-")[1] <= EndPoint.split("-")[1]):
                Result.append(table[i])
        print(len(Result))
        print(Result[0])
        Log.Write(Result)
        return Result
        
            
        


while True :
    print("""
    1. 기간별 출력(월단위)
    2. 결재건수별 출력
    """)
    UserAnswer = input()
    if UserAnswer == "1" :
        print("기간별 출력을 선택하셨습니다.")
        Func.PrintToDate(table)
    elif UserAnswer == "2" :
        print("결개건수별 출력을 선택하셨습니다.")
    else : continue
