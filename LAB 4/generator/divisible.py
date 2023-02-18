n =  int(input())
list_3_4 = ( x for x in range ( 1 , n ) if x % 3 == 0 or x % 4 == 0 )
print(list(list_3_4))