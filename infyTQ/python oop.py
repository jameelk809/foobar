"""Modular programming"""

"""
def purchase_mobile(price, brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print(total_price)


def purchase_shoes(price, material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    print(total_price)


purchase_mobile(20000, "Apple")
purchase_shoes(1000, "leather")
"""


"""
class Mobile:
    pass


mob1 = Mobile()
mob2 = Mobile()

print(id(mob1))
print(id(mob2))

mob1.price = 20000
mob1.brand = "Apple"
mob1.ios_version = 10
mob1.ios_version = 11  # updating attribute

mob2.price = 3000
mob2.brand = "Samsung"
mob2.android_version = "Marshmallow"

print(mob1.brand, mob1.price, mob1.ios_version)
print(mob2.brand, mob2.price, mob2.android_version)
"""

# Parameterless & Parametrized Constructor

"""
class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        print("Id of self in constructor", id(self))
        self.brand = brand
        self.price = price


mob1 = Mobile("Apple", 20000)
print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)

mob2 = Mobile("Samsung", 3000)
print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)
"""

"""
class Mobile:
    def __init__(self):
        print("Inside the Mobile constructor")
        self.brand = None
        brand = "Apple"  # This is a local variable.
        # Variables without self are local, and they don't affect the attributes.

        # Local variables cannot be accessed outside the init
        # Using self creates attributes which are
        # accessible in other methods as well


mob1 = Mobile()
print(mob1.brand)  # This does not print Apple


# This prints None because brand=Apple creates
# a local variable, and it does not affect the attribute
"""

"""
class Mobile:
    def __init__(self):
        print("Inside constructor")

    def purchase(self):
        print("Purchasing a mobile")


mob1 = Mobile()
mob1.purchase()
"""

"""
class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand", self.brand, "and price", self.price)


print("Mobile-1")
mob1 = Mobile("Apple", 20000)
mob1.purchase()

print("Mobile-2")
mob2 = Mobile("Samsung", 3000)
mob2.purchase()
"""

"""
class Mobile:
    def __init__(self, price, brand):
        print(id(self))
        self.price = price
        self.brand = brand

    def return_product(self):
        print(id(self))
        print("Brand being returned is ", self.brand, " and price is ", self.price)


mob1 = Mobile(1000, "Apple")
print("Mobile 1 has id", id(mob1))

mob2 = Mobile(2000, "Samsung")
print("Mobile 2 has id", id(mob2))

mob2.return_product()
Mobile.return_product(mob2)
"""

# Q1
"""

class Employee:
    def __init__(self):
        self.employee_id = None

    def check_eligibility(self):
        if 9000 <= self.employee_id <= 10000:
            print("The employee is eligible for special benefits")
        else:
            print("The employee is not eligible for special benefits")


emp1 = Employee()
emp1.employee_id = 10000
emp1.check_eligibility()
emp2 = Employee()
emp2.employee_id = 4500
emp2.check_eligibility()
"""

# Q2
"""
class Example:
    def __init__(self, num):
        self.num = num

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num


obj = Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

"""

# Q3
"""
class Example:
    def __init__(self, num):
        self.num = num

    def set_num(self, num):
        num = num

    def get_num(self):
        return self.num


obj = Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

"""

# Q4
"""
class Customer:
    def __init__(self):
        cust_id = 100


c1 = Customer()
print(c1.cust_id)

"""

# Q5
"""
class Customer:
    def __init__(self):
        self.id = 100

c1=Customer()
print(c1.id)
"""

"""
class Customer:
    def __init__(self,id):
        id = 100

c1=Customer(200)
print(c1.id)
"""

"""
class Customer:
    def __init__(self,id1):
        self.id = id1

c1=Customer(200)
print(c1.id1)
"""

"""
class Customer:
    def __init__(self,id1):
        self.id = id1

c1=Customer(200)
print(c1.id)
"""

"""
class Book:
    def __init__(self):
        self.title=None


my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"
print("My favorite is",my_fav.title)
print("Your's is",your_fav.title)
"""

"""
class Customer:
    def __init__(id,self,age):
        id.self=self
        id.age=age

c1=Customer(100,20)
print(c1.self)

"""

"""
class Vehicle:
    def __init__(self, mileage, fuel_left):
        self.mileage = mileage
        self.fuel_left = fuel_left

    def identify_distance_that_can_be_travelled(self):
        return (self.fuel_left - 5) * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        return (initial_fuel - self.fuel_left) * self.mileage


Car = Vehicle(10, 5)
Car.identify_distance_that_can_be_travelled()
Car.identify_distance_travelled(15)
"""

"""
class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material

    def __str__(self):
        return "Shoe with price: " + str(self.price) + " and material: " + self.material


s1 = Shoe(1000, "Canvas")
print(s1)
"""

"""
class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand", self.brand, "and price", self.price)


print("Mobile-1")
mob1 = Mobile("Apple", 20000)
mob1.purchase()
print("Mobile-2")
mob2 = Mobile("Samsung", 3000)
mob2.purchase()
"""

"""
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance          # Private

    def update_balance(self, amount):
        if 1000 > amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.__wallet_balance)


c1 = Customer(100, "Gopal", 24, 1000)
print(c1.__wallet_balance)                              # attribute error
"""

"""
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if 1000 > amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.__wallet_balance)


c1 = Customer(100, "Gopal", 24, 1000)
# If we try to assign a value to a private variable, we end up creating a new attribute in python.
# Thus this code does not give an error, but it is logically flawed and does not produce the intended result.
c1.__wallet_balance = 10000000000
c1.show_balance()
"""

"""
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if 1000 > amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.__wallet_balance)


c1 = Customer(100, "Gopal", 24, 1000)
# _ClassName__AttributeName
c1._Customer__wallet_balance = 10000000000
c1.show_balance()
"""

"""
# ------------------------Getters & Setters---------------------------
class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if 1000 > amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance


c1 = Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
"""

