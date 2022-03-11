

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
        kl = im.KeyList.ReturnList()
        #print("kl 1 :",kl)
        #for i in range(len(kl[0])) :print(kl[0][i],end="\n")
        
        StartPoint , EndPoint = Func.InputDate()
        
        print("StartPoint :",StartPoint)
        print("EndPoint :",EndPoint)
        Times=[]

        Result = []
        for i in range(len(table)) :
            if (table[i]["기준년월"].split("-")[1] >= StartPoint.split("-")[1]) or (table[i]["기준년월"].split("-")[1] <= EndPoint.split("-")[1]):
                Result.append(table[i])
        print(len(Result))
        print(Result[0])
        im.PrintLog.Write(Result)
        return Result
        
            
        

