def main_reverse_sentence():    
    line = input()
    new_string_list = list(map(str , line.split(" ")))
    print(*new_string_list[::-1])
main_reverse_sentence()
