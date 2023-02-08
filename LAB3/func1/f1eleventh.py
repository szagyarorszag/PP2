def is_it_palindrome(word):
    true = True
    for index , item in enumerate(word):
        if word[index] == word[len(word) - 1 - index]:
            pass
        else:
            return False
    return True 
print(is_it_palindrome('madam'))