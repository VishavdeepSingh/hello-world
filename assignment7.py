#DICTIONARY

#Q1

dict={}
for i in range(1,4):
    k=(input('ENTER KEY'))
    v=(input('ENTER VALUE'))
    dict[k]=v
print(dict)

#Q2
dict_n={}
dict_m={}
for i in range(1,3):
    name=(input('ENTER NAME'))
    for j in range(1,3):
        subject=(input('ENTER SUBJECT'))
        marks=float(input('ENTER MARKS'))
        dict_m[subject]=marks
    dict_n[name]=dict_m
print(dict_n)
stu=input("ENTER STUDENT NAME TO GET HIS/HER MARKS")
print(dict_n[stu])
    
    
