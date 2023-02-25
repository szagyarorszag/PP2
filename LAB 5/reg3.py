import re
data1 = "some_data"
data2 = "somedata"
data3 = "SomeData"
x = re.search("[a-z]+_[a-z]+" , data2 )
if x :
    print('Match found!')
else :
    print('Not found!')