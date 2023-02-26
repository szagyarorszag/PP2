def upperAndLower(string):
    upper = 0
    lower = 0
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            upper+=1
            print(i)
        else:
            lower+=1
    print(f"upper :{upper} lower : {lower}")
upperAndLower("GotterFrunken")