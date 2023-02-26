import os
with open(r"C:\Users\bakit\PPrep2.0\LAB6\filehandling\sakkijarvenPolkka.txt" , 'r') as file:
    data = file.read() 
with open(r"abotherFileForCopy.txt" , 'w') as f:
    f.write(data)