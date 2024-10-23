from Bankaccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate=0.02, balance=0)

    
    
    def make_deposit(self, amount):
        self.account.balance = self.account.balance + amount
        
    def make_withdrawal(self, amount):
        self.account.balance = self.account.balance - amount

    def display_user_balance(self):
        print(self.account.balance)
        



