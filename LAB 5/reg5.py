import re
data1 = "aferrg4gb"
data2 = "agggrttre"
data3 = "iueriuerb"
data4 = "wfegrjks"
x = re.search("^a.*?b$" , data1)
if x:
    print("Match found!")
else:
    print("Not found!")

