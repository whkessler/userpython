class User:
    def __init__ (self,name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        if amount > self.account_balance:
            print ("insufficient funds")
        self.account_balance -= amount
    def display_user_balance(self):
        print (self.account_balance)
John = User("John Smith")
Andrew = User("Andrew Jones")
Jane = User("Jane Curtan")
John.make_deposit(100)
John.make_deposit(360)
John.make_deposit(20)
John.make_withdrawal(330)
print(John.account_balance)
Andrew.make_deposit(3245)
Andrew.make_deposit(23)
Andrew.make_withdrawal(654)
Andrew.make_withdrawal(345)
print(Andrew.account_balance)
Jane.make_deposit(1000)
Jane.make_withdrawal(25)
Jane.make_withdrawal(345)
Jane.make_withdrawal(999)
print(Jane.account_balance)

