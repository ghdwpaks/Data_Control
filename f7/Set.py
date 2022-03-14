import copy as c
import csv
from re import sub
from unittest import result

import Importer as im

class SetClass :
    
    def GetTable(filepath) :
            #table.csv
            table = []
            with open(filepath,'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    table.append(row)
                    #print(row)
            return table

    def ApplyPriNum(Table) :
        for i in range(len(Table)) :
            Table[i].update({"고유번호":i+1})
        return Table





    def ApplyPeriod(Table,StartTime=737055,EndTime=737630) :
        #{'기준년월': '2020-11', '시군구명': '권선구', '읍면동명': '고색동', '성별': '여', '연령대': '10대', '업종명': '약국', '결제건수': '4', '결제금액': '15500', '데이터기준일자': '2020-12-11', '고유번호': 103}
        '''
        0 : 기준년월
        1 : 장소 시군구명+.+읍면동명
        2 : 성별
        3 : 연령대
        4 : 업종명
        5 : 결재건수
        6 : 결재금액
        '''
        for i in range(len(Table)) :
            Table[i]["기준년월"] = str(int(Table[i]["기준년월"].split("-")[0])*365+int(Table[i]["기준년월"].split("-")[1])*30)
            Table[i]["지역"] = str(Table[i]["시군구명"])+"."+str(Table[i]["읍면동명"])
            del Table[i]["시군구명"]
            del Table[i]["읍면동명"]
            del Table[i]["데이터기준일자"]
        #for i in Table : print(i)
        SetClass.ApplyPriNum(Table)
        #im.PrintLog.Write(Table)
        #{'기준년월': '737630', '성별': '남', '연령대': '20대', '업종명': '보건위생', '결제건수': '12', '결제금액': '149000', '지역': '권선구.고색동', '고유번호': 14}
        Result=[]
        StartTime = int(im.Func.Year2Num(StartTime))
        EndTime = int(im.Func.Year2Num(EndTime))
        for i in range(len(Table)):
            if StartTime <= int(Table[i]["기준년월"]) and int(Table[i]["기준년월"]) <= EndTime :
                Result.append(Table[i])
            
        for i in range(len(Result)) :
            Result[i]["기준년월"] = im.Func.Num2Year(Result[i]["기준년월"])
        im.PrintLog.Write(Result)
        return Result





    def ApplySort(Table,Sub="결제금액",Reverse=True) :
        TempTable = []
        Str2IntAble = SetClass.CheckAbleStr2Int(Table[0][Sub])
        print("Str2IntAble :",Str2IntAble)
        for i in range(len(Table)) :
            if Str2IntAble :
                #문자열(기본) => 정수 가능
                TempTable.append([int(Table[i][Sub]),Table[i]["고유번호"]])
            else :
                TempTable.append([Table[i][Sub],Table[i]["고유번호"]])
        #for i in TempTable : print(i)
        TempTable.sort(reverse=Reverse,key=lambda x : (x[0], x[1]))
        for i in TempTable : print(i)
        Result = c.deepcopy(TempTable)
        for i in range(len(Result)) :
            for j in range(len(Table)) :
                if Result[i][1] == Table[j]["고유번호"] :
                    Result[i] = c.deepcopy(Table[j])
                    break
        
        im.PrintLog.Write(Result) 

                

        
    def CheckAbleStr2Int(var) :
        AboutAble = False
        try : 
            tmp = int(var)
            AboutAble = True
        except :
            AboutAble = False
        return AboutAble



        
        


        

        