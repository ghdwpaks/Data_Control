import csv
import os

class setting :

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
    def duplicate_deficiencying(table) :
        prints.print_list(table)
        kinds_lv1 = []
        for i in table :
            if i[0] not in kinds_lv1 :
                kinds_lv1.append(i[0])
        print("duplicate_deficiencying kinds_lv1 :",kinds_lv1)
        prints.print_list(kinds_lv1)

        kinds_lv2 = []
        for i in table :
            if i[1] not in kinds_lv2 :
                kinds_lv2.append(i[1])
        print("duplicate_deficiencying kinds_lv2 :",kinds_lv2)
        prints.print_list(kinds_lv2)

        kinds_lv3 = []
        for i in table :
            if i[2] not in kinds_lv3 :
                kinds_lv3.append(i[2])
        print("duplicate_deficiencying kinds_lv3 :",kinds_lv3)
        prints.print_list(kinds_lv3)
        
        kinds_res_cat_t = []
        for i in table :
            temp_list = [i[0],i[1],i[2]]
            if temp_list not in kinds_res_cat_t :
                kinds_res_cat_t.append(temp_list)
        kinds_res_cat = []
        for i in kinds_res_cat_t :
            kinds_res_cat.append([i,[]])
        print("table :")
        prints.print_list(table)
        print("kinds_res_cat :")
        prints.print_list(kinds_res_cat)
        #kinds_res_cat[0][1].append(1)
        #print(kinds_res_cat[0][1][0])
        #os.system('pause')
        res = []
        for i in kinds_lv1 :
            #print("i :",i)
            for j in kinds_lv2 :
                for k in kinds_lv3 :
                    for e in table :
                        #print("e :",e)
                        if e[0] == i and e[1] == j and e[2] == k :
                            t_title = [e[0],e[1],e[2]]
                            #print(t_title)
                            for n in kinds_res_cat :
                                #print("n[0] == t_title :",n[0] == t_title)
                                #print("n[0] :",n[0] )
                                #print("t_title :",t_title)
                                #os.system('pause')
                                if n[0] == t_title :
                                    #print("1n :",n)
                                    #print("2n[0] :",n[0])
                                    #print("3n[1] :",n[1])
                                    #print("4appending target e[3]:",e[3])
                                    n[1].append(e[3])
                                    #print("5n :",n)
                                    #print("6n[0] :",n[0])
                                    #print("7n[1] :",n[1])
        print("1kinds_res_cat; res :",kinds_res_cat)
        prints.print_list(kinds_res_cat)    
        for i in kinds_res_cat :
            temp_res = 0
            for j in i[1] :
                temp_res += int(j)
            temp_res = temp_res // len(i[1])
            i[1] = temp_res
        print("2kinds_res_cat; res :",kinds_res_cat)
        prints.print_list(kinds_res_cat)  
        print("이름\t\t\t무게\t등급\t\t평균가격")
        for i in kinds_res_cat :
            #print("{}\t\t{}\t{}\t\t{}".format(i[0][0],i[0][1],i[0][2],i[1]))
            #get_real_length_on_CMD
            pass
            print(i[0][0],end="")
            if prints.get_real_length_on_CMD(i[0][0]) < 8 :
                print("\t\t\t",end="")
            elif prints.get_real_length_on_CMD(i[0][0]) < 16 :
                print("\t\t",end="")
            elif prints.get_real_length_on_CMD(i[0][0]) < 24 :
                print(" ",end="")
                
            print(i[0][1],end="\t")
            print(i[0][2],end="")
            if prints.get_real_length_on_CMD(i[0][2]) < 8 :
                print("\t\t",end="")
            elif prints.get_real_length_on_CMD(i[0][2]) < 16 :
                print("\t",end="")
            print(i[1])
            
                

        print("이름\t\t\t무게\t등급\t\t평군가격")
                
                                    


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
            #print("select lv2 category i:",i)
            if cat_name in i[0] :
                if i not in res :

                    print("select lv2 category appending culomn :",i)
                    res.append(i)

        #prints.print_list("select lv2 category res :",res)
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
                if string[i] == "]" or string[i] == "[" or string[i] == ")" or string[i] == "(" or string[i] == " " or string[i].encode().isalpha():
                    #영어 맞음
                    count += 1
                else :
                    count += 2 
        #print("GRLOC :",count)
        return count

    
class sectors :
    def sector1() :
        while True :
            table = []
            table = setting.get_table("table.csv")
            #print("len(table) bf :",len(table))

            table = setting.setting_column(table)
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
            prints.print_list(small_cat)

            setting.duplicate_deficiencying(small_cat)
            
            print("\n\n")
            print("sector 1 의 역할이 전부 끝났습니다.\n계속 하시려면 엔터, 그만두시려면 'ㄴ' 또는 's'를 눌러주세요")
            choose_exit = input("입력 : ")
            choose_exit.lower()
            if choose_exit == 'ㄴ' or choose_exit == "s" :
                break
            else :
                continue
            print("\n\n")
                

        
    


# get_table -> setting
# get_table -> setting -> select_lv1_category


while True :
    print("\n\n\n")
    print("농수산물 정보 출력 시스템에 진입했습니다.")
    print("원하는 기능을 '숫자로만' 선택해주세요.")
    print("1.품목명별 정보 출력")
    select1_subject = input("입력 : ")
    if select1_subject == '1' :
        sectors.sector1()
