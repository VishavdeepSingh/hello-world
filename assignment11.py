#Q1

import re

a=input("Enter an E-mail")

b=re.findall('^[0-9A-Za-z][\w_]*[@](gmail.com|yahoo.com)',a)

if b:

    print("Valid email")

else:

    print("Invalid email")





#Q2

import re

c=input("Enter a mobile number with country code")

d=re.findall('^[+]91[6-9][0-9]{9}',c)

if d:

    print("Indian Number")

else:

    print("Number Is Not Indian")


