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


user1.deposit(100)
user1.deposit(200)
user1.deposit(50)
user1.withdraw(80)
user1.yield_interest()
user1.display_account_info()
user2.deposit(300)
user2.deposit(30)
user2.withdraw(10)
user2.withdraw(40)
user2.withdraw(20)
user2.withdraw(15)
user2.yield_interest()
user2.display_account_info()


