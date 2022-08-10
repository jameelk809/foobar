class Appartment:
    def __init__(self, flat_number, owner_name, electricity_bill_amount):
        self.flat_number = flat_number
        self.owner_name = owner_name
        self.electricity_bill_amount = electricity_bill_amount


class ApartmentDemo:
    def __init__(self):
        pass

    def getSecondBill(self, listOfObjects):
        bill = []
        for obj in listOfObjects:
            bill.append(obj.electricity_bill_amount)
        bill.sort()
        return bill[1]


ap1 = Appartment(1000, 'Hari', 5000)
ap2 = Appartment(1001, 'Hena', 5002)
ap3 = Appartment(1002, 'Harsh', 5001)
lis = [ap1, ap2, ap3]
demo = ApartmentDemo()
print(demo.getSecondBill(lis))
