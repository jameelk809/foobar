class Employee:
    def __init__(self, emp_id, emp_name, emp_role, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_role = emp_role
        self.emp_salary = emp_salary

    def increase_salary(self, percentage):
        self.emp_salary += self.emp_salary * percentage/100


class Organisation:
    def __init__(self, org_name, emp_list):
        self.org_name = org_name
        self.emp_list = emp_list

    def calculate_increment(self, emp_role, percentage):
        result = []
        for employee in self.emp_list:
            if employee.emp_role == emp_role:
                employee.increase_salary(percentage)
                result.append(employee)
        return result


# emp1 = Employee(100, 'Rajesh', 'Developer', 40000)
# emp2 = Employee(101, 'Ayesha', 'Developer', 41000)
# emp3 = Employee(102, 'Hari', 'Analyst', 45000)
# emp4 = Employee(103, 'Aman', 'Manager', 60000)
# emp_lis = [emp1, emp2, emp3, emp4]
# o = Organisation('XYZ Corp', emp_lis)
# inp_role = 'Developer'
# inp_percent = 5
# res = o.calculate_increment(inp_role, inp_percent)
# if len(res) != 0:
#     for emp in res:
#         print(emp.emp_name, '\t', emp.emp_salary)
# else:
#     print('No employee found with given role')

if __name__ == '__main__':
    emp_list = []
    count = int(input('Enter no of employees: '))
    for i in range(count):
        eid = int(input('Employee Id: '))
        name = input('Employee Name: ')
        role = input('Employee Role: ')
        salary = int(input('Employee Salary: '))
        emp_list.append(Employee(eid, name, role, salary))
    o = Organisation('XYZ Corp', emp_list)
    inp_role = input('Enter role to be incremented: ')
    inp_percent = int(input('Enter percentage: '))
    res = o.calculate_increment(inp_role, inp_percent)
    if len(res) != 0:
        for emp in res:
            print(emp.emp_name, '\t', emp.emp_salary)
    else:
        print('No employee found with given role')

