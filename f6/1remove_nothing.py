
def change_1char(l,c,c2) :
    print("l :",l)
    print("c :",c)
    print("c2 :",c2)
    while c in l :  
        loc = l.index(c)
        print("loc :",loc)
        l.remove(c)
        l.insert(loc,c2)
    l = "".join(l)
    return l

def change_1char(l,c,c2) :
    while c in l :  
        loc = l.index(c)
        l.remove(c)
        l.insert(loc,c2)
    return l

l = list("ghdwpaks")

print(l.index("g"))
l = change_1char(l,"w","ghd")
print("l2 :",l)


while 'w' in l:
    l.remove(' ')
print(l)

'''
Traceback (most recent call last):
  File "C:\workspace\Data_Control\f6\1remove_nothing.py", line 5, in <module>
    l.remove(' ')
ValueError: list.remove(x): x not in list
'''
