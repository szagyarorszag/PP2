import os
with open("test.txt" , "w") as file:
    file.write("I still exist!")
__path = r"C:\Users\bakit\PPrep2.0\test.txt"
data = open("test.txt")
if os.path.exists(__path):
    print("File and path exists let's check readability!")
    if data.readable():
        print("Wunderbar! we may read this file so let's chek the writability!")
        if os.access(__path , os.W_OK):
            print("Perfekt! we may write something in this file so let's check the executability!")
            if os.access(__path , os.X_OK):
                print("Gotterfrunken! this file is executable!")
                answer = input("Finally do you want to read this file ? (put Y|N) ") 
                if answer == "Y":
                    print(data.read())  
                    #os.remove(__path) 
                    print("File deleted!")
                    try:
                        os.remove(__path) 
                        print(os.path.exists(__path))
                    except PermissionError as e: 
                        print("You can't get access because this path is no longer exist!" )

            else:
                print("Mein Got! this file isn't executable") 
        else:
            print("Donner und Blitz! we can't write anything in this file! ")
    else:
        print("Sheisse! unfortunately we can't read thie file!")
else:
    print("File doesn't exist!")