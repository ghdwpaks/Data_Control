



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



str = "[사과]루비에스(사과)"
print("[사과]후지(부사) :",get_real_length_on_CMD("[사과]후지(부사)"))
print("[사과]사과 :",get_real_length_on_CMD("[사과]사과"))
print("[사과]미야비(사과) :",get_real_length_on_CMD("[사과]미야비(사과)"))
print("[사과]아리수(사과) :",get_real_length_on_CMD("[사과]아리수(사과)"))
print("[사과]아오리 :",get_real_length_on_CMD("[사과]아오리"))
print("[사과]아오리(쓰가루동북 :",get_real_length_on_CMD("[사과]아오리(쓰가루동북s"))
print("[사과]미야비(사과)\t1")
print("[사과]아오리\t1")

print(get_real_length_on_CMD(str))
print(str)
print("12345678901234567890")
print("\t1")
print("\t\t2")
print("\t\t\t3")