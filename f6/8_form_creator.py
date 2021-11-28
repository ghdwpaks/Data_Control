import random as r
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

def return_isalph(w) :
    #w = "'41'"
    w = list(w)
    temp_res = []
    for i in range(len(w)) :
        if w[i].isdigit() :
            temp_res.append(w[i])
    print("temp_res :",temp_res)
    print("".join(temp_res))
    return int("".join(temp_res))
    
def creator() :
    lengh_ = 0
    while True :
        lengh_ = r.randint(0,10)
        if lengh_ % 2 == 0 :
            continue
        else :
            break

    data_type = ["+","-","*"]
    #data_type2 = ["damage","rpm","capacity"]
    data_type2 = [1,2,3]
    form_ = []
    for i in range(lengh_) :
        if i % 2 == 0 :
            form_.append(data_type2[r.randrange(0,len(data_type2))])
        else :
            form_.append(data_type[r.randrange(0,len(data_type))])
    return form_
name = get_table("weapon_names.csv")
print(name)
status = get_table("status2.csv")
print(status)
name_status = []
#print(len(name))
print(name[0]["name"])
for i in range(len(name)) :
    name_status.append([str(name[i]["name"]).lower(),return_isalph(str(status[i]["damage"])),return_isalph(str(status[i]["rpm"])),return_isalph(status[i]["capacity"])])
print(name_status)
for i in name_status : print(i)

result = []
form_ = creator()
print(form_)
for i in range(len(name_status)) :
    temp_res = name_status[i][form_[0]]
    for j in range(1,len(form_),2) :
        temp_res = eval(str(temp_res)+str(form_[j])+str(name_status[i][form_[j+1]]))
    result.append(temp_res)
print(result)
print(len(result))
print(len(name_status))

for i in range(len(name_status)) :
    name_status[i].append(result[i])
#lst.sort(key=lambda x:x[0])
print("\n\n\n\n\n\n")
name_status.sort(key=lambda x:x[4] ,reverse=True)
for i in name_status : print(i)
print(len(name_status))
f = open("tier.txt", 'r')
tier = f.read()
f.close
tier = tier.split("\n")
for i in range(len(tier)) :
    tier[i] = tier[i].split(",")
tier.sort(key=lambda x:x[1] )
print("tier :",tier)
tier_weapons = []
for i in range(len(tier)) :
    for j in range(len(name_status)) :
        s1 = str(tier[i][0]).strip().lower()
        s2 = str(name_status[j][0]).strip().lower()
        
        s1 = s1.replace(" ","")
        s2 = s2.replace(" ","")
        if s1 ==s2 :
            #print("str(tier[i]['name']).strip().lower() :",str(tier[i]["name"]).strip().lower())
            #print("str(name_status[j][0]).strip().lower() :",str(name_status[j][0]).strip().lower())
            tier_weapons.append([name_status[j][0],name_status[j][4]])
print("\n\n\n\n\n\n")
tier_weapons.sort(key=lambda x:x[1] ,reverse=True)
print("len(tier_weapons) :",len(tier_weapons))
for i in range(len(tier_weapons)) :
    if i <= 12 :tier_weapons[i].append(1)
    elif i <= 19 :tier_weapons[i].append(2)
    elif i <= 25 :tier_weapons[i].append(3)
    elif i <= 30 :tier_weapons[i].append(4)
    elif i <= 35 :tier_weapons[i].append(5)
for i in tier_weapons : print(i)
right_tier_count = 0
for i in range(len(tier_weapons)) :
    si = str(tier_weapons[i][0]).strip().lower()
    for j in range(len(tier)) :
        #(tier_weapons[i][0] == tier[j][0]) and 
        #print(tier_weapons[i][0],tier[j][0],(tier_weapons[i][0] == tier[j][0]))
        #if (int(tier_weapons[i][2]) == int(tier[j][1])):
        
        if si == tier[j][0].strip().lower() and (int(tier_weapons[i][2]) == int(tier[j][1])) :
            #print("\n"*20,True,"\n"*20)
            right_tier_count += 1
print(right_tier_count)
    






