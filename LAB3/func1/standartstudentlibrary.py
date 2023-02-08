def sqrt( n ):
    return n**0.5
def faren_to_celcium(far):
    return (5/9)*(far-32)     
def is_it_palindrome(word):
    true = True
    for index , item in enumerate(word):
        if word[index] == word[len(word) - 1 - index]:
            pass
        else:
            return False
    return True
def histogram(list):
    for i in list:
        print("*"*i)
def volume_of_sphere(radius):
    return (4/3)*3.14*(radius**3)