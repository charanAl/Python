class BankAccount:
    def __init__(self):
        self.account_number = '876548765543'
        self.__ATM_pin = 1436

    def view_atm_pin(self):
        return self.__ATM_pin                 #getter()
    
    def change_atm_pin(self, new_pin):
        self.__ATM_pin= new_pin                 #setter()

a1=BankAccount()
print(a1.account_number)
print(a1.view_atm_pin())
a1.change_atm_pin('0098')
print(a1.view_atm_pin())