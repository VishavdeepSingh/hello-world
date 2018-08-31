#Q1

import datetime 

date=datetime.datetime.now()

print(date.day)


#Q2

import webbrowser as web

web.open("https://www.google.com")


#Q3

import os

os.chdir("F:\changedirectory")#Used to change working directory

a =  os.getcwd()#Returns current working directory

files = os.listdir(a)#Returns list of files in the current directory

i=1

print(files)

for filename in files:

    os.rename(filename,str(i)+'.jpg')

    i=i+1
