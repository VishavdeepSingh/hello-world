## FILE HANDLING
#Q1
a = open('old.txt','r')
l = a.readlines()
for i in l:
    print(i)
a.close()

#Q2
from collections import Counter
with open('old.txt','r') as a:
    b = Counter(a.read().split())
    print(b)

#Q3
with open('old.txt','r') as c:
    with open('new.txt','w') as d:
        for i in c:
            d.write(i)

#Q4
with open('old.txt') as f:
    with open('new.txt') as e:
        for i1,i2 in zip(f,e):
            print(i1+i2)

#Q5
a = open("file1.txt")
b = []
for i in a:
    b.append(int(i))
b.sort()
print(b)
a.close()
