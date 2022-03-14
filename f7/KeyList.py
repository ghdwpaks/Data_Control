
from unittest import result
from numpy import result_type, true_divide
import Importer as im
from PrintLog import PrintLog  

class KeyList :

    def ReturnList() :
        Table = im.SetClass.GetTable("table.csv")
        #for i in Table : print(i)
        KindOf = [[],[],[],[],[],[],[]]
        '''
        0 : 기준년월
        1 : 장소 시군구명+.+읍면동명
        2 : 성별
        3 : 연령대
        4 : 업종명
        5 : 결재건수
        6 : 결재금액
        '''

        for i in Table :

            KindOf[0].append(i["기준년월"])
            #print('i["기준년월"] :',i["기준년월"])
            KindOf[1].append(str(i["시군구명"])+"."+str(i["읍면동명"]))
            KindOf[2].append(i["성별"])
            KindOf[3].append(i["연령대"])
            KindOf[4].append(i["업종명"])
            KindOf[5].append(i["결제건수"])
            KindOf[6].append(i["결제금액"])
        for i in range(len(KindOf)) :
            KindOf[i] = set(KindOf[i])
            KindOf[i] = list(KindOf[i])
            KindOf[i].sort()
        return KindOf

    def SelectSortSubject() :
        while True :
            Userans = input("""
(선택종료 : exit, e, ㄷ턋, ㄷ)
1. 고유번호
2. 결제건수
3. 결제금액
선택 >""")
            if Userans == "1" or Userans == "고유번호" : return "고유번호"
            elif Userans == "2" or Userans == "결제건수" : return "결제건수"
            elif Userans == "3" or Userans == "결제금액" : return "결제금액"
            else : print("잘못 선택하셨습니다.")


    
    def SelectKindOfSubject(AnsLim=1) :
        PassAble = True
        Result = []
        while PassAble :
            Userans = input("""
(선택종료 : exit, e, ㄷ턋, ㄷ)
1. 장소
2. 성별
3. 연령대
4. 업종명
선택 >""")
            if Userans == "1" or Userans == "장소" :
                Result.append(1)
                if len(Result) > AnsLim : del Result[0]
            elif Userans == "2" or Userans == "성별" :
                Result.append(2)
                if len(Result) > AnsLim : del Result[0]
            elif Userans == "3" or Userans == "연령대" :
                Result.append(3)
                if len(Result) > AnsLim : del Result[0]
            elif Userans == "4" or Userans == "업종명" :
                Result.append(4)
                if len(Result) > AnsLim : del Result[0]
                if len(Result) > AnsLim : del Result[0]
            elif Userans == "exit" or Userans == "e" or Userans == "ㄷ턋" or Userans == "ㄷ" :
                print("선택을 종료합니다.")
                break
            else :
                print("선택이 잘못됐습니다.")
                continue
        Result = set(Result)
        Result = list(Result)
        Result.sort()
        return Result



    def SelectKindOf(SubNum):
        #SubNum = [1,3,4]
        KindOf = KeyList.ReturnList()
        Result = []
        for i in range(len(SubNum)) :
            Result.append([])
        for i in range(len(SubNum)):
            PrintLog.print_div_6(KindOf[SubNum[i]])
            while True :
                UserInput = input("\n선택 :")
                if UserInput == "exit" or UserInput == "e" or UserInput == "ㄷ턋" or UserInput == "ㄷ" :
                    print("입력을 종료합니다.")
                    break
                if UserInput in KindOf[SubNum[i]] :
                    Result[i].append(UserInput)
                else :
                    print("다시 선택해주세요.")
        return Result

