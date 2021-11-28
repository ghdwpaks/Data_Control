
f = open("results.txt", 'r')
tier = f.read()
print(tier.count("\t"))
f.close