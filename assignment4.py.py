#Q1.
li=['1','2','3','4','5']
print(li[::-1])

#Q2
a='viShavDeeP SingH sanDHu'
for ch in a:
    if(ch >= 'A' and ch <= 'Z'):
        print(ch, end=" ")

#Q3
a=['1','2','3','4','5']
b=[]
for i in a:
    b.append(int(i))
a=b
print(b)

#Q4
a='vahav'
b=(a[::-1])
if a==b:
    print('THE STRING IS PALLINDROMIC')
else:
    print('THE STRING IS NOT PALLINDROMIC')

#Q5
import copy
x=[1,2, [3,4,5],6]
y=copy.deepcopy(x)
y[2][1]=7
print(x)
print(y)

'''SHALLOW COPY: A Shallow copy does not creates a copy of nested objects, instead it just copies the reference of nested loop.
   DEEP COPY: A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements'''
