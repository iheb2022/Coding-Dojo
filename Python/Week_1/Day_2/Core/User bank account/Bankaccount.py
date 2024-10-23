class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance<amount:
            print( "Insufficient funds: Charging a $5 fee")
            self.balance = self.balance -5
        return self
    def display_account_info(self):
        print(f"Balance {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    
user1= BankAccount(0.1,200)
user2= BankAccount(0.1,300)


user1.deposit(100).deposit(200).deposit(50).withdraw(80).yield_interest().display_account_info()
user2.deposit(300).deposit(30).withdraw(10).withdraw(40).withdraw(20).withdraw(15).yield_interest().display_account_info()
