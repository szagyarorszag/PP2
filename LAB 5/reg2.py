import re
data1 = "abb"
data2 = "abbb"
data3 = "ab"
x = re.search("^a(b{2,3})$" , data3 )
if x :
    print("Match found!")
else : 
    print("Not found!")