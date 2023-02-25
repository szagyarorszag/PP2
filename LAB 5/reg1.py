import re
data = "abb"
x = re.search('^a(b*)$' , data)
if x:
    print("Match found!")
else:
    print("Not found!")