def unique_list(lst):
    unic_list = []
    for element in lst:
        if element not in unic_list:
            unic_list.append(element)
    return unic_list 
list = [1,2,4,0,0,7,5]
print(unique_list(list))