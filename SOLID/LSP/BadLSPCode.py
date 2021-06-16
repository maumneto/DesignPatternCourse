class AccountCommon(object):
    def __init__(self, balance = 0):
        self.balance = balance
    
    def getBalance(self):
        return self.balance

    def withdraw(self, value):
        if self.balance >= value:
            self.balance = self.balance - value
        else:
            print('Insufficient Funds')

    def deposit(self, value):
        self.balance = self.balance + value

    def income(self):
        self.balance = self.balance + self.balance*0.005

class AccountSpecial(AccountCommon):
    def __init__(self, balance=0):
        super(AccountSpecial, self).__init__(balance=balance)

    def income(self):
        print('There is no income on this account!')

if __name__ == '__main__':
    account1 = AccountCommon(1000)
    print('Balance value: ', account1.getBalance())
    account1.income()
    print('New Balance value: ', account1.getBalance())
    account2 = AccountSpecial(2000)
    print('Balance value: ', account2.getBalance())
    account2.income()
    print('New Balance value: ', account2.getBalance())