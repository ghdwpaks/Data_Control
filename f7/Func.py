

import os
import Importer as im

class Func :
    def InputDate() :
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
            if EndPoint == "" or int(EndPoint[:4]) >= 2020:
                print("종단기간을 미응답 2020년 11월까지로 설정하였습니다.")
                EndPoint="2020-11"
                break
            elif (int(EndPoint[:4]) <= 2020 and int(EndPoint[:4]) >= int(StartPoint[:4]) and int(EndPoint[4:]) <= 12 and int(EndPoint[4:]) >= 00)or(EndPoint[:4]>StartPoint[:4]):
                EndPoint = str(EndPoint[:4])+"-"+str(EndPoint[4:])
                break
            else :
                print("다시 입력해주세요")
                continue
        #StartPoint="2019-04" , EndPoint="2020-11"
        return [StartPoint, EndPoint]


    def Year2Num(date) :
        
        if len(date)>6 :
            #date = "2019-04"
            return str(int(date.split("-")[0])*365+int(date.split("-")[1])*30)
            #return = 737085
        elif len(date)<=6 :
            #date = "201904"
            return str(int(date[:4]*365)+int(date[4:]*30))
            #return = 737085
    def Num2Year(date) :
        #date = 737085
        return str(int(date)//365)+"-"+im.Func.FillUp0(str(int(date)%365//30),2)

    #Come from git project ghdwpaks/dc
    def FillUp0(i,byte=4) :
        #i = "10"
        i = list(i)
        while True :
            if len(i) < byte :
                i.insert(0,"0")
            else :
                break
        return "".join(i)


    def PrintToDate(table) :
        print("기간별 출력을 선택하셨습니다.")
        
        StartPoint, EndPoint = im.Func.InputDate()
        Table = im.SetClass.ApplyPeriod(table,StartPoint,EndPoint)
        subject = im.KeyList.SelectSortSubject()
        Return = im.SetClass.ApplySort(Table,subject)
        return Return
        
    
    def PrintToSub(table) :
        print("종목별 출력을 선택하셨습니다.")
        Table = im.SetClass.ApplyPriNum(table)
        Table = im.SetClass.ApplyLoc(Table)
        Subject = im.KeyList.SelectKindOfSubject(5)
        Subject = im.KeyList.SelectKindOf(Subject)
        Result=[]
        
        '''
        print("Subject :",Subject)
        print("len(Subject) :",len(Subject))
        print("Table[0] :",Table[0])
        print("list(Table[0].values()) :",list(Table[0].values()))
        CorrCount = 0
        for i in range(len(Subject)):
            for j in range(len(Subject[i])) :
                print("Subject[",i,"][",j,"] :",Subject[i][j])
                print("list(Table[0].values()) :",list(Table[0].values()))
                print("Subject[",i,"][",j,"] in list(Table[0].values()) :",Subject[i][j] in list(Table[0].values()) )
                if Subject[i][j] in list(Table[0].values()) :
                    CorrCount += 1
                    break
            if CorrCount >= len(Subject) :
                Result.append(Table[0])
        print("Result :",Result)
        os.system("pause")
        '''

        for k in range(len(Table)) :
            CorrCount = 0
            for i in range(len(Subject)):
                for j in range(len(Subject[i])) :
                
                
                    if Subject[i][j] in list(Table[k].values()) :
                        CorrCount += 1
                        break
                if CorrCount >= len(Subject) :
                    Result.append(Table[k])
        Subject = im.KeyList.SelectSortSubject()
        Result = im.SetClass.ApplySort(Result,Subject)
                
        im.PrintLog.Write(Result)
        

