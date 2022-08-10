class Account:
    def __init__(self, accnNo, accnName, acctBalance):
        self.accNo = accnNo
        self.accnName = accnName
        self.acctBalance = acctBalance


class AccountDemo:
    def __init__(self):
        pass

    def depositAmt(self, account, amount):
        account.acctBalance += amount
        return account.acctBalance

    def withdrawAmount(self, account, amount):
        min_balance = 1000
        balance = account.acctBalance
        if balance - amount < min_balance:
            print("No Adequate Balance")
        else:
            account.acctBalance = balance - amount
        return account.acctBalance


cust1 = Account(120, 'Rajesh', 1500)
deposit = 1200
withdraw = 2000
demo = AccountDemo()
print(demo.depositAmt(cust1, deposit))
print(demo.withdrawAmount(cust1, withdraw))
