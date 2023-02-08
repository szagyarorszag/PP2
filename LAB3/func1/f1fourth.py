import math as m
def filter_prime(numbers):
    def prime(n):
        if n == 1 :
            return False
        if n == 2 :
            return True
        if n % 2 == 0 :
            return False
        i = 3
        while i < m.sqrt(n) + 1 :
            if n % i == 0 :
                return False
            i += 2
        return True

    return [num for num in numbers if prime(num)] 
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))
