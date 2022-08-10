class Item:
    def __init__(self, item_id, item_name, item_price, quantity_available):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.quantity_available = quantity_available

    def calculate_price(self, quantity):
        if quantity <= self.quantity_available:
            price = quantity * self.item_price
            return price
        else:
            return 0


class Store:
    def __init__(self, item_list):
        self.item_list = item_list

    def generate_bill(self, item_dict):
        bill = 0
        for item in item_dict.keys():
            for obj in self.item_list:
                if item == obj.item_name:
                    price = obj.calculate_price(item_dict[item])
                    bill += price
        return bill


# item1 = Item(1, 'bread', 30, 5)
# item2 = Item(2, 'butter', 20, 3)
# item3 = Item(3, 'milk', 50, 10)
# dct = {'bread': 2, 'butter': 2}
# lst = [item1, item2, item3]
# store = Store(lst)
# print(store.generate_bill(dct))

if __name__ == '__main__':
    item_list = []
    count = int(input())
    for i in range(count):
        id = int(input())
        name = input()
        price = int(input())
        quantity = int(input())
        item_list.append(Item(id, name, price, quantity))
    s = Store(item_list)
    d = {}
    d_count = int(input())
    for i in range(d_count):
        name = input()
        quantity = int(input())
        d[name] = quantity
    print(s.generate_bill(d))
