from ast import Import
from Set import SetClass

class KeyList :
    def ReturnList() :
        Table = SetClass.GetTable("table.csv")
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