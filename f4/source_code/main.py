import functions as f



def sector_sub1(table) :

    sub_name = f.gets.get_big_subject_name(table,1,']')
    f.prints.print_strings_dived(sub_name)
    print()
    ans1_big_subs = input("주제 입력 :")
    ans1_big_subs = f.setting.sealing_input_sub(ans1_big_subs)
    subs_ops = f.gets.select_ops_by_keyword(table,ans1_big_subs,1)
    #f.prints.print_table_at_str(subs_ops,'}')
    sub_small_name = f.gets.get_subjects_name(subs_ops,1)

    ans2 = ""
    while True :
        print(ans1_big_subs,"에 적합한 품목은 다음과 같습니다.")
        f.prints.print_strings_dived(sub_small_name)
        print()
        ans2 = input("주제 입력 : ")
        if ans2 in sub_small_name :
            break
        else :
            print("주제를 정확히 입력해주세요.")
    res_ops = f.gets.select_ops_by_keyword(subs_ops,ans2,1)
    
    f.prints.print_table_at_str(res_ops,"}")
    sorted_res_ops = []
    sec2_type = []
    for i in range(len(res_ops)) :
        if res_ops[i]['2'] not in sec2_type :
            sec2_type.append(res_ops[i]['2'])
    sec2_type.sort()

    sec3_type = []
    for i in range(len(res_ops)) :
        if res_ops[i]['3'] not in sec3_type :
            sec3_type.append(res_ops[i]['3'])
    sec3_type.sort()

    temp_res_ops2 = []
    for i in range(len(sec2_type)) :
        sec2_temp = []
        for j in range(len(res_ops)) :
            if sec2_type[i] == res_ops[j]['2'] :
                sec2_temp.append(res_ops[j])
        temp_res_ops2.append(sec2_temp)
    '''
    print("\n\n\n\ntemp_res_ops2")
    f.prints.print_table_at_str(temp_res_ops2,"}")
    print("\ntemp_res_ops2\n\n\n")
    print("len(sec3_type) :",len(sec3_type))
    '''
    temp_res_ops3 = []
    for i in range(len(sec3_type)) :
        sec3_temp = []
        for j in range(len(temp_res_ops2)) :
            for k in range(len(temp_res_ops2[j])) :
                if sec3_type[i] == temp_res_ops2[j][k]['3'] :
                    sec3_temp.append(temp_res_ops2[j][k])
        temp_res_ops3.append(sec3_temp)
    '''
    print("\n\n\n\ntemp_res_ops3")
    f.prints.print_table_at_str(temp_res_ops3,"}")
    print("\ntemp_res_ops3\n\n\n")
    '''
    for i in range(len(temp_res_ops3)) :
        for j in range(len(temp_res_ops3[i])) :
            sorted_res_ops.append(temp_res_ops3[i][j])
    '''
    print("\n\n\n\nsorted_res_ops")
    f.prints.print_table_at_str(sorted_res_ops,"}")
    print("\nsorted_res_ops\n\n\n\n")          
    '''
    temp_sub = [sorted_res_ops[0]['1'],sorted_res_ops[0]['2'],sorted_res_ops[0]['3']]
    print()
    print(temp_sub)
    res = []
    cost = 0
    addcost_count = 0
    for i in range(len(sorted_res_ops)) :
        canpass = True
        for j in range(len(temp_sub)) :
            if sorted_res_ops[i][str(j+1)] == temp_sub[j] :
                cost += int(sorted_res_ops[i]['4'])
                addcost_count += 1
            else :
                canpass = False
        if canpass and i != len(sorted_res_ops)-1 :
            cost += int(sorted_res_ops[i]['4'])
        else :
            res.append([temp_sub[0],temp_sub[1],temp_sub[2],cost//addcost_count])
            temp_sub = [sorted_res_ops[i]['1'],sorted_res_ops[i]['2'],sorted_res_ops[i]['3']]
            cost = 0
            addcost_count = 0
    print(res)
    f.prints.print_table_at_str(res,']')
        
    
    
    
            



 



#1등급을 고른다면, 각 항목에 관한 것들 출력 해주기
table = f.gets.get_table("table.csv")

while True :
    print("농수산물 정보 출력 시스템에 진입했습니다.")
    print("원하는 기능을 '숫자로만' 선택해주세요.")
    print("1.품목명별 정보 출력")
    print("2.단위별 정보 출력")
    print("3.등급별 정보 출력")
    print("4.가격별 정보 출력")
    print("5.산지별 정보 출력")
    print("6.친환경 구분별 정보 출력")
    select1_subject = input("입력 : ")
    if select1_subject == '1' :
        sector_sub1(table)
