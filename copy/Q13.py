class Payslip:
    def __init__(self, basicSalary, hra, ita):
        self.basicSalary = basicSalary
        self.hra = hra
        self.ita = ita


class PayslipDemo:
    def __init__(self):
        pass

    def getHighestPF(self, listOfObjects):
        res = []
        for obj in listOfObjects:
            res.append(round(obj.basicSalary * 0.12))
        return max(res)


# p1 = Payslip(10000, 2000, 1000)
# p2 = Payslip(50000, 3000, 2000)
# lis = [p1, p2]
# demo = PayslipDemo()
# out = demo.getHighestPF(lis)

if __name__ == '__main__':
    c = int(input())
    lis = []
    for i in range(c):
        bS = int(input())
        hr = int(input())
        it = int(input())
        lis.append(Payslip(bS, hr, it))
    demo = PayslipDemo()
    print(demo.getHighestPF(lis))
