from itertools import permutations
def permut_of_string(str_):
    permut = permutations(str_)
    for i in list(permut):
        print(*i)

user_string = input()

permut_of_string(user_string)
