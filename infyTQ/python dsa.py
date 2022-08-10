""""""

"""-----------------------List using Arrays--------------------------------"""

"""
# Do not remove the below import statement
import sys

'''This function provides the capacity, size and space left in the list.
You can invoke it to get the details of the list'''


def list_details(lst):
    # Number of elements that can be stored in the list
    print("Capacity:", (sys.getsizeof(lst) - 36) // 4)

    # Number of elements in the list
    print("Size:", len(lst))

    # Number of elements that can be accommodated in the space left
    print("Space Left:", ((sys.getsizeof(lst) - 36) - len(lst * 4)) // 4)

    # formula changes based on the system architecture
    # (size-36)/4 for 32 bit machines and
    # (size-64)/8 for 64 bit machines

    # 36, 64 - size of an empty list based on machine
    # 4, 8 - size of a single element in the list based on machine


marias_lst = []
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)
"""

"""
#   add operation
import sys


def list_details(lst):
    print("Capacity:", (sys.getsizeof(lst) - 36) // 4)
    print("Size:", len(lst))
    print("Space Left:", ((sys.getsizeof(lst) - 36) - len(lst * 4)) // 4)


marias_lst = []
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)

marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)
"""

"""
#   insert
import sys


def list_details(lst):
    print("Capacity:", (sys.getsizeof(lst) - 36) // 4)
    print("Size:", len(lst))
    print("Space Left:", ((sys.getsizeof(lst) - 36) - len(lst * 4)) // 4)


marias_lst = []
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)

marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.append("Tea Bags")
marias_lst.append("Milk")
marias_lst.append("Biscuit")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.insert(1, "Salt")
print(marias_lst)
print("List details:")
list_details(marias_lst)
"""

"""
#   delete
import sys


def list_details(lst):
    print("Capacity:", (sys.getsizeof(lst) - 36) // 4)
    print("Size:", len(lst))
    print("Space Left:", ((sys.getsizeof(lst) - 36) - len(lst * 4)) // 4)


marias_lst = []
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)

marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.append("Tea Bags")
marias_lst.append("Milk")
marias_lst.append("Biscuit")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.insert(1, "Salt")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.pop()
"""

"""
# lookup example
class Employee:
    def __init__(self, name, emp_id, email_id):
        self.__name = name
        self.__emp_id = emp_id
        self.__email_id = email_id

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_email_id(self):
        return self.__email_id


class OrganizationDirectory:
    def __init__(self, emp_list):
        self.__emp_list = emp_list

    def lookup(self, key_name):
        result_list = []
        for emp in self.__emp_list:
            if key_name in emp.get_name():
                result_list.append(emp)
        self.display(result_list)
        return result_list

    def display(self, result_list):
        print("Search results:")
        for emp in result_list:
            print(emp.get_name(), " ", emp.get_emp_id(), " ", emp.get_email_id())


emp1 = Employee("Kevin", 24089, "Kevin_xyz@organization.com")
emp2 = Employee("Jack", 56789, "Jack_xyz@organization.com")
emp3 = Employee("Jackson", 67895, "Jackson_xyz@organization.com")
emp4 = Employee("Henry Jack", 23456, "Jacky_xyz@organization.com")
emp_list = [emp1, emp2, emp3, emp4]

org_dir = OrganizationDirectory(emp_list)
org_dir.lookup("Jack")
"""

"""
#   Exercise on list using array - Level 1
def update_mark_list(mark_list, new_element, pos):
    mark_list.insert(pos, new_element)
    return mark_list


def find_mark(mark_list, pos1, pos2):
    return mark_list.__getitem__(pos1), mark_list.__getitem__(pos2)


mark_list = [89, 78, 99, 76, 77, 72, 88, 99]
new_element = 69
pos = 2
pos1 = 5
pos2 = 8
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))
"""

"""-----------------------------Linked List--------------------------------"""

"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


