#Create a BankAccount class where:
#1. The __init__ method initializes the account with an account number, account holder's name, and balance.
#2. A deposit method that adds a specified amount to the balance.

class BankAccountL:
    class Bank_name : "State Bank of India"
    def __init__(self, account_number, account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance 
    
obj = BankAccountL("SBIN0001234", 5000)
print("Account Number:",obj.account_number)
print("Account Balance:",obj.account_balance)
print("Account FianlAmount:",obj.deposit(2000))
