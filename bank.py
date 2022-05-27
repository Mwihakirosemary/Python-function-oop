class Account:
    def __init__(self,bankname,accountnumber,accountname,accountbalance):
        self.accountnumber  = accountnumber
        self.accountname = accountname
        self.accountbalance  = accountbalance
        self.bankname = bankname
    def deposit(self):
        amount = int (input("Enter Amount "))
        amount += self.accountbalance
        return amount
    def withdraw(self):
        amount = int (input("Enter Amount "))
        self.accountbalance -= amount
        return self.accountbalance    
    

        
        