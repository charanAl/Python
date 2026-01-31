class Bank_Account:
    bank_name = "Kotak Mahindra Bank"
    def __init__(self, acc_no, acc_balance):
        self.account_number = acc_no
        self.account_balance = acc_balance

    
    def show_info(self):
        print('bank name:',Bank_Account.bank_name)
        print('account number:', self.account_number)
        print('account balance:', self.account_balance)


account1 = Bank_Account('KOTAK0001234', 10000)
account2 = Bank_Account('987654321066', 5000)

account1.show_info()
account2.show_info()