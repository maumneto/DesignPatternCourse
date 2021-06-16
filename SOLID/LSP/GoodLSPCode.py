class AccountManager(object):
    def __init__(self, balance = 0):
        self.balance = balance
    
    def getBalance(self):
        return self.balance

    def withdraw(self, value):
        if self.balance >= value:
            self.balance = self.balance - value
            print('Successful Withdrawal.')
        else:
            print('Insufficient Funds')

    def deposit(self, value):
        self.balance = self.balance + value
        print('Successful Deposit')

    def income(self, rate):
        self.balance = self.balance + self.balance*rate

class AccountCommon(AccountManager):
    def __init__(self, balance = 0):
        super(AccountCommon, self).__init__(balance=balance)

    def getBalance(self):
        return super().getBalance()

    def deposit(self, value):
        super().deposit(value)

    def withdraw(self, value):
        super().withdraw(value)
    
    def income(self, rate):
        super().income(rate)
    
    def message(self):
        print('Common account balance: %.2f', self.getBalance())

class AccountSpetial(AccountManager):
    def __init__(self, balance = 0):
        super(AccountSpetial, self).__init__(balance=balance)

    def getBalance(self):
        return super().getBalance()

    def deposit(self, value):
        super().deposit(value)
    
    def withdraw(self, value):
        super().withdraw(value)

    def message(self):
        print('Common account balance: %.2f', self.getBalance())

if __name__ == '__main__':
    commonAccount = AccountCommon(500)
    commonAccount.deposit(500)
    commonAccount.withdraw(100)
    commonAccount.income(0.005)
    commonAccount.message()
    print(' ------- ')
    spetialAccount = AccountSpetial(1000)
    spetialAccount.deposit(500)
    spetialAccount.withdraw(200)
    spetialAccount.message()

        