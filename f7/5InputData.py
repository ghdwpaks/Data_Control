
string = "ghdwpaks"
print(string[:4])
date1 = "201905"
print(date1[:4])
print(date1[4:])

def func() :
    return [1,2]
s , e = func()
print(s,e)
print('eval("1-2") :',eval("1-2"))
print("eval('2') :",eval("2"))
print(type(eval("2")))

while True :
    StartPoint = input("출력을 원하는 시작기간(ex.201905)을 입력해주세요.(미입력시 2019년 5월부터)\n")
    if StartPoint == "" :
        EndPoint="201905"
        break
    elif (int(StartPoint[:4]) <= 2020 and int(StartPoint[:4]) >= 2019) and (int(StartPoint[4:]) <= 12 and int(StartPoint[4:]) >= 00) :
        break
    else :
        print("다시 입력해주세요")
        continue
        
while True :
    EndPoint = input("출력을 원하는 종단기간(ex.202007) 입력해주세요.(미입력시 2020sus 07월까지)\n")
    if EndPoint == "" :
        EndPoint="202007"
        break
    elif (int(EndPoint[:4]) <= 2020 and int(EndPoint[:4]) >= int(StartPoint[:4]) and int(EndPoint[4:]) <= 12 and int(EndPoint[4:]) >= 00)or(EndPoint[:4]>StartPoint[:4]):
        break
    else :
        print("다시 입력해주세요")
        continue