item_node = Node("Sugar")
print(item_node.get_data())
"""

#   List using linked list
"""
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail
"""

#   List using linked list - Add & Display operation - Try out
"""
Add a method, add(data) to the LinkedList class to add a new element to the end of the linked list as shown in the 
class diagram. Once done, represent Maria’s new list of items as a linked list and add the following items to the 
linked list: Sugar, Tea Bags, Milk and Biscuit 

Modify the program to add a new method, display() which traverses through the linked list and display the data in 
each node. Once done, display the items in Maria’s list. 

add(data)
1. Create a new node with the data
2. If the linked list is empty (head node is not referring to any other node),
make the head node and the tail node refer to the new node
3. Otherwise,
a. Make the tail node’s link refer to new node
b. Call the new node as tail node

display()
1. Call the head node as temp
2. While temp is not None,
a. Display temp’s data
b. Make the next node as temp
"""

"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


list1 = LinkedList()
list1.add("Sugar")
print("Element added successfully")
list1.add("milk")
list1.display()
print(list1)
# Similarly add all the specified element(s)
"""

#   Assignment Set 1
#   Assignment on List of Strings - Level 1
"""
def merge_list(list1, list2):
    resultant_data = ""
    for i in range(len(list1)):
        data1 = list1[i]
        data2 = list2[len(list2)-1-i]
        merged_data = ""
        if data1 is None:
            merged_data += data2
        elif data2 is None:
            merged_data += data1
        else:
            merged_data += data1 + data2
        resultant_data += merged_data
        if i != len(list1)-1:
            resultant_data += " "
    return resultant_data


list1 = ['T', 'sk', None, 'bl']
list2 = ['ue', 'is', 'y', 'he']
merged_data = merge_list(list1, list2)
print(merged_data)
"""

#   Assignment on List of Strings - Level 2
"""
class Car:
    def __init__(self, model, year, registration_number):
        self.__model = model
        self.__year = year
        self.__registration_number = registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return self.__model + " " + self.__registration_number + " " + str(self.__year)


class Service:
    def __init__(self, car_list):
        self.__car_list = car_list

    def get_car_list(self):
        return self.__car_list

    def find_cars_by_year(self, year):
        found_cars = []
        for cars in self.get_car_list():
            if cars.get_year() == year:
                found_cars.append(cars.get_model())
        if len(found_cars) == 0:
            return None
        else:
            return found_cars

    def add_cars(self, new_car_list):
        #   sorting cars incomplete
        for cars in new_car_list:
            self.get_car_list().append(cars)

    def remove_cars_from_karnataka(self):
        for car in self.get_car_list():
            if car.get_registration_number().startswith('KA'):
                self.get_car_list().remove(car)


car1 = Car("WagonR", 2010, "KA09 3056")
car2 = Car("Beat", 2011, "MH10 6776")
car3 = Car("Ritz", 2013, "KA12 9098")
car4 = Car("Polo", 2013, "GJ01 7854")
car5 = Car("Amaze", 2014, "KL07 4332")
car_list = [car1, car2, car3]
serv1 = Service(car_list)
print(serv1.find_cars_by_year(2010))
add_list = [car4, car5]
serv1.add_cars(add_list)
for car in serv1.get_car_list():
    print(car)
serv1.remove_cars_from_karnataka()
print()
for car in serv1.get_car_list():
    print(car)
"""

#   Assignment on list using array - Level 1
"""
def check_double(list1, list2):
    new_list = []
    for element in list1:
        if 2*element in list2:
            new_list.append(element)
    return new_list


list1 = [11, 8, 23, 7, 25, 15]
list2 = [6, 33, 50, 31, 46, 78, 16, 34]
print(check_double(list1, list2))
"""

