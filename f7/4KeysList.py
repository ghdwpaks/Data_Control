from ast import Import
from Set import SetClass

Table = SetClass.get_table("table.csv")
KindOf = [[],[],[],[],[],[]]
'''
0 : 장소 시군구명+.+읍면동명
1 : 성별
2 : 연령대
3 : 업종명
4 : 결재건수
5 : 결재금액
'''

for i in Table :
    KindOf[0].append(str(i["시군구명"])+"."+str(i["읍면동명"]))
    KindOf[1].append(i["성별"])
    KindOf[2].append(i["연령대"])
    KindOf[3].append(i["업종명"])
    KindOf[4].append(i["결제건수"])
    KindOf[5].append(i["결제금액"])

for i in range(len(KindOf)) :

    TempList = KindOf[i]
    TempList = set(TempList)
    TempList = list(TempList)
    TempList.sort
    KindOf[i] = TempList
for i in range(len(KindOf)) :
    if not (i == 4 or i == 5):
        print(KindOf[i])