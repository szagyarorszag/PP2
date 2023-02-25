import re  
data = "SomeData"
x = re.sub("[A-Z]", " " , data)
print(x)