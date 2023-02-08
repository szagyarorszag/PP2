def spy_game(list):
    f = False
    s = False
    t = False 
    for index ,  item in enumerate(list):
        if f == True and s == True and item == 7:
            t = True
        elif f == True and item == 0:
            s = True
        elif  item == 0:
            f = True    
    if f == s and s == t and t == True:
        print("True")
    else:
        print("False")
     
list1 = [1,2,4,0,0,7,5]
list2 = [1,0,2,4,0,5,7]
list3 = [1,7,2,0,4,5,0]

spy_game(list2 )
