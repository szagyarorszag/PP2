import time
def afterTime(miliseconds , number):
    time.sleep(miliseconds/1000)
    print(f"Square root of {number} after {miliseconds} miliseconds is {number**0.5}")
afterTime(1488,1488)