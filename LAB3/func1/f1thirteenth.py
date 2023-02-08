name = input("Hello! What is your name? ") 
def guess_it( name ):
    number = 0
    print("Well," + name + ", I am thinking of a number between 1 and 20.")
    def still_guess_it( name , number ):
        n = int(input("Take a guess.")) 
        if n < 12:
            print("Your guess is too low.")
            number += 1
            return still_guess_it(name , number )
        if n > 12:
            print("Your guess is too high.")
            number += 1
            return still_guess_it(name ,  number)
        if n == 12:
            number += 1
            print(f"Good job!, {name}! You guessed my number in {number} guesses!")
    still_guess_it(name , number)

guess_it(name)