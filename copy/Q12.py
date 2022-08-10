class Bill:
    def __init__(self, mobile_number, payment_bill):
        self.mobile_number = mobile_number
        self.payment_bill = payment_bill


class Mobile:
    def __init__(self, service_provider, mobile_number, data_used, payment_method):
        self.service_provider = service_provider
        self.mobile_number = mobile_number
        self.data_used = data_used
        self.payment_method = payment_method

    def claculate_bill(self, listOfObjects):
        rate = 0
        outlist = []
        for obj in listOfObjects:
            if obj.service_provider == 'airtel':
                rate = 11
            if obj.service_provider == 'jio':
                rate = 10
            bill = rate * obj.data_used
            if obj.payment_method == 'paytm' and obj.service_provider == 'airtel':
                disc = 0.1
            else:
                disc = 0
            bill -= bill*disc
            bill = round(bill)
            outlist.append(Bill(obj.mobile_number, bill))
        return outlist


mob1 = Mobile('airtel', 123, 16, 'paytm')
mob2 = Mobile('airtel', 456, 10, 'amazon')
mob3 = Mobile('jio', 789, 10, 'paytm')
lis = [mob1, mob2, mob3]
out = Mobile('', 0, 0, '').claculate_bill(lis)
for i in out:
    print(i.mobile_number, i.payment_bill)
