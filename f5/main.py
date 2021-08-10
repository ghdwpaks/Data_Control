import csv
from os import truncate

class setting_fir :

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
        res = []
        for i in table :
            temp_li = [i["품목명"],i["단위"],i["등급"],i["가격"]]
            #print("setting_column tmp_li :",temp_li)
            if not i in res :
                #print(i)
                res.append(temp_li)
        return res

class selects :
    def select_lv1_category(table) :
        res = []
        for i in table :
            temp_li = str(i[0]).split("]")
            temp_li = list(temp_li)
            del temp_li[0]
            temp_li = "".join(temp_li)
            if temp_li not in res :
                res.append(temp_li)
        prints.print_list(res)
        return res
    
    def select_lv2_category(table,cat_name) :
        res = []
        for i in table :
            if cat_name in i["품목명"] :
                res.append(i)

        prints.print_list("select lv2 category res :",res)
        return res
    
    
    




class prints :
    def print_list(table) :
        for i in table :
            print(i)
    
    def print_div_6(table) :
        for i in range(len(table)) :
            if i % 6 == 0 and i != 0:
                print()
            print(table[i],end="\t")
            if prints.get_real_length_on_CMD(table[i]) < 8 :
                print("\t\t",end="")
            elif prints.get_real_length_on_CMD(table[i]) < 16 :
                print("\t",end="")

    def get_real_length_on_CMD(string) :
        count = 0
        for i in range(len(string)) :
            if string[i].encode().isdigit() :
                count += 1
            else :
                if string[i] == "]" or string[i] == "[" or string[i] == ")" or string[i] == "(" or string[i].encode().isalpha():
                    #영어 맞음
                    count += 1
                else :
                    count += 2 
        #print("GRLOC :",count)
        return count

    
class sectors :
    def sector1() :
        table = []
        table = setting_fir.get_table("table.csv")
        #print("len(table) bf :",len(table))

        table = setting_fir.setting_column(table)
        #print("len(table) af :",len(table))
        #prints.print_list(table)

        big_cat = selects.select_lv1_category(table)

        prints.print_div_6(big_cat)
        user_big_cat = ""
        while True :
            print("종류를 정확히 골라주세요")
            user_big_cat = input("입력 :")
            if user_big_cat in big_cat :
                print("주제가 정확히 들어맞음을 확인했습니다.")
                break
            else :
                print("주제가 포함되지 않음을 확인했습니다.")
                continue
        
        small_cat = selects.select_lv2_category(table,user_big_cat)
                

        
    


# get_table -> setting_column
# get_table -> setting_column -> select_lv1_category


while True :
    print("\n\n\n")
    print("농수산물 정보 출력 시스템에 진입했습니다.")
    print("원하는 기능을 '숫자로만' 선택해주세요.")
    print("1.품목명별 정보 출력")
    select1_subject = input("입력 : ")
    if select1_subject == '1' :
        sectors.sector1()
