example_list = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

prime_list = list(filter(lambda x: all(x%i != 0 for i in range(2 , int(x)**0.5+1)) and x!= 1 ,example_list))

print(prime_list)