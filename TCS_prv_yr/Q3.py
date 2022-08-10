class Account:
    def __init__(self, account_no, account_name, account_balance):
        self.account_no = account_no
        self.account_name = account_name
        self.account_balance = account_balance

    def depositAmnt(self, amount):
        self.account_balance += amount

    def withdrawAmnt(self, amount):
        if self.account_balance <= 1000:
            self.account_balance -= amount
            return 1
        else:
            return 0


# acc = Account(120, 'Rajesh', 1500)
# dep = 1200
# withd = 2000
# acc.depositAmnt(dep)
# print('Balance after deposit: ', acc.account_balance)
# res = acc.withdrawAmnt(withd)
# if res == 1:
#     print('Balance after withdrawal: ', acc.account_balance)
# else:
#     print('Insufficient balance')


if __name__ == '__main__':
    acno = int(input())
    acname = input()
    acntbal = int(input())
    depamnt = int(input())
    withamnt = int(input())
    obj = Account(acno, acname, acntbal)
    print('Balance after deposit: ', obj.account_balance)
    res = obj.withdrawAmnt(withamnt)
    if res == 1:
        print('Balance after withdrawal: ', obj.account_balance)
    else:
        print('Insufficient balance')

