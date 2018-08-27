#ASSIGNMENT9

#Q1
a=3
if a<4:
    try:
        a=a/(a-3)
    except:
        print('Division cannot be done by zero')
print(a)

#Q2
l=[1,2,3]
try:
    print(l[3])
except:
    print('List index out of range.')

#Q3
print("An exception")

#Q4
print("OUTPUT\n"
"""-5.0
a/b result is 0""")

#Q5

#1
try:
   import maths
except ImportError:
    print("It is import error because no such module is present")
    
#2
try:
    a=int(input("ENTER NO."))
except ValueError:
    print("ENTER NO.ONLY")

#3
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Invalid index")
