import os 
EngAlphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
ListOfAlphabet = list(map(str , EngAlphabet.split(" "))) 
for char in ListOfAlphabet:    
    with open( char +".txt", "w") as file:
        file.write("Glory to Ukraine")