from Set import SetClass
import csv

table = SetClass.get_table("table.csv")
for i in table :
    print(i)
print("type(table) :",type(table))
print("type(table[0]) :",type(table[0]))
LocationList = []
for i in table :
    LocationList.append(i)

