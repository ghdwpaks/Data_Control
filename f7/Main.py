
import Importer as im



table = im.SetClass.GetTable("table.csv")
table = im.SetClass.ApplyPriNum(table)
#for i in table :print(i)
print("type(table) :",type(table))
print("type(table[0]) :",type(table[0])) 


while True :
    print("""
    1. 기간별 출력(월단위)
    2. 결재건수별 출력
    """)
    UserAnswer = input()
    if UserAnswer == "1" :
        print("기간별 출력을 선택하셨습니다.")
        im.Func.PrintToDate(table)
    elif UserAnswer == "2" :
        print("결개건수별 출력을 선택하셨습니다.")
    else : continue
