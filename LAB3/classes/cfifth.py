class Account:
    def __init__(self , owner ,  balance ):
        self.owner = owner
        self.balance = balance 
    def deposit(self, k ):
        old = self.balance 
        self.balance *= (k / 100 ) + 1
        print(f"the bank deposit rate of jokes is {k} percent ,your balance has been increased by {int(self.balance - old )} , the account balance is {self.balance}")
    def withdraw(self , minus ):
        if self.balance - minus > 0:
            self.balance-= minus 
            print(f"{minus} was withdrawn from your balance , the account balance is {self.balance}")
        else:
            print(f"You don't have enough money for it! the account balance is {self.balance}")
me = Account(555 , 566)
me.deposit(16)
me.withdraw(660)