#   Assignment on list using array - Level 2
"""
class Player:
    def __init__(self, name, experience):
        self.__name = name
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return self.__name + " " + str(self.__experience)


class Game:
    def __init__(self, players_list):
        self.__players_list = players_list

    def get_player_list(self):
        return self.__players_list

    def sort_players_based_on_experience(self):
        self.__players_list.sort(key=lambda x: x.get_experience(), reverse=True)

    def shift_player_to_new_position(self, old_index_position, new_index_position):
        temp = self.__players_list.pop(old_index_position)
        self.__players_list.insert(new_index_position, temp)

    def display_player_details(self):
        for i in self.__players_list:
            print(i.get_name(), i.get_experience())


player1 = Player("Dhoni", 15)
player2 = Player("Virat", 10)
player3 = Player("Rohit", 12)
player4 = Player("Raina", 11)
player5 = Player("Jadeja", 13)
player6 = Player("Ishant", 9)
player7 = Player("Shikhar", 8)
player8 = Player("Axar", 7.5)
player9 = Player("Ashwin", 6)
player10 = Player("Stuart", 7)
player11 = Player("Bhuvneshwar", 5)
players_list = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11]
game = Game(players_list)
game.sort_players_based_on_experience()

for players in game.get_player_list():
    print(players)

x = lambda a: a + 10
print(x(x(5)))
"""

#   TCS question
"""
class Toy:
    def __init__(self, toy_id, toy_type, price):
        self.toy_id = toy_id
        self.toy_type = toy_type
        self.price = price
        self.discount_applicable = 0
        self.price_after_discount = 0


class Store:
    def __init__(self, toy_list, applicable_discount_details):
        self.toy_list = toy_list
        self.applicable_discount_details = applicable_discount_details

    def calculate_discount(self):
        for toy in self.toy_list:
            price = toy.price
            toy_type = toy.toy_type
            if toy.toy_type in self.applicable_discount_details.keys():
                discount_rate = self.applicable_discount_details.get(toy_type)
            else:
                discount_rate = toy.discount_applicable
            discount_applicable = price * (discount_rate / 100)
            toy.discount_applicable = discount_applicable
            toy.price_after_discount = price - discount_applicable

    def display(self):
        self.toy_list.sort(key=lambda x: x.discount_applicable, reverse=True)
        for toy in self.toy_list:
            print(toy.toy_id, toy.price, (toy.price - toy.discount_applicable))


n = int(input("Enter number of toys: "))
obj_list = []
for i in range(n):
    t_id = str(input("Enter toy_id for " + str(i+1) + " toy: "))
    t_type = str(input("Enter toy type for " + str(i+1) + " toy: "))
    t_price = int(input("Enter price for " + str(i+1) + " toy: "))
    obj = Toy(t_id, t_type, t_price)
    obj_list.append(obj)


#   for reading "toy_type:discount_rate" dictionary
disc_details = dict()
for i in range(3):
    keys = str(input("Enter Toy Type #" + str(i + 1) + "toy: "))
    values = int(input("Enter Discount Rate #" + str(i + 1) + "toy: "))
    disc_details[keys] = values

# toy1 = Toy(101, 'puzzle', 550)
# toy2 = Toy(102, 'Light and sound', 700)
# toy3 = Toy(103, 'puzzle', 600)
# toy4 = Toy(104, 'Soft Toy', 1500)
# 
# obj_list = [toy1, toy2, toy3, toy4]
# disc_details = {'Soft Toy': 12, 'puzzle': 15, 'electronics': 10}


toy_shop = Store(obj_list, disc_details)

toy_shop.calculate_discount()

toy_shop.display()

"""

#   List using linked list - Search operation - Try out
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() is data:
                return temp.get_data()
            temp = temp.get_next()
        return None

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


list1 = LinkedList()
list1.add("Sugar")
list1.add("salt")
node = list1.find_node("salt")
if node is not None:
    print("Node found")
else:
    print("Node not found")
"""

#   List using Linked List - Insert Operation - Try out
"""
insert(data,data_before)
1. Create a new node with the given data
2. If the data_before is None,
    a. Make the new node's link refer to head node 
    b. Call the new node as head node
    c. If the new node's link is None, make it the tail node
