def has_33(list , n ):
    for index , item in enumerate(list):
        if index + 1 != len(list):
            if list[index] == list[index+1] and list[index] == int(n):
                return "True"
    return "False" 
list1 = input("Input the list: ")
list = list(map(int , list1.split(" ")))
print(list)
n = input("Input a number: ")
print(has_33(list,n)) 