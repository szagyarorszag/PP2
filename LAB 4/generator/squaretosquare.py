f = int(input("Please input the first number : "))
s = int(input("Please input the second number : "))
list_of_squares = ( x**2 for x in range(f ,s+1)) 
print(list(list_of_squares))