3. Else
    a. Find the node with data_before, once found consider it as node_before
    b. Make the new node’s link refer to node_before’s link.
    c. Make the node_before’s link refer to new node
    d. If new node’s link is None, make it the tail node
4. If node with data_before is not found, display appropriate error message
"""
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() is data:
                return temp.get_data()
            temp = temp.get_next()
        return None

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node
        else:
            temp = self.__head
            flag = False
            while temp is not None:
                if temp.get_data() == data_before:
                    flag = True
                    node_before = temp
                    new_node.set_next(node_before.get_next())
                    node_before.set_next(new_node)
                    if new_node is None:
                        self.__tail = new_node
                    break
                temp = temp.get_next()
            if not flag:
                print("Error!   Previous Node not found")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            msg.append("->")
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "HEAD: " + msg + " NULL"
        return msg


list1 = LinkedList()
list1.add("Salt")
list1.add("Sugar")
list1.insert("NewItem", "Sugar")
list1.display()
print(list1)
"""

#   Insert after a Node (using public Linked List)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, current_data, prev_data):
        new_node = Node(current_data)
        if prev_data is None:
            #   inserting at beginning
            new_node.next = self.head
            self.head = new_node
            if new_node.next is None:
                self.tail = new_node
        else:
            temp = self.head
            flag = False
            while temp is not None:
                if temp.data == prev_data:
                    flag = True
                    node_before = temp
                    new_node.next = node_before.next
                    node_before.next = new_node
                    if new_node.next is None:
                        self.tail = new_node
                    break
                temp = temp.next
            if not flag:
                print("Error!   Element not found")

    def display(self):
        temp = self.head
        print("Head\n   |->  ", end="")  # ⤷
        while temp is not None:
            print(temp.data + " -> ", end="")
            temp = temp.next
        print("Tail")


list1 = LinkedList()
list1.add('new1')
list1.add('new2')
list1.add('new4')
list1.insert('new3', 'new2')
list1.insert('new5', 'new4')
list1.insert('new', None)
list1.display()
"""

"""Modify the program to add a new method, delete(data) to delete the node with the data from the linked list. Once 
done, delete Sugar and Milk from Maria’s list using the methods available in LinkedList class. Note: Use the program 
written earlier for including insert(data,data_before) method and enhance it for the above requirement. 

delete(data):
1. Find the node with the given data. If found,
   a. If the node to be deleted is head node, make the next node as head node
      1. If it is also the tail node, make the tail node as None
   b. Otherwise,
      1. Traverse till the node before the node to be deleted, call it temp
      2. Make temp’s link refer to node’s link.
      3. If the node to be deleted is the tail node, call the temp as tail node
      4. Make the node's link as None
2. If the node to be deleted is not found, display appropriate error message
"""
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        print("adding ", data, " into LinkedList....")
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        print("\nHead\n   ⤷  ", end="")
        while temp is not None:
            print(temp.get_data() + " -> ", end="")
            temp = temp.get_next()
        print("Tail")

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() is data:
                return temp.get_data()
            temp = temp.get_next()
        return None

    def insert(self, data, data_before):
        print("inserting ", data, " after ", data_before, "....")
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node
        else:
            temp = self.__head
            flag = False
            while temp is not None:
                if temp.get_data() == data_before:
                    flag = True
                    node_before = temp
                    new_node.set_next(node_before.get_next())
                    node_before.set_next(new_node)
                    if new_node is None:
                        self.__tail = new_node
                    break
                temp = temp.get_next()
            if not flag:
                print("Error!   Previous Node not found")

    def delete(self, data):
        print("deleting ", data, "....")
        flag = False
        if self.find_node(data) is not None:
            flag = True
        temp_node = self.__head
        if flag:
            while temp_node is not None:
                if temp_node.get_data() is data:
                    #   deleting first node
                    if temp_node is self.__head:
                        self.__head = temp_node.get_next()
                        if self.__tail.get_data() is data:
                            self.__tail = None
                        flag = True
                        return
                else:
                    if temp_node.get_next().get_data() is data:
                        temp = temp_node
                        temp_node = temp_node.get_next()
                        if self.__tail.get_data() is data:
                            self.__tail = temp
                        temp.set_next(temp_node.get_next())
                        temp_node.set_next(None)
                        flag = True
                temp_node = temp_node.get_next()
        else:
            print("Error!   Element not present")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist: " + msg
        return msg


list1 = LinkedList()
list1.add("Sugar")
list1.add("Salt")
list1.add("Milk")
list1.insert("Onion", "Milk")
list1.display()
list1.delete("Sugar")
list1.display()
list1.delete("Milk")
list1.display()
list1.delete("Sur")
list1.display()
"""

