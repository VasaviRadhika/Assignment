class Bank:
    def __init__(self, owner, balance=0):

        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
           self.__balance+=amount
    def withdraw(self,amount):
        if 0<amount<self.__balance:
          self.__balance-=amount
        else:
          raise ValueError("insufficient funds")
    def balance(self):
        return self.__balance
account=Bank("vasavi",10000)
print(account.owner,)
print(account.balance(),"initial balance")
account.deposit(50000)
print(account.balance(),"balance after deposit")
account.withdraw(200)
print(account.balance(),"balance after withdraw")
