f = open("Unstructured_data.txt", 'r')
data = f.read()
print(data)

data = data.replace('\t',' ')
data = data.replace('\n',' ')
data = data.split(" ")
print(data)

weapon_data = []
for i in range(len(data)) :
    if '(' in data[i] :
        print(data[i])

f.close()