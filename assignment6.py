#Q1
import math

def sphere(r):
    '''THE AREA OF THE SPHERE IS'''
    area = 4 * r * r * math.pi
    print('Surface Area Is = %.2f' %area)
r=float(input('enter the radius='))
sphere(r)

#Q2
def perfect(n):
    count=0
    for i in range(1,n):
        if(n%i==0):
            count=count+i
    if(count==n):
        print(n)
a=1000
for j in range(1,a):        
    perfect(j)

#Q3
def table(n):
    '''THE TABLE IS'''
    for i in range(1,11):
        m=n*i
        print(n,'x',i,'=',m)
n=int(input('enter the value'))
table(n)

#Q4
def power_of_no(b,x):
    if(x==1):
        return(b)
    if(x!=1):
        return(b*power_of_no(b,x-1))
b=int(input('ENTER BASE:'))
x=int(input('ENTER EXP:'))
print('RESULT:',power_of_no(b,x))
    

    