"""
# In the Athlete class given below,
#
# make all the attributes private and
# add the necessary accessor and mutator methods
# Represent Maria, the runner and make her run.

class Athlete:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def running(self):
        if self.__gender == "girl":
            print("150mtr running")
        else:
            print("200mtr running")

    def __str__(self):
        return "Athelete: " + self.__name + ", " + self.__gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


Ath1 = Athlete('Maria', "girl")
print(Ath1)
Ath1.set_name('Ravi')
Ath1.set_gender('boy')
Ath1.running()
print(Ath1)
"""

"""
# Getters & Setters
class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if 1000 > amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance


c1 = Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
"""

"""
# Q4 of 4

class Table:
    def __init__(self):
        self.no_of_legs = 4
        self.__glass_top = None
        self.__wooden_top = None

    def assign_data(self, glass_top, wooden_top):
        self.__glass_top = glass_top
        self.__wooden_top = wooden_top

    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top, wooden_top)
        if self.__glass_top:
            rate = 20000
        elif self.__wooden_top:
            rate = 30000
        else:
            rate = 0
        return rate


dining_table = Table()
rate = dining_table.identify_rate(True, False)
print(rate)
"""

"""
class Vehicle:
    def __init__(self):
        self.__vehicle_cost = None
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__premium_amount = None
        self.__premium_percentage = None

    def calculate_premium(self):
        flag = False
        if self.__vehicle_type == 'TwoWheeler':
            self.__premium_percentage = 2
            flag = True
        elif self.__vehicle_type == "FourWheeler":
            self.__premium_percentage = 6
            flag = True
        if flag:
            self.__premium_amount = (self.__premium_percentage / 100) * self.__vehicle_cost
            return self.__premium_amount
        else:
            return "Invalid"

    def calculate_vehicle_cost(self):
        self.__vehicle_cost += self.__premium_amount
        return self.__vehicle_cost

    def display_vehicle_details(self):
        print("Details are:")
        print("Vehicle Type: ", self.__vehicle_type)
        print("Vehicle ID: ", self.__vehicle_id)
        print("Vehicle Cost: ", self.__vehicle_cost)
        print("Premium Percentage", self.__premium_percentage)
        print("Premium Amount", self.__premium_amount)

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_premium_amount(self):
        return self.__premium_amount

    def get_premium_percentage(self):
        return self.__premium_percentage

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_vehicle_type(self, vehicle_type):
        vehicle_type_list = ['TwoWheeler', 'FourWheeler']
        if vehicle_type in vehicle_type_list:
            self.__vehicle_type = vehicle_type
        else:
            print("INVALID DETAILS")

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount


TwoWheeler = Vehicle()
TwoWheeler.set_vehicle_type('TwoWheeler')
TwoWheeler.set_vehicle_cost(5000)
TwoWheeler.calculate_premium()
TwoWheeler.display_vehicle_details()
"""

"""
class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__technology_skill = None
        self.__experience = None
        self.__avg_feedback = None

    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name

    def get_instructor_name(self):
        return self.__instructor_name

    def set_experience(self, experience):
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill

    def get_technology_skill(self):
        return self.__technology_skill

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def get_avg_feedback(self):
        return self.__avg_feedback

    def check_eligibility(self):
        flag = False
        if self.__experience >= 3 and self.__avg_feedback >= 4.5:
            flag = True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            flag = True
        return flag

    def allocate_course(self, technology):
        if technology in self.__technology_skill:
            return True
        else:
            return False


Teacher = Instructor()
"""

"""
class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees

    def validate_marks(self):
        if 0 <= self.__marks <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False

    def check_qualification(self):
        flag = False
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                flag = True
        return flag

    def choose_course(self, course_id):
        flag = False
        fee_dict = {1001: 25575.0,
                    1002: 15500.0}
        if course_id in fee_dict.keys():
            self.__course_id = course_id
            self.__fees = fee_dict.get(course_id)
            if self.__marks > 85:
                discount = 0.25 * self.__fees
                self.__fees -= discount
                flag = True
        return flag


maddy = Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if maddy.check_qualification():
    print("Student has qualified")
    if maddy.choose_course(1002):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
"""

#   -----------------Printing an Object--------------------------
"""
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __repr__(self):
    #     return "<Test a:%s b:%s>" % (self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s, b is %s" % (self.a, self.b)

    def __repr__(self):
        return 'Test("%s","%s")' % (self.a, self.b)

test = Test(4, 5)
print(test)
print(test.__dict__)

y = eval(repr(test))
print("Human readable: ", str(y))
print('Object representation: ', repr(y))
"""

####################################################################
"""

class Foobar:
    # This will create Foobar type object.

    def __init__(self):
        self.a = None
        print("Foobar object is created.")

    def __repr__(self):
        return "Type what do you want to see here."


a = Foobar()
print(a)
print(a.__dict__)
"""

"""
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand


def change_price(mobile_obj):
    mobile_obj.price = 3000


mob1 = Mobile(1000, "Apple")
change_price(mob1)
print(mob1.price)
"""

#   -------------------List of Objects-------------------------
"""
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


mob1 = Mobile("Apple", 1000)
mob2 = Mobile("Samsung", 2000)
mob3 = Mobile("Apple", 3000)
mob4 = Mobile("Samsung", 4000)
mob5 = Mobile("Apple", 5000)

list_of_mobiles = [mob1, mob2, mob3, mob4, mob5]
for mobile in list_of_mobiles:
    print(mobile.brand, mobile.price)
"""

#   -----------------------Dictionary of Objects-------------------------
"""
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


mob1 = Mobile("Apple", 1000)
mob2 = Mobile("Samsung", 5000)
mob3 = Mobile("Apple", 3000)

mob_dict = {
    "m1": mob1,
    "m2": mob2,
    "m3": mob3
}

for key, value in mob_dict.items():
    if value.price > 3000:
        print(value.brand, value.price)
"""

