
import csv

class SetClass :
    
    def GetTable(filepath) :
            #table.csv
            table = []
            with open(filepath,'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    table.append(row)
                    #print(row)
            return table

    def ApplyPriNum(Table) :
        for i in range(len(Table)) :
            Table[i].update({"고유번호":i+1})
        return Table

