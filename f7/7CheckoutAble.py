l = [[1,64],[2,256],[3,142]]

l.sort(reverse=True,key=lambda x : (x[0], x[1]))
for i in l :
    print(i)

