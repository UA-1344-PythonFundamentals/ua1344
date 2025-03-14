class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    # @property
    # def account_number(self):
    #      return self.__account_number
    
    # @account_number.setter
    # def account_number(self, account_number):
    #     self._account_number = account_number

    @property
    def account_holder(self):
        return self._account_holder
    
    # @property
    # def balance(self):
    #     return self.__balance
        
    def deposit(self, amount_of_money):
        self.__balance += amount_of_money
        
    def check_balance(self):
        return self.__balance
        
    def withdraw(self, amount_of_money):
        if(self.__balance <= amount_of_money):
            print ("Insufficient funds")
        else:
            self.__balance -=  amount_of_money


    

	
	
my_account = BankAccount("123456789", "John Doe", 1000.0)
print(my_account.account_holder)

try:
    _ = my_account.account_number
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

