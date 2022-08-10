class PropertyDealer:
    def __init__(self, reg_no, dealer_commission):
        self.reg_no = reg_no
        self.dealer_commission = dealer_commission


def fulfill(dealers, details):
    property_list = list(property_dict.keys())
    property_list.sort()
    commission = 0
    comm_list = {}
    for dealer in dealers:
        deal_list = list(dealer.dealer_commission.keys())
        deal_list.sort()
        if property_list == deal_list:
            print('here')
            for item in details.items():
                print(item[1])
                property_type = item[0]
                rate = dealer.dealer_commission.get(property_type)
                commission += item[1] * rate//100
            comm_list[dealer.reg_no] = commission
            comm = list(comm_list.items())
            mini = min(comm)



            # property_price =
            # commision =
        else:
            return None


p1 = PropertyDealer(10111, {'Land': 60, 'House': 30, 'commercial space': 30})
p2 = PropertyDealer(10201, {'Land': 50, 'House': 30, 'commercial space': 20})
p3 = PropertyDealer(103011, {'Land': 50, 'House': 30})
p4 = PropertyDealer(104111, {'Land': 40, 'commercial space': 30})

dealer_list = [p1, p2, p3, p4]

property_dict = {'Land': 500000, 'House': 300000, 'commercial space': 200000}

fulfill(dealer_list, property_dict)
