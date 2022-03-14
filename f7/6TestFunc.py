
import Importer as im
from KeyList import KeyList 

Table = im.SetClass.GetTable("table.csv")

StartPoint, EndPoint = im.Func.InputDate()
Table = im.SetClass.ApplyPeriod(Table,StartPoint,EndPoint)

#print(KeyList.ReturnList())
subject = KeyList.SelectSortSubject()
im.SetClass.ApplySort(Table,subject)



