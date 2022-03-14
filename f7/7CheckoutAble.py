
import Importer as im
import os
l = [[1,64],[2,256],[3,142]]
x = ["123","456","789"]
y = ["ghd","wpaks"]
x.extend(y)
print("123465 :",x)
l.sort(reverse=True,key=lambda x : (x[0], x[1]))
#for i in l :print(i)

KindOf = im.KeyList.ReturnList()
#for i in KindOf : print(i)
#print("type(KindOf) :",type(KindOf))
#print("tpye(KindOf[0]) :",type(KindOf[0]))
os.system("pause")
SubNum = im.KeyList.SelectKindOfSubject(5)
res = im.KeyList.SelectKindOf(SubNum)
#print("123465 :",[].extend([1,2]))
