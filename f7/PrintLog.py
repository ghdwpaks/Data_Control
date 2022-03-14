


class PrintLog :
    def Write(cont , filepath="resulttemp.txt") :
        f = open(filepath,'w',encoding="UTF-8")
        if type(cont) == type("") or type(cont) == type(0) :
            f.write(cont)
        elif type(cont) == type([]):
            for i in cont :
                f.write(str(i)+str("\n"))
        f.close()

    
    def print_div_6(table) :
        for i in range(len(table)) :
            if i % 6 == 0 and i != 0:
                print()
            print(table[i],end="\t")
            if PrintLog.get_real_length_on_CMD(table[i]) < 8 :
                print("\t\t",end="")
            elif PrintLog.get_real_length_on_CMD(table[i]) < 16 :
                print("\t",end="")

    
    def get_real_length_on_CMD(string) :
        count = 0
        for i in range(len(string)) :
            if string[i].encode().isdigit() :
                count += 1
            else :
                if string[i] == "]" or string[i] == "[" or string[i] == ")" or string[i] == "(" or string[i] == " " or string[i] == "." or string[i] == "," or string[i].encode().isalpha():
                    #영어가 맞으면
                    count += 1
                else :
                    count += 2 
        #print("GRLOC :",count)
        return count