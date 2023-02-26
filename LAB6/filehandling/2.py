import os 
path = r"C:\Users\bakit\PPrep2.0\LAB6\filehandling\sakkijarvenPolkka.txt"
data = open(path) 
if os.path.exists(path):
    print("File and path exists let's check readability!")
    if data.readable():
        print("Wunderbar! we may read this file so let's chek the writability!")
        if os.access(path , os.W_OK):
            print("Perfekt! we may write something in this file so let's check the executability!")
            if os.access(path , os.X_OK):
                print("Gotterfrunken! this file is executable!")
                answer = input("Finally do you want to read this file ? (put Y|N) ") 
                if answer == "Y":
                    print(data.read()) 
            else:
                print("Mein Got! this file isn't executable") 
        else:
            print("Donner und Blitz! we can't write anything in this file! ")
    else:
        print("Sheisse! unfortunately we can't read thie file!")
else:
    print("File doesn't exist!")