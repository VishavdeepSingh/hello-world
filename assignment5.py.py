
#Q1

year=int(input("Enter year"))

if(year%4==0):

    if(year%100==0):

        if(year%400==0):

            print("IT IS LEAP YEAR")

        else:

            print("IT IS NOT LEAP YEAR")

    else:

        print("IT IS LEAP YEAR!!!")

else:

    print("IT IS NOT LEAP YEAR")


#Q2

length=int(input("Length"))

breadth=int(input("Breadth"))

if(length==breadth):

    print("IT IS SQUARE")

else:

    print("IT IS RECTANGLE")


#Q3

a=int(input("1 age"))

b=int(input("2 age"))

c=int(input("3 age"))

if(a>=b and a>=c):

    print("First is oldest")

elif(b>=c and b>=a):

    print("Second is oldest")

else:

    print("Third is oldest")



if(a<=b and b<=c):

    print("First is youngest")

elif(b<=c and b<=a):

    print("Second is youngest")

else:

    print("Third is youngest")


#Q4

a=int(input("Age"))

s=input("Sex")

m=input("Marital status")

if(s=='F'):

    print("Work in Urban Areas")

else:
    if(a>=20 and a<=40 and s=='M'):

        print("Can work anywhere")

    elif(a>=40 and a<=60 and s=='M'):

        print("Work in urban areas")

    else:

        print("Error")





#Question 5


q=int(input("Quantity"))

cost=100*q

if(cost>1000):

    cost=cost-(cost*0.1)

    print("Cost after discount =",cost)

else:

    print("Cost is =",cost)


#LOOPS


#Q1


a=[]

for i in range(10):

    b=int(input("Enter Number"))

    a.append(b)

print(a)


#Q2


while True:

    print("THANKS")
   

#Q3

    
a=[]

b=[]

n=3

for i in range(n):

    c=int(input("Enter Number"))

    a.append(c)

for j in a:

    v=j*j

    b.append(v)

print(b)



#Q4


l1=[]

l2=[]

l3=[]

l4=[]

a=4

for i in range(a):

    b=input("Enter Elements")

    l1.append(b)

for i in l1:

    if(i.isdigit()):

        l2.append(i)

    elif(i.isalpha()):

        l3.append(i)

    else:

        l4.append(i)

print(l2)

print(l3)

print(l4)



#Q5


list=[]

for i in range(1,101):

    if(i>1):

        count=False

        for j in range(2,i):

            if(i%j==0):

                count=True

        if not count:

            list.append(i)

print(list)



#Q6


for i in range(5):

    for j in range(i):

        print("*",end='')

    print()


#Q7


li1=[]

n=4

for i in range(n):

    a=int(input("Enter Element"))

    li1.append(a)

b=int(input("Enter the number u want to delete"))

x=li1.count(b)

for i in range(x):

    y=li1.index(b)

    del(li1[y])

print(li1)
