#LIST
#Q1.
li=['samsung','htc','sony','nokia']
print(li)
#Q2
add=['google','apple','facebook','microsoft','tesla']
print(li+add)
#Q3
numb=[1,2,3,1,2,3,1,4,3,2,8,6,5,9]
print(numb.count(1))
#Q4
d=[1,2,3,1,2,3,1,4,3,2,8,6,5,9]
(d.sort())
print(d)
#Q5
A=[1,2,3,4,5]
B=[6,7,8,9]
C=(A+B)
(C.sort())
print(C)
#Q6
numb=[1,2,3,1,2,3,1,4,3,2,8,6,5,9]
even=0
odd=0
for i in numb:
    if i % 2:
        even=even+1
    else:
        odd=odd+1
#odd nos:
print(odd)
#even nos:
print(even)
#TUPLES
#Q1
a=[1,2,3,1,2,3,1,4,3,2,8,6,5,9]
b=(reversed(a))
print(tuple(b))
#Q2
num=[1,2,3,1,2,3,1,4,3,2,8,6,5,9]
#MAX NO:
print(max(num))
#MIN NO:
print(min(num))
#STRINGS
#Q1
name='vishavdeep singh'
print(name.upper())
#Q2
name='vishavsandhu7700@gmail.com'
if name.isnumeric():
    print('TRUE')
else:
    print('FALSE')
#Q3
a='HELLO WORLD'
print(a.replace('WORLD','VISHAVDEEP SINGH SANDHU'))