#   --------------------------Dictionary of list of objects--------------------------
"""
class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location


list_of_customers = [Customer(101, 'Mark', 'US'),
                     Customer(102, 'Jane', 'Japan'),
                     Customer(103, 'Kumar', 'India')]

dict_of_customer = {}
for customer in list_of_customers:
    dict_of_customer[customer.location] = customer
print("Customer name in India is " + dict_of_customer["India"].cust_name)
for key, value in dict_of_customer.items():
    print("Location: " + key + ", Name: " + value.cust_name + ", Id: " + str(value.cust_id))
"""


"""--------------static variables---------------"""


"""
class Mobile:
    discount = 50

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print(self.brand, "mobile with price", self.price, "is available after discount at", total)


#   updating static variables
def enable_discount():
    Mobile.discount = 50


def disable_discount():
    Mobile.discount = 0


mob1 = Mobile(20000, "Apple")
mob2 = Mobile(30000, "Apple")
mob3 = Mobile(5000, "Samsung")

mob1.purchase()
mob2.purchase()
mob3.purchase()
"""

"""
------------------------Private Static Variable----------------------

class Mobile:
    __discount = 50
    def get_discount(self):
        return Mobile.__discount
    def set_discount(self,discount):
        Mobile.__discount = discount


m1 = Mobile()
print(m1.get_discount())
m1.set_discount(90)
print(m1.get_discount())
"""

"""
------------------------------static method--------------------------------

class Mobile:
    __discount = 50

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print("Total is ", total)

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount


print(Mobile.get_discount())
"""

"""
class Mobile:
    __discount = 50

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print(self.brand, "mobile with price", self.price, "is available after discount at", total)

    @staticmethod
    def enable_discount():
        Mobile.set_discount(50)

    @staticmethod
    def disable_discount():
        Mobile.set_discount(0)

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount


mob1 = Mobile(20000, "Apple")
mob2 = Mobile(30000, "Apple")
mob3 = Mobile(5000, "Samsung")

Mobile.disable_discount()
mob1.purchase()
Mobile.enable_discount()
mob2.purchase()
Mobile.disable_discount()
mob3.purchase()
"""

"""
class Mobile:
    counter = 1000

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.mobile_id = Mobile.counter
        Mobile.counter += 1


mob1 = Mobile(20000, "Apple")
mob2 = Mobile(30000, "Apple")
mob3 = Mobile(5000, "Samsung")
print("mobile_id for mob1 is", mob1.mobile_id)
print("mobile_id for mob2 is", mob2.mobile_id)
print("mobile_id for mob3 is", mob3.mobile_id)
print("Current value of counter is", Mobile.counter)
"""

"""
#   Q1
class Lion:
    __water_source = "well in the circus"

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def drinks_water(self):
        print(self.__name,
              "drinks water from the", Lion.__water_source)

    @staticmethod
    def get_water_source():
        return Lion.__water_source


print("Water source of lions:", Lion.get_water_source())
simba = Lion("Simba", "Male")
simba.drinks_water()
"""

"""
#   Q2
class Example:
    num=10
    @staticmethod
    def add(num1,num2):
        result=(num1+num2)*Example.num
        return result
print(Example.add(100, 200))
"""

"""
#   Q3
class Demo:
    num=5
    def __init__(self,status):
        num=10
        print(status,num)
d=Demo('A')
"""

"""
#   Q4
class ClassA:
    __var1 = 20

    def __init__(self, var2):
        self.__var2 = var2

    def method1(self):
        self.__var2 = self.__var2 + 1
        ClassA.__var1 = ClassA.__var1 - 1

    def method2(self):
        print(ClassA.__var1)
        print(self.__var2)


obj1 = ClassA(1)
obj1.method1()
obj1.method2()
obj2 = ClassA(2)
obj2.method2()
"""

"""
#   Q5
class Example:
    def __init__(self):
        self.__num=10
    @staticmethod
    def display():
        self.__num+=1
        print(self.__num)
obj=Example()
obj.display()
"""

"""
#   Q7
class ClassA:
    __var1 = 500

    def __init__(self, var2):
        self.__var2 = var2

    def method1(self, var3):
        self.__var2 = ClassA.__var1 * var3


obj = ClassA(6)
obj.method1(4)
"""

"""
#   Q8
class Util:
    @staticmethod
    def is_valid_number(amount):
        try:
            if (float(amount)) > 0:
                return True
            return False
        except:
            return False


class AccountUI:
    def get_input_for_deposit(self, amount):
        if not Util.is_valid_number(amount):
            print("Amount should be greater than 0. Try again")
        else:
            print("Successfully deposited")


AccountUI().get_input_for_deposit("-2000")
"""

"""
class Ticket:
    counter = 1

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.__source = source
        self.__destination = destination
        self.__ticket_counter = Ticket.counter
        Ticket.counter += 1

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_ticket_id(self):
        return self.__ticket_id

    def validate_source_destination(self):
        flag = False
        destination_list = ['mumbai', 'chennai', 'pune', 'kolkata']
        if self.__source.lower() == 'delhi' and self.__destination.lower() in destination_list:
            flag = True
        return flag

    def generate_ticket(self):
        if self.validate_source_destination():
            self.__ticket_id = ''
            self.__ticket_id += self.__source[0:1] + self.__destination[0:1] + str(0) + str(self.__ticket_counter)
        else:
            self.__ticket_id = None


psngr1 = Ticket('abc', 'Delhi', 'Kolkata')
psngr1.generate_ticket()
print(psngr1.get_ticket_id())
psngr2 = Ticket('abc', 'Delhi', 'Kolkata')
psngr2.generate_ticket()
print(psngr2.get_ticket_id())
"""

"""
class Mobile:
    discount = 50

    def display(self):
        print(self.discount)
        # The above line is a valid way of accessing static
        print(Mobile.discount)

    def change(self):
        self.discount = 40
        # The above line creates a new attribute
        # instead of modifying the static value
        # Now there are two discount variables,
        # one at class level and the other at object level
        # Hence best is to access Static through class name


m1 = Mobile()
m1.display()  # Will display 50 and 50

m1.change()
m1.display()  # Will display 50 and 40
"""

