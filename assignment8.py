#Q1

class circle:

    def __init__(self,r):

        self.radius=r

    def getArea(self):

        return(3.14*(self.radius**2))

    def getcircumference(self):

        return(2*3.14*self.radius)

r=int(input('RADIUS'))

a=circle(r)

print('AREA IS ',a.getArea())

print('CIRCUMFERENCE IS ',a.getcircumference())


#Q2

class student:

    def __init__(self):

        self.name=input("Enter Name")

        self.rollno=int(input("Enter Rollno"))

    def display(self):

        print("Student Info")

        print('NAME:',self.name,'ROLL NO:',self.rollno,'AGE:',self.age,'MARKS:',self.marks)

    def setAge(self):

        self.age=int(input("Enter Age"))

    def setmarks(self):

        self.marks=int(input("Enter Marks"))

a=student()

a.setAge()

a.setmarks()

a.display()


#Q3


class temp():
    
    def fah(self):
        
        self.c=int(input("ENTER TEMP IN CELCIUS"))
        
        return((9/5)*self.c+32)
    
    def cel(self):
        
        self.f=int(input("ENTER TEMP IN FAHRENHIET"))
        
        return(((self.f-32)*5)/9)

a=temp()

print(a.fah())

print(a.cel())


#Q4


class MovieDetails():

      def __init__(self):

        self.artist_name=input("Artist Name:- ")

        self.year=int(input("Year Of release:- "))

        self.rating=int(input("Rating:-"))

      def Add(self):
          
        self.moviename=input("Enter Movie Name:- ")

      def Display(self):

        print("Movie Details:")

        print("Movie name:-",self.moviename,"\nArtist Name:-",self.artist_name,"\nYear Of Release:-",self.year,"\nRating:-",self.rating)

  
x=MovieDetails()

x.Add()

x.Display()


#Q5


class animal:

    def info_(self):

        print("Class Animal")

class animal_attribute():

    def attribute(self):

        print("Class Animal_Attributes")

class tiger(animal,animal_attribute):

    def tiger_(self):

        print(" Class Tiger")

x=animal()

y=animal_attribute()

z=tiger()

z.info_()

z.attribute()



#Q6

"""OUTPUT:    A B

A B"""


#Q7

class shape:

    def __init__(self,l,b):

        self.length=l

        self.breath=b

    def area(self):

        return(self.length*self.breath)
    
class rectangle(shape):
      pass

class square(shape):
      pass
    
l=int(input("ENTER LENGTH"))

b=int(input("ENTER BREATH"))

a=rectangle(l,b)

b=square(l,b)

print("AREA OF RECT",a.area())
print("AREA OF SQUARE",b.area())
