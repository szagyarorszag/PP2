import re

data1 = "Something"
data2 = "notSomething"
data3 = "something"
x = re.match("[A-Z]{1}[a-z]" , data1 )
if x :
    print("Match found!")
else:
    print("Not found!")
