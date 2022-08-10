class Employee:
    def __init__(self, employee_name, designation, salary, overTimeContribution):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = False


class Organization:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def check(self, overtime_threshold):
        for emp in self.employee_list:
            overtime = sum(emp.overTimeContribution.values())
            if overtime >= overtime_threshold:
                emp.overTimeStatus = True
        return self.employee_list

    def calculate_bonus(self, rate):
        amount = 0
        for emp in self.employee_list:
            if emp.overTimeStatus:
                amount += sum(emp.overTimeContribution.values()) * rate
        return amount


"""
emp1 = Employee('Sunita', 'Faculty', 2300, {'jan': 4, 'mar': 6})
emp2 = Employee('Arun', 'Admin', 30000, {'feb': 4, 'mar': 12, 'june': 10})
emp3 = Employee('Dipak', 'Admin', 25000, {'jan': 12, 'july': 5, 'aug': 3})
emplist = [emp1, emp2, emp3]
company = Organization(emplist)
threshold = 18
rate_per_hour = 100
emplist = company.check(threshold)
for employee in emplist:
    print(employee.employee_name, employee.overTimeStatus)
total = company.calculate_bonus(rate_per_hour)
print(total)
"""

a = int(input("Enter no. of employees: "))
lst = []
for i in range(a):
    emp_name = input("Employee name: ")
    desig = input("Designation: ")
    salary = int(input("Salary"))
    b = int(input("no. of bonus months: "))
    dct = {}
    for j in range(b):
        mon = input("Month: ")
        bon = int(input("Bonus"))
        dct[mon.lower()] = bon
    obj = Employee(emp_name, desig, salary, dct)
    lst.append(obj)
obj = Organization(lst)
overtime_threshold = int(input("overtime threshold: "))
rate_per_hour = int(input("rate per hour: "))
lst = obj.check(overtime_threshold)
for i in lst:
    print(i.employee_name, i.overTimeStatus)
total = obj.calculate_bonus(rate_per_hour)
print(total)
