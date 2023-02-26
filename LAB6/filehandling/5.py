import os 
list = ["There" , "was" , "Sakkijarven" , "Polkka"]
with open(r"C:\Users\bakit\PPrep2.0\LAB6\filehandling\sakkijarvenPolkka.txt" , "w+") as myFile:
    for word in list:
        myFile.write(word + "\n")