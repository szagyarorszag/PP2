import re
data = "snake_case_something"
indexUnderscore = [index for index, item in enumerate(data) if item == "_"]
data = re.sub("_", "", data)
camelData = ""

i = 0
for index, item in enumerate(data):
    if indexUnderscore and i < len(indexUnderscore) and index == indexUnderscore[i] - i:
        camelData += item.upper()
        i = i + 1
    else:
        camelData += item
        
print(camelData)
