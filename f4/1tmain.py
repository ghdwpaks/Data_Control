from distutils.log import error
import threading
import copy as c
import csv
from queue import Queue
from random import randrange
import time

secs = time.time()
ttable=[]
with open("table.csv",'r') as f :
    reader = csv.DictReader(f)
    for row in reader : ttable.append(row)
'''
f = open("result.txt", 'w')
for i in range(len(ttable)):
    f.write(str(ttable[i])+"\n")
f.close()
'''
j = 0 
for i in range(len(ttable)):
    try :
        print(j)
        del ttable[i]
        j+=1
        ttable.append(ttable[i])
    except :
        break
print(j)

print(time.time()-secs)
#129.7314329147339
#