# Account class

class Account:
    accNumber = 1234
    balance = 0.00
    active = 'Active'
    
    # describe attributes of this account
    def describe(self):
        print('Account Number: %d\nBalance: %.2f\nStatus: %s' % (self.accNumber,self.balance,self.active))
#create an instance of Account and use the describe method
acc1 = Account()
#acc1.describe()

#create a subclass from Account

class MobileAccount(Account):
    phoneNumber = '+254 0000-000-000'

    def getNum(self):
        print('Phone Number: %s' % (self.phoneNumber))
acc2 = MobileAccount()
acc2.describe()
acc2.getNum()

