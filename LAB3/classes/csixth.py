import math as m
def isPrime(x):
    if x == 1 :
        return False
    if x == 2 :
        return True
    if x % 2 == 0 :
        return False

    i = 3
    while i < m.sqrt(x) + 1 :
        if x % i == 0 :
            return False
        i += 2
    return True
example_list = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

prime_list = list(filter(lambda a : isPrime(a) , example_list))

print(prime_list)