"""
class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
        self.required_quantity = None

    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name

    def get_flower_name(self):
        return self.__flower_name

    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg

    def get_price_per_kg(self):
        return self.__price_per_kg

    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available

    def get_stock_available(self):
        return self.__stock_available

    def validate_flower(self):
        flower_list = ['orchid', 'rose', 'jasmine']
        flag = False
        if self.__flower_name.lower() in flower_list:
            flag = True
        return flag

    def validate_stock(self, required_quantity):
        flag = False
        if required_quantity <= self.__stock_available:
            flag = True
            self.required_quantity = required_quantity
        return flag

    def sell_flower(self, required_quantity):
        self.required_quantity = required_quantity
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= self.required_quantity

    def check_level(self):
        flag = False
        order_level_dict = {'orchid': 15, 'rose': 25, 'jasmine': 40}
        stock = self.get_stock_available()
        if self.validate_flower():
            if stock < order_level_dict.get(self.__flower_name.lower()):
                flag = True
        return flag


flower1 = Flower()
flower1.set_flower_name('Cacti')
flower1.set_price_per_kg(200)
flower1.set_stock_available(53)
print(flower1.validate_flower())
print(flower1.validate_stock(99))
print(flower1.check_level())
"""

"""
class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.__phoneno = phoneno
        self.__called_no = called_no
        self.__duration = duration
        self.__call_type = call_type


class Util:
    def __init__(self):
        self.list_of_call_objects = None

    def parse_customer(self, list_of_call_string):
        self.list_of_call_objects = []
        for item in list_of_call_string:
            item = item.split(',')
            phoneno = item[0]
            called_no = item[1]
            duration = item[2]
            call_type = item[3]
            obj = CallDetail(phoneno, called_no, duration, call_type)
            self.list_of_call_objects.append(obj)
        print(self.list_of_call_objects)


call = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,Local'
call3 = '9990000001,9330000003,6,ISD'

list_of_call_string = [call, call2, call3]
Util().parse_customer(list_of_call_string)
"""

"""
class Bill:
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = None

    def get_bill_id(self):
        return self.__bill_id

    def get_patient_name(self):
        return self.__patient_name

    def get_bill_amount(self):
        return self.__bill_amount

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        bill_amount = 0
        for i in range(len(quantity_list)):
            bill_amount += quantity_list[i] * price_list[i]
        self.__bill_amount = bill_amount + consultation_fees


bill1 = Bill('abc', 101)
"""

"""
class Classroom:
    classroom_list = ['G015', 'G066', 'L123', 'L135', 'L143', 'L13']

    @staticmethod
    def search_classroom(class_room):
        for i in range(len(Classroom.classroom_list)):
            Classroom.classroom_list[i] = Classroom.classroom_list[i].lower()

        if class_room.lower() in Classroom.classroom_list:
            return "Found"
        else:
            return -1


Classroom.search_classroom('l135')
"""

"""=======================AGGREGATION ======================="""

"""
class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.door_no, self.address.street, self.address.pincode)

    def update_details(self, add):
        self.address = add


class Address:
    def __init__(self, door_no, street, pincode):
        self.door_no = door_no
        self.street = street
        self.pincode = pincode

    def update_address(self):
        pass


add1 = Address(123, "5th Lane", 56001)
add2 = Address(567, "6th Lane", 82006)
cus1 = Customer("Jack", 24, 1234, add1)
cus1.view_details()
cus1.update_details(add2)
cus1.view_details()
"""

"""
class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.__door_no, self.address.__street, self.address.__pincode)


class Address:
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode

    def update_address(self):
        pass


add1 = Address(123, "5th Lane", 56001)
cus1 = Customer("Jack", 24, 1234, add1)

cus1.view_details()
"""

"""-------Accessing private attributes of Aggregated class (using getters & setters)-------"""

"""
class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.get_door_no(), self.address.get_street(), self.address.get_pincode())


class Address:
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode

    def get_door_no(self):
        return self.__door_no

    def get_street(self):
        return self.__street

    def get_pincode(self):
        return self.__pincode

    def set_door_no(self, value):
        self.__door_no = value

    def set_street(self, value):
        self.__street = value

    def set_pincode(self, value):
        self.__pincode = value

    def update_address(self):
        pass


add1 = Address(123, "5th Lane", 56001)
cus1 = Customer("Jack", 24, 1234, add1)

cus1.view_details()
"""

"""-----------------Object passed as a parameter----------------"""
"""---------------Dependency via Formal Parameter---------------"""
"""
class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def purchase(self, payment):
        if payment.type == "card":
            print("Paying by card")
        elif payment.type == "e-wallet":
            print("Paying by wallet")
        else:
            print("Paying by cash")


class Payment:
    def __init__(self, type):
        self.type = type


payment1 = Payment("card")
c = Customer("Jack", 23, 1234)

c.purchase(payment1)
"""

"""----------create an object locally inside a method-------"""
"""---------------Dependency via Local Object---------------"""

"""
# Object creation
class Customer:
    def __init__(self, name, cust_type, bill):
        self.name = name
        self.bill = bill
        self.cust_type = cust_type

    def calculate_bill(self):
        tax1 = Tax(self.cust_type)
        final_bill = self.bill * tax1.tax_details(self.cust_type)
        return final_bill


class Tax:
    def __init__(self, cust_type):
        self.cust_type = cust_type

    def tax_details(self, cust_type):
        if cust_type == "Student":
            return 5
        else:
            return 10


cust1 = Customer("Maddy", "Student", 100)
print(cust1.calculate_bill())


# Usage of static
class CustomerCare:
    helpline = 111000


class Customer:
    def call_support(self):
        print("Calling ", CustomerCare.helpline)


Customer().call_support()
"""

#   Q1
"""
class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        print(cover.color)
class Cover:
    def __init__(self):
        self.__color="red"
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
"""