"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    # This method is added for this tryout alone
    def set_head(self, new_node):
        self.__head = new_node

    # This method is added for this tryout alone
    def set_tail(self, new_node):
        self.__tail = new_node

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

            # You can use the below __str__() to print the elements of the DS object while debugging

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def find_total_nodes(mem_block):
    temp = mem_block.get_head()
    total_nodes = 0
    while temp is not None:
        total_nodes += 1
        temp = temp.get_next()

    return total_nodes


def maximum_contiguous_free_blocks(mem_block):
    temp = mem_block.get_head()
    total_nodes = find_total_nodes(mem_block)
    free_list = []
    free_contiguous_nodes = 0
    if temp.get_data() == "Free":
        free_contiguous_nodes += 1
    prev_data = temp.get_data()
    temp = temp.get_next()
    while temp is not None:
        if temp.get_data() == "Free":
            if prev_data == "Free":
                free_contiguous_nodes += 1
            else:
                free_list.append(free_contiguous_nodes)
                free_contiguous_nodes = 1
        else:
            free_list.append(free_contiguous_nodes)
            free_contiguous_nodes = 0

        prev_data = temp.get_data()
        temp = temp.get_next()
    free_list.append(free_contiguous_nodes)
    max_free_contiguous_nodes = max(free_list)
    return (max_free_contiguous_nodes / total_nodes) * 100


def total_free_blocks(mem_block):
    temp = mem_block.get_head()
    total_blocks = find_total_nodes(mem_block)
    total_free_blocks = 0
    while temp is not None:
        if temp.get_data() == "Free":
            total_free_blocks += 1
        temp = temp.get_next()
    return (total_free_blocks / total_blocks) * 100


def memory_compaction(mem_block):
    temp = mem_block.get_head()
    prev_occupied = None
    prev_free = None
    occupied = None
    free = None
    if temp.get_data() == "Occupied":
        occupied = temp
        prev_occupied = temp
    elif temp.get_data() == "Free":
        free = temp
        prev_free = temp
    temp = temp.get_next()
    while temp is not None:
        if temp.get_data() == "Occupied":
            if occupied is None:
                occupied = temp
            if prev_occupied is None:
                prev_occupied = temp
            else:
                prev_occupied.set_next(temp)
                prev_occupied = temp
        elif temp.get_data() == "Free":
            if free is None:
                free = temp
            if prev_free is None:
                prev_free = temp
            else:
                prev_free.set_next(temp)
                prev_free = temp
        temp = temp.get_next()

    prev_occupied.set_next(free)
    prev_free.set_next(None)
    mem_block.set_head(occupied)
    mem_block.set_tail(prev_free)


mem_block = LinkedList()
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Free")

print("Before compaction")
print("_________________")
print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block), "%")
print("Total free blocks:", total_free_blocks(mem_block), "%")

memory_compaction(mem_block)

print()
print("After compaction")
print("________________")
print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block), "%")
print("Total free blocks:", total_free_blocks(mem_block), "%")
"""

#   Exercise on Linked List Basics - Level 1
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def find_sum(number_list):
    s = 0
    count = 0
    temp = number_list.get_head()
    while temp is not None:
        count += 1
        if count % 2 != 0:
            s += temp.get_data()
        temp = temp.get_next()
    return s


number_list = LinkedList()
number_list.add(10)
number_list.add(20)
number_list.add(30)
number_list.add(40)
number_list.add(50)
number_list.add(60)
number_list.add(70)
number_list.add(80)
number_list.add(90)
number_list.add(100)
number_list.add(110)

print(find_sum(number_list))
"""

