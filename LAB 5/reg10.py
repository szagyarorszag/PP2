import re   
camelCase = "snakeCaseSomething"
snake_case = re.findall("[A-Z][a-z]*" , camelCase)
print("{}{}".format(re.sub("[A-Z][a-z]*","" ,camelCase) ,"".join("_"+word.lower()  for word in snake_case)))