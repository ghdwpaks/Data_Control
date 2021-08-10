import csv



def get_table(filepath) :
        #table.csv
        table = []
        with open(filepath,'r') as f :
            reader = csv.DictReader(f)
            for row in reader :
                table.append(row)
                #print(row)
        return table

def setting_column(table) :
    for i in table :
        print(i)



table = []
table = get_table("table.csv")
setting_column(table)