import os 
superDirectory = 'D:\For myself\Edu\python codes'
print(*[directory for directory in os.listdir(superDirectory)] , sep = "\n")