#   Exercise on Linked List of Numbers - Level 1
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def replace_maximum(number_list, new_value):
    temp = number_list.get_head()
    maxm = temp.get_data()
    while temp is not None:
        if temp.get_data() > maxm:
            maxm = temp.get_data()
        temp = temp.get_next()
    max_node = number_list.find_node(maxm)
    max_node.set_data(new_value)
    return number_list


number_list = LinkedList()
number_list.add(12)
number_list.add(95)
number_list.add(140)
number_list.add(110)
number_list.add(40)

new_value = 100
number_list = replace_maximum(number_list, new_value)
number_list.display()
"""

# Exercise on linked list of objects - Level 1
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


class Circle:
    def __init__(self, color, radius):
        self.__color = color
        self.__radius = radius

    def __str__(self):
        return self.__color + " " + str(self.__radius)

    def get_color(self):
        return self.__color

    def get_radius(self):
        return self.__radius


class Shape:
    def __init__(self, circle_list):
        self.__circle_list = circle_list

    def get_circle_list(self):
        return self.__circle_list

    def insert_circle(self, new_circle):
        self.get_circle_list().insert(new_circle, None)


circle1 = Circle("Red", 4)
circle2 = Circle("Green", 5)
circle3 = Circle("Purple", 3.5)
new_circle = Circle("Blue", 6)

circle_list = LinkedList()
circle_list.add(circle1)
circle_list.add(circle2)
circle_list.add(circle3)

shape = Shape(circle_list)
shape.insert_circle(new_circle)
shape.get_circle_list().display()
"""

#   Assignment on Linked List of Characters - Level 2
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def create_new_sentence(word_list):
    flag = ''
    new_sentence = ""
    characters = ['*', '/']
    temp = word_list.get_head()
    while temp is not None:
        letter = temp.get_data()
        if flag == 'up':
            letter = letter.upper()
        if letter in characters:
            next_letter = temp.get_next()
            if next_letter.get_data() in characters:
                flag = 'up'
            else:
                new_sentence += " "
        else:
            new_sentence += letter
            flag = ''
        temp = temp.get_next()
    return new_sentence


word_list = LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result = create_new_sentence(word_list)
print(result)
"""

# Assignment on linked list of objects - Level 2
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print( "is not present in Linked list")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


class Child:
    def __init__(self, name, item_to_perform):
        self.__name = name
        self.__item_to_perform = item_to_perform

    def __str__(self):
        return self.__name + " " + self.__item_to_perform

    def get_name(self):
        return self.__name

    def get_item_to_perform(self):
        return self.__item_to_perform


class Performance:
    def __init__(self, children_list):
        self.__children_list = children_list

    def get_children_list(self):
        return self.__children_list

    def change_position(self, child):
        temp = self.get_children_list().get_head()
        count = 1
        rahul = self.get_children_list().find_node(child)
        while temp is not None:
            if count == 3:
                self.get_children_list().insert(rahul.get_data(), temp.get_data())
                self.get_children_list().delete(self.get_children_list().get_head().get_data())
            temp = temp.get_next()
            count += 1

    def add_new_child(self, child):
        self.get_children_list().add(child)


child1 = Child("Rahul", "solo song")
child2 = Child("Sheema", "Dance")
child3 = Child("Gitu", "Plays Flute")
child4 = Child("Tarun", "Gymnastics")
child5 = Child("Tom", "MIME")

children_list = LinkedList()
children_list.add(child1)
children_list.add(child2)
children_list.add(child3)
children_list.add(child4)
children_list.add(child5)
performance = Performance(children_list)
print("The order in which the children would perform:")
performance.get_children_list().display()
print()
print("After Rahul's performance, the schedule would change to:")
performance.change_position(child1)
performance.get_children_list().display()
print()
child6 = Child("Swetha", "Vote of Thanks")
print("After Swetha has joined, the schedule is:")
performance.add_new_child(child6)
performance.get_children_list().display()
"""