#   Q4
"""
class Customer:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile


class Mobile:
    def __init__(self, brand):
        self.brand = brand

    def unlock(self, cover):
        cover.color = "yellow"


class Cover:
    def __init__(self):
        self.color = "red"


Customer("Cus1", Mobile("Apple")).mobile.unlock(Cover())
print(Cover().color)
"""

#   Q4
"""
class Trade:
    def __init__(self):
        self.__trade_detail = None

    def get_trade_detail(self):
        return self.__trade_detail

    def set_trade_detail(self, value):
        self.__trade_detail = value


class TradeDetail:
    def __init__(self):
        self.__trade_id = None
        self.__order_id = None

    def get_trade_id(self):
        return self.__trade_id

    def get_order_id(self):
        return self.__order_id

    def set_trade_id(self, value):
        self.__trade_id = value

    def set_order_id(self, value):
        self.__order_id = value


T = Trade()
Tr = TradeDetail()
tr = Tr.get_trade_id()
"""

#   Q5
"""
class Mobile:
    def __init__(self, brand, case):
        self.brand = brand
        self.case = case

    def display(self):
        print(self.case.color)


class Case:
    def __init__(self, color):
        self.color = color


c1 = Case("Black")
c2 = Case("White")
m1 = Mobile("Hony", c1)
c1.color = "Green"
m1.display()
"""

"""
class Foo:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.num2 = num2

    def __str__(self):
        return str(self.__dict__)


f1 = Foo(10, 20)
f2 = Foo(20, 30)
f3 = Foo(30, 40)
print(f1, f2, f3)
"""

"""
class Parrot:
    __counter = 7001

    def __init__(self, name, color):
        self.__name = name
        self.__color = color
        self.__unique_number = Parrot.__counter
        Parrot.__counter += 1

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_unique_number(self):
        return self.__unique_number


P = Parrot('ccc', 'sdw')
"""

"""
# The parse_customer method takes a list of Customer objects and a list of CallDetail objects. For every customer,
# identify all the corresponding Call Detail objects (the customer phone number and the phone number of Call detail
# object have to match), add them to the list_of_calls of corresponding customer object and add the updated customer
# object to list_of_customer_calldetail_objects of Util class.

class Customer:
    def __init__(self, phone_no, name, age):
        self.phone_no = phone_no
        self.name = name
        self.age = age
        self.list_of_calls = None


class CallDetail:
    def __init__(self, phone_no, called_no, duration):
        self.phone_no = phone_no
        self.called_no = called_no
        self.duration = duration


class Util:
    def parse_customer(self, list_of_customers, list_of_calls):
        pass


cust1 = Customer(9900009901, 'cust1', 23)
cust2 = Customer(9900009902, 'cust2', 24)
cust3 = Customer(9900009903, 'cust3', 25)
list_of_customers = [cust1, cust2, cust3]

call1 = CallDetail(9900009901, 8800123401, 5)
call2 = CallDetail(9900009903, 8800123402, 10)
call3 = CallDetail(9900009902, 8800123403, 2)
call4 = CallDetail(9900009901, 8800123404, 8)
call5 = CallDetail(9900009901, 8800123405, 7)
call6 = CallDetail(9900009903, 8800123406, 9)
call7 = CallDetail(9900009903, 8800123407, 4)
list_of_calls = [call1, call2, call3, call4, call5, call6, call7]

Util().parse_customer(list_of_customers, list_of_calls)
"""

"""
class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address

    def validate_customer_id(self):
        flag = False
        if 100000 <= self.__customer_id <= 199999:
            flag = True
        return flag

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address


class Freight:
    counter = 198

    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.__freight_id = None
        self.__recipient_customer = recipient_customer
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance
        self.__freight_charge = None
        self.counter += 2

    def validate_weight(self):
        flag = False
        if self.__weight % 5 == 0:
            flag = True
        return flag

    def validate_distance(self):
        flag = False
        if 500 <= self.__distance <= 5000:
            flag = True
        return flag

    def forward_cargo(self):
        if self.get_from_customer().validate_customer_id() and self.get_recipient_customer().validate_customer_id()\
                and self.validate_distance() and self.validate_weight():
            self.__freight_id = self.counter
            self.__freight_charge = self.__distance * 60 + self.__weight * 150
        else:
            self.__freight_charge = 0

    def get_freight_charge(self):
        return self.__freight_charge

    def get_freight_id(self):
        return self.__freight_id

    def get_recipient_customer(self):
        return self.__recipient_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance


c1 = Customer(100989, 'abc', 'ghh')
c2 = Customer(108973, 'sds', 'sss')
f1 = Freight(c1, c2, 50, 501)
f1.forward_cargo()
print(f1.get_freight_charge())
"""

"""==========================Inheritance========================="""

"""
class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

#   name of the parent class in brackets

class FeaturePhone(Phone):
    pass


class SmartPhone(Phone):
    pass


FeaturePhone(10000, "Apple", "13px").buy()
"""

"""
class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val


son = Child(100, 200)
print(son.get_num())
print(son.get_val())
"""

"""
class Parent:
    def __init__(self):
        self.num = 100


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.num)
        print(self.var)


son = Child()
son.show()
"""


"""
def customer_record(customer_type, name, discount, points_earned, membership_card_type):
    if customer_type == "Regular":
        record = "Record Regular Customer:" + name + " " + str(discount)
    elif customer_type == "Privileged":
        record = "Record Privileged Customer:" + name + " " + str(points_earned)
    elif customer_type == "Elite":
        record = "Record Elite Customer:" + name + " " + membership_card_type
    print(record)


customer_record('Regular', 's', 'w', 'q', 'q')
"""

"""
class Parent:
    def __init__(self):
        self.__num = 100

    def show(self):
        print("Parent:", self.__num)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        print("Child:", self.__var)


dad = Parent()
dad.show()
son = Child()
son.show()
"""

"""
class Parent:
    def __init__(self):
        self.__num = 100

    def show(self):
        print("Parent:", self.__num)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        super().show()
        print("Child:", self.__var)


obj = Child()
obj.show()
"""

