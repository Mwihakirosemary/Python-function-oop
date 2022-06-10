class Account:
    def __init__(self,accountnumber,accountname):
        self.accountnumber  = accountnumber
        self.accountname = accountname
        self.accountbalance  = 0
        self.deposits=[]
        self.withdrawals=[]

    def deposit(self, amount):
        if amount<=0:
           return f"Hello your deposited amount {amount} this is your new balance {self.accountbalance}"    
        else:
            self.accountbalance+=amount
            self.deposits.append(amount)
            return f"You have deposited {amount}. Your new balance is {self.accountbalance}"
   
    def withdraw(self, amount):
        if amount>self.accountbalance:
           return f"Your balance is {self.accountbalance}, you cannot withdraw {amount}"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount} your balance is {self.accountbalance}"
       
    def deposits_statement(self):
          print(*self.deposits, sep="\n")  
         
    def withdrawals_statement(self):
        print(*self.withdrawals, sep="\n")  
    

        
        