"""
Write a python program to remove all duplicate elements from a sorted linked list containing integer data.
Use the LinkedList class and methods in it to implement the above program.

Example:
Input LinkedList: 10 10 20 20 30 30 30 40 50
Output LinkedList: 10 20 30 40 50
"""
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node
        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print("is not present in Linked list")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def remove_duplicates(duplicate_list):
    d_list = []
    temp = duplicate_list.get_head()
    print(duplicate_list)
    while temp is not None:
        temp_data = temp.get_data()
        if temp_data not in d_list:
            d_list.append(temp_data)
        else:
            duplicate_list.delete(temp_data)
        temp = temp.get_next()
    return duplicate_list


duplicate_list = LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

remove_duplicates(duplicate_list)
print(duplicate_list)
"""

#   Assignment on Linked List of Sorted Objects - Level 2
"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node
        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


class BakeHouse:
    counter = 0
    table_list = []

    def __init__(self):
        self.__occupied_table_list = LinkedList()

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate_table(self):
        BakeHouse.counter += 1
        BakeHouse.table_list.append(BakeHouse.counter)

        self.get_occupied_table_list().add(BakeHouse.counter)

    def deallocate_table(self, table_number):
        self.table_list.remove(table_number)
        self.get_occupied_table_list().delete(table_number)


bakehouse = BakeHouse()
bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.get_occupied_table_list().display()
bakehouse.deallocate_table(2)
print()
bakehouse.get_occupied_table_list().display()
bakehouse.allocate_table()
print()
bakehouse.get_occupied_table_list().display()

"""

#   ------------------Stack creation-----------------
"""
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index])
                index -= 1

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while index >= 0:
            msg.append(str(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg


def find_average(num_list):
    # write your logic here

    return num_list


# Push different values to the stack and test your program
num_list = Stack(7)
num_list.push(78)
num_list.push(65)
num_list.push(92)
num_list.push(46)
num_list.push(89)
num_list.push(71)
"""

"""
#   ----------------Queue creation code----------------
class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index])

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while index <= self.__rear:
            msg.append(str(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg


num_queue = Queue(7)
num_queue.enqueue(2)
num_queue.enqueue(7)
num_queue.enqueue(9)
num_queue.enqueue(4)
num_queue.enqueue(6)
num_queue.enqueue(5)
num_queue.enqueue(10)
num_queue.display()
"""

"""
#   Exercise on Searching a String - Level 1
def pattern_search(text, pattern):
    count = 0
    len_text = len(text)
    len_pattern = len(pattern)
    for i in range(len_text - len_pattern + 1):
        substring = text[i:i+len_pattern]
        if substring == pattern:
            count += 1
    return count


text = "MESMERIZING MESSAGE"
pattern = "MES"
result = pattern_search(text, pattern)
print("The given text:", text)
print("Pattern:", pattern)
print("No. of occurrences of the pattern :", result)
"""

"""
#   Exercise on Searching a String index
def find_decreasing_start(list1, start, end):
    for i in range(end):
        if list1[i] > list1[i+1]:
            return i+1


list1 = [1, 4, 7, 8, 9, 5, 4]
start = 0
end = len(list1) - 1
result = find_decreasing_start(list1, start, end)
print("The index position at which the increasing array starts decreasing is:", result)
"""