"""
class Customer:
    def __init__(self):
        self.__cust_id = None
        self.__cust_name = None

    def get_cust_id(self):
        print("Normal customer")

    def get_cust_name(self):
        return self.__cust_name

    def set_cust_id(self, value):
        self.__cust_id = value

    def set_cust_name(self, value):
        self.__cust_name = value


class PrivilegedCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.__overdraft_limit = None

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def set_overdraft_limit(self, value):
        self.__overdraft_limit = value

    def get_cust_id(self):
        print("Privileged Customer")


class RegularCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.__min_balance = None

    def get_min_balance(self):
        return self.__min_balance

    def set_min_balance(self, value):
        self.__min_balance = value


r = RegularCustomer()
p = PrivilegedCustomer()
r.get_cust_id()
p.get_cust_id()
"""

"""--------------------Single Inheritance------------------"""
"""
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

    def get_price(self):
        return self.__price


class SmartPhone(Phone):
    pass


phone1 = SmartPhone(1000, "Apple", "13px")
print(phone1.brand)
print(phone1.get_price())
phone1.buy()
"""

"""------------------Multilevel Inheritance--------------------"""
"""
class Product:
    def review(self):
        print("Product customer review")


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 12)
s.buy()
s.review()
"""

"""-------------------Hierarchical inheritance---------------------"""
"""
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass


class FeaturePhone(Phone):
    pass


SmartPhone(1000, "Apple", "13px").buy()
"""

"""------------------Multiple inheritance--------------------"""
"""
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class Product:
    def review(self):
        print("Customer review")


class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "Apple", 12)

s.buy()
s.review()
"""

"""
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class Product:
    def buy(self):
        print("Product buy method")


class SmartPhone(Product, Phone):
    pass


s = SmartPhone(20000, "Apple", 12)
s.buy()
"""

#   Q:1
"""
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40
class C(B):
    def m2(self):
        return 20
    
obj1 = A()
obj2 = B()
obj3 = C()
a = obj1.m1()
b = obj3.m1()
c = obj3.m2()
print(a+b+c)
# print(obj1.m1() + obj3.m1()+ obj3.m2())
"""

#   Q:2
"""
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        val=super().m1()+30
        return val
class C(B):
    def m1(self):
        val=self.m1()+20
        return val
obj=C()
print(obj.m1())
"""

"""
class Apparel:
    counter = 100

    def __init__(self, price, item_type):
        self.__item_id = None
        self.__price = price
        self.__item_type = item_type
        Apparel.counter += 1
        if self.__item_type == 'Silk':
            self.__item_id = self.__item_type[0:1] + str(Apparel.counter)
        if self.__item_type == 'Cotton':
            self.__item_id = self.__item_type[0:1] + str(Apparel.counter)

    def calculate_price(self):
        service_tax = 0.05 * self.__price
        self.__price += service_tax

    def get_item_id(self):
        return self.__item_id

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def set_price(self, price):
        self.__price = price


class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(self, item_type='Cotton')
        self.__discount = discount
        super().set_price(price)

    def calculate_price(self):
        super().calculate_price()
        price = super().get_price()
        price -= price*self.get_discount()/100
        vat = 0.05 * price
        price += vat
        super().set_price(price)

    def get_discount(self):
        return self.__discount


class Silk(Apparel):
    def __init__(self, price):
        super().__init__(self, item_type='Silk')
        self.__points = None
        super().set_price(price)

    def calculate_price(self):
        super().calculate_price()
        price = super().get_price()
        if price > 10000:
            self.__points = 10
        elif price <= 10000:
            self.__points = 3
        vat = 0.1 * price
        price += vat
        super().set_price(price)

    def get_points(self):
        return self.__points


item2 = Cotton(60, 5)
item2.calculate_price()
print(item2.get_price())

item3 = Silk(50)
item3.calculate_price()
print(item3.get_price())
print(item3.get_points())
print(item3.get_item_id())
"""

"""
class FruitInfo:
    __fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    __fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            i = FruitInfo.__fruit_name_list.index(fruit_name)
            price = FruitInfo.__fruit_price_list[i]
        else:
            price = -1
        return price

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list


class Purchase:
    __counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = None
        self.customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__counter = Purchase.__counter
        Purchase.__counter += 1

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.customer

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        if self.__fruit_name in FruitInfo.get_fruit_name_list():
            price_of_fruit = FruitInfo.get_fruit_price(self.__fruit_name)
            price = price_of_fruit * self.__quantity
            if price_of_fruit == max(FruitInfo.get_fruit_price_list()) and self.__quantity > 1:
                discount = 0.02*price
                price -= discount
            elif price_of_fruit == min(FruitInfo.get_fruit_price_list()) and self.__quantity > 5:
                discount = 0.05 * price
                price -= discount
            if self.customer.get_cust_type() == 'wholesale':
                add_disc = 0.1 * price
                price -= add_disc
            self.__purchase_id = 'P' + str(self.__counter)
        else:
            price = -1
        return price


class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type


cust1 = Customer('aaa', 'wholesale')
fruit1 = Purchase(cust1, 'Apple', 3)
fruit1.calculate_price()
print(FruitInfo.get_fruit_price('Apple'))
"""

