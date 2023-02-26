import os
with open(r"C:\Users\bakit\PPrep2.0\LAB6\filehandling\sakkijarvenPolkka.txt" ,'r') as file:
    data = file.readlines()
print(f"There is {len(data)} lines")