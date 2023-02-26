def multiplylist(*a):
    number = 1
    for i in a:
        number*=i
    return number 
print(multiplylist(1,2,3,5,6))