"""
#   incomplete
class ThemePark:
    dict_of_games = {"Game1": [35.5, 5], "Game2": [40.0, 6], "Game3": [120.0, 10],
                     "Game4": [60.0, 7], "Game5": [25.0, 4]}

    @staticmethod
    def validate_game(game_input):
        flag = False
        if game_input in ThemePark.dict_of_games.keys():
            flag = True
        return flag

    @staticmethod
    def get_points(game_input):
        return ThemePark.dict_of_games.get(game_input)[1]

    @staticmethod
    def get_amount(game_input):
        return ThemePark.dict_of_games.get(game_input)[0]


class Ticket:
    __ticket_count = 200

    def __init__(self):
        self.__ticket_id = None
        self.__ticket_amount = 0

    def generate_ticket_id(self):
        self.__ticket_id = Ticket.__ticket_count+1

    def calculate_amount(self, list_of_games):
        amount = 0
        flag = True
        for game in list_of_games:
            if game not in ThemePark.dict_of_games.keys():
                flag = False
        if flag:
            for game in list_of_games:
                amount += ThemePark.get_amount(game)
        self.__ticket_amount = amount
        return flag

    def get_ticket_id(self):
        return self.__ticket_id

    def get_ticket_amount(self):
        return self.__ticket_amount


class Customer:
    def __init__(self, ticket):
        self.points_earned = 0
        self.food_coupon = 'No'
        self.ticket = ticket

    def update_food_coupon(self):
        pass

    def book_ticket(self):
        pass

    def play_game(self):
        pass


'''
Represent customers and display all details of the customer, if he is able to 
book the ticket and play the game. Else, display appropriate error message '''
th = ThemePark.get_amount('Game1')
tic = Ticket()
tic.calculate_amount(['Game1', 'Game2'])
player1 = Customer(tic)
"""

"""-------------------------Abstract Classes---------------------------"""

"""
class Product:
    def return_policy(self):
        pass


class Mobile(Product):
    def return_policy(self):
        print("All mobiles must be returned within 10 days of purchase")


class Shoe(Product):
    def return_policy(self):
        print("All shoes must be returned within 7 days of purchase")


m = Mobile()
m.return_policy()

s = Shoe()
s.return_policy()
"""


"""
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass


class Furniture(Product):
    pass


class Mobile(Product):
    def return_policy(self):
        print("All mobiles must be returned within 10 days of purchase")


class Shoe(Product):
    def return_policy(self):
        print("All shoes must be returned within 7 days of purchase")
"""


"""
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass


class Furniture(Product):
    def return_policy(self):
        print('e')


Furniture().return_policy()
"""


"""
#   If a child class overrides the abstract method, 
#   then its own child classes need not override the abstract method.
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass


class Furniture(Product):
    def return_policy(self):
        print("Furnitures cannot be returned")


class Sofa(Furniture):
    pass


Sofa()
"""

"""
# Q1 of 6
# What is the output of the following code snippet?

from abc import ABCMeta, abstractmethod
class Parent(metaclass=ABCMeta):
    def __init__(self):
        self.num=100

    @abstractmethod
    def show(self):
        pass

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=10

    def show(self):
        print(self.num)
        print(self.__var)

obj=Parent()
obj.show()
"""

"""
# Q2 of 6
# What is the output of the following code snippet?
from abc import ABCMeta, abstractmethod
class Parent(metaclass=ABCMeta):
    def __init__(self):
        self.num=5
    @abstractmethod
    def show(self):
        pass

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=10
    def show(self):
        print(self.num)
        print(self.__var)


obj=Child()
obj.show()
"""

"""
# Q3 of 6
# What is the output of the following code snippet?
from abc import ABCMeta, abstractmethod
class Parent(metaclass=ABCMeta):
    def __init__(self):
        print(100)

    @abstractmethod
    def show(self):
        pass

class Child(Parent):
    def __init__(self):
        super().__init__()
        print(10)

obj=Child()
obj.show()
"""

"""
# Q4 of 6
# What is the output of the following code snippet?

from abc import ABCMeta, abstractmethod


class Parent(metaclass=ABCMeta):
    def __init__(self):
        self.num = 5

    @abstractmethod
    def show(self):
        pass


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 10


class GrandChild(Child):
    def show(self):
        print(self.num)
        print(self.var)
        print("This is possible")


obj = GrandChild()
obj.show()
"""

"""
# Q5 of 6
# What will be the output of the code given below?

from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    def __init__(self):
        print("123")
    @abstractmethod
    def method1(self):
        pass
class B(A):
    def method2(self):
        print("456")
obj=B()
obj.method2()
"""

"""
#   INCOMPLETE
from abc import ABCMeta, abstractmethod


class DirectToHomeService(metaclass=ABCMeta):
    counter = 101

    def __init__(self, consumer_name):
        self.__consumer_name = consumer_name
        self.__consumer_number = self.counter
        self.counter += 1

    def get_consumer_number(self):
        return self.__consumer_number

    def get_consumer_name(self):
        return self.__consumer_name

    def calculate_monthly_rent(self):
        pass


class BasePackage(DirectToHomeService):
    def __init__(self):
        self.__base_pack_name = None
        self.__subscription_period = None

    def get_base_pack_name(self):
        return self.__base_pack_name

    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self, base_pack_name):
        pack_list = ["Silver", "Gold", "Platinum"]
        if base_pack_name in pack_list:
            self.base_pack_name = base_pack_name
        else:
            print("Base package name is incorrect, set to Silver")
            self.base_pack_name = 'Silver'

    def calculate_monthly_rent(self):
        pass
"""

"""-------------------------Exception Handling---------------------------"""

"""
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance


class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception()
        if card_no not in self.cards:
            raise Exception()
        if price > self.cards[card_no].balance:
            raise Exception()


card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = {card1.card_no: card1, card2.card_no: card2}
c = Customer(cards)
while True:
    card_no = int(input("Please enter a card number"))
    try:
        c.purchase_item(1200, card_no)
        break
    except Exception as e:
        print("Something went wrong. " + str(e))
"""

"""
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance


class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception("Invalid Price")
        if card_no not in self.cards:
            raise Exception("Wrong card")
        if price > self.cards[card_no].balance:
            raise Exception("Wrong card")


card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = {card1.card_no: card1, card2.card_no: card2}
c = Customer(cards)
while True:
    card_no = int(input("Please enter a card number"))
    try:
        c.purchase_item(1200, card_no)
        break
    except Exception as e:
        if str(e) == "Invalid Price":
            print("Product price is wrong")
            break
        if str(e) == "Wrong card":
            continue
"""

