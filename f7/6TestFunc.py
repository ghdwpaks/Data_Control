
import Importer as im

Table = im.SetClass.GetTable("table.csv")

StartPoint, EndPoint = im.Func.InputDate()
im.SetClass.ApplySort(Table,"결재금액",StartPoint,EndPoint)