"""
#   *********************Queue*****************************
class Queue:
    def __init__(self, max_size):

        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while index <= self.__rear:
            msg.append(str(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg


#   *********************Stack*****************************


class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if self.__top == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index])
                index -= 1

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while index >= 0:
            msg.append(str(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg


def separate_boxes(box_stack):
    result = Queue(box_stack.get_max_size())
    temp_stack = Stack(box_stack.get_max_size())
    primary_colors = ['Red', 'Green', 'Blue']
    while not box_stack.is_empty():
        color = box_stack.pop()
        if color not in primary_colors:
            # print("not primary")
            result.enqueue(color)
        else:
            # print("primary")
            temp_stack.push(color)
    while not temp_stack.is_empty():
        box_stack.push(temp_stack.pop())
    return result


# Use different values for stack and test your program
box_stack = Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result = separate_boxes(box_stack)
print()
print("\nBoxes in the stack after modification:")
box_stack.display()
print("\nBoxes in the queue:")
result.display()
"""

#   -------------------sorting----------------------
"""
def swap(num_list, first_index, second_index):
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]


num_list = [2, 3, 89, 45, 67]
print("List before swapping:", num_list)
swap(num_list, 1, 2)
print("List after swapping:", num_list)
"""

"""
def find_next_min(num_list, start_index):
    temp_list = num_list[start_index:]
    return num_list.index(min(temp_list))


num_list = [10, 2, 100, 67]
start_index = 1
print("Index of the next minimum element is", find_next_min(num_list, start_index))
"""

"""
#   ------------------Selection Sort----------------------
def swap(num_list, first_index, second_index):
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]


def find_next_min(num_list, start_index):
    temp_list = num_list[start_index:]
    return num_list.index(min(temp_list))


def selection_sort(num_list):
    for i in range(len(num_list)):
        j = find_next_min(num_list, i)
        swap(num_list, i, j)


num_list = [8, 2, 19, 34, 23, 67, 91]
print("Before sorting;", num_list)
selection_sort(num_list)
print("After sorting:", num_list)
"""

"""
#   Bubble sort no of passes
def swap(num_list, first_index, second_index):
    global no_of_swaps
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]
    no_of_swaps += 1


def bubble_sort(num_list):
    global no_of_passes
    end_index = len(num_list)
    for index1 in range(0, end_index - 1):
        swapped = False
        no_of_passes += 1
        for index2 in range(0, (end_index - index1 - 1)):
            if num_list[index2] > num_list[index2 + 1]:
                swap(num_list, index2, index2 + 1)
                swapped = True
        if not swapped:
            break
        print("At the end of pass-", no_of_passes, ":", num_list)


no_of_swaps = 0
no_of_passes = 0
# num_list = [5, 4, 3, 2, 1]
num_list = [32, 21, 1, 34, 97, 46, 67, 56]
print("In the beginning:", num_list)
print("______________________________________________")
bubble_sort(num_list)
print("______________________________________________")
print("At the end:", num_list)
print("______________________________________________")
print("No. of swaps:", no_of_swaps)
print("No. of passes:", no_of_passes)
"""

"""
#   --------------------Quick Sort----------------------
def swap(num_list, first_index, second_index):
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def quick_sort(num_list, low, high):
    if low >= high:
        return
    split_point = partition(num_list, low, high)
    quick_sort(num_list, low, split_point - 1)
    quick_sort(num_list, split_point + 1, high)


def partition(num_list, low, high):
    pivot = num_list[low]
    i = low + 1
    j = high
    done = False
    while not done:
        while i <= j and num_list[i] <= pivot:
            i = i + 1
        while num_list[j] >= pivot and j >= i:
            j = j - 1
        if j < i:
            done = True
        else:
            swap(num_list, i, j)
    swap(num_list, low, j)
    return j


num_list = [3, 1, 0, 4, 2]
print("Before sorting;", num_list)
l = len(num_list)
quick_sort(num_list, 0, l - 1)
print("After sorting:", num_list)
"""

"""
#   ----------------Merge Sort-------------------
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    l = 0
    r = len(arr) - 1
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: ", arr)
mergeSort(arr, 0, n - 1)
print("\nSorted array is: ", arr)
"""

"""
#   nth Fibonacci term
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(6))
"""


#   Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [1, 2, 3, 4, 5]
search_element = 3
print(search_element, "is at: ", linear_search(arr, search_element) + 1)


# Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