"""
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance


class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception("Invalid Price")
        if card_no not in self.cards:
            raise Exception("Wrong card")
        if price > self.cards[card_no].balance:
            raise Exception("Wrong card")


card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = {card1.card_no: card1, card2.card_no: card2}
c = Customer(cards)
while True:
    card_no = int(input("Please enter a card number"))
    try:
        c.purchase_item(1200, card_no)
    except Exception as e:
        if str(e) == "Invalid Price":
            print("Product price is wrong")
            break
        if str(e) == "Wrong card":
            continue
"""

"""-------------------------custom exceptions--------------------------------"""
"""
class InvalidPrice(Exception):
    pass


class WrongCard(Exception):
    pass


class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance


class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise InvalidPrice("The price is wrong")
        if card_no not in self.cards:
            raise WrongCard("Card is invalid")
        if price > self.cards[card_no].balance:
            raise WrongCard("Card has insufficient balance")


card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = {card1.card_no: card1, card2.card_no: card2}
c = Customer(cards)
while True:
    card_no = int(input("Please enter a card number"))
    try:
        c.purchase_item(1200, card_no)
        break
    except InvalidPrice as e:
        print(str(e))
        break
    except WrongCard as e:
        print(str(e))
        continue
    except Exception as e:
        print("Something went wrong. " + str(e))
"""

"""
#   try-out
class InvalidPrice(Exception):
    pass


class WrongCard(Exception):
    pass


try:
    raise InvalidPrice()
except Exception as e:
    print("Exception")
except InvalidPrice:
    print("InvalidPrice")
except WrongCard:
    print("WrongCard")
"""

"""
try:
    1 / 0
except Exception:
    print("Exception")
except ZeroDivisionError:
    print("Zero division")
"""

"""
# Q1 of 8
# What is the output of the below program?
class InvalidAccountException(Exception):
    pass


class Account:
    account_list = [1001, 1002, 1003, 1004]

    def validate_account(self, account_id):
        status = 0
        for acct_id in self.account_list:
            if account_id == acct_id:
                status = 1
                break
        if status != 0:
            return True
        else:
            raise InvalidAccountException


try:
    account1 = Account()
    account1.validate_account(1006)
    print("Valid account number")
except InvalidAccountException:
    print("Invalid account number")
"""

"""
# Q2 of 8
# What will be the output of the code given below?
class NameLengthException(Exception):
    pass
class EmployeeIdException(Exception):
    pass
class Employee:
    __trials = 0
    def __init__(self, emp_id, emp_name):
        self.__emp_name = emp_name
        self.__emp_id = emp_id
    def validate_name(self):
        try:
            if len(self.__emp_name) < 4:
                Employee.__trials = Employee.__trials+1
                raise NameLengthException
            if not(self.__emp_id.startswith('E')):
                raise EmployeeIdException
        except NameLengthException:
            Employee.__trials = Employee.__trials+1
            print(Employee.__trials)
        except EmployeeIdException:
            Employee.__trials = Employee.__trials+1
            print(Employee.__trials)
emp1 = Employee('E1001', 'Tom')
emp1.validate_name()
emp2 = Employee('1001', 'Tomy')
emp2.validate_name()
"""

"""
# Q3 of 8
# What will be the output of the code given below?
class Project:
    def __init__(self,employee_list):
        self.__employee_list=employee_list

    def validate_employee(self,employee_id):
        try:
            if employee_id not in self.__employee_list:
                raise Exception
                print("1")
        except Exception:
            print("2")

project1=Project([1001,1002,1003])
project1.validate_employee(1005)
print("3")
"""

"""
# Q4 of 8
# What will be the output of the code given below?
class NotEligibleException(Exception):
    pass
class Employee:
    def __init__(self,salary):
        self.__salary=salary

    def check_salary(self):
        if(self.__salary < 2000):
            raise NotEligibleException
            return False
        else:
            return True

emp1=Employee(5000)
emp2=Employee(1000)
try:
    status=emp1.check_salary()
    print(status)
    status=emp2.check_salary()
    print(status)
except NotEligibleException:
    print("Not Eligible")
"""

"""
# Q5 of 8
# What will be the output of the code given below?
class NotEligibleException(Exception):
    pass
class Employee:
    def __init__(self,salary):
        self.__salary=salary

    def check_salary(self):
        try:
            if(self.__salary < 2000):
                raise NotEligibleException
            else:
                return True
        except NotEligibleException:
            print("1")
            raise NotEligibleException

emp1=Employee(1000)
try:
    status=emp1.check_salary()
    print("2")
except NotEligibleException:
    print("3")
"""

"""
# Q6 of 8
# What will be the output of the code given below?
class InvalidEmployeeException(Exception):
    pass
class Project:
    def __init__(self,employee_list):
        self.__employee_list=employee_list

    def validate_employee(self,employee_id):
        flag=False
        for key in self.__employee_list:
            if(key==employee_id):
                flag=True
        if(flag==False):
            raise InvalidEmployeeException
            print("1")
        return True

project1=Project([1001,1002,1003])
try:
    print(project1.validate_employee(1005))
except Exception:
    print("2")
except InvalidEmployeeException:
    print("3")
"""

"""
# Q7 of 8
# What will be the output of the code given below?
class CustomerBusiness:
    def get_customer(self,cust_id):
        if cust_id == "":
            raise InvalidCustomerException()
        return cust_id

class AccountUI:
    def deposit_money_ui(self):
        try:
            cust_id = CustomerBusiness().get_customer("")
        except Exception:
            print("Exception raised")
        except InvalidCustomerException:
            print("Invalid Customer Exception raised")

class InvalidCustomerException(Exception):
    pass

a=AccountUI()
a.deposit_money_ui()
"""

"""
#   Q8
class CustomerBusiness:
    def get_customer(self,cust_id):
        if cust_id == "":
            raise InvalidCustomerException()
        return cust_id
class AccountUI:
    def deposit_money_ui(self):
        try:
            cust_id = CustomerBusiness().get_customer("")
        except InvalidCustomerException:
            print("Invalid Customer Exception raised.")
        except Exception:
            print("Exception raised")
class InvalidCustomerException(Exception):
    pass
a=AccountUI()
a.deposit_money_ui()
"""
