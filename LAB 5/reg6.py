import re
data = "wwewfw erfrw,rf43"
x = re.sub("[\s,.]" , ":" , data)
# x = re.sub("," , ":" , data)
# x = re.sub("." , ":" , data)
print(x)