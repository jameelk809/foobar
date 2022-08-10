class Employee:
    def __init__(self, empno, empname, leaves):
        self.empno = empno
        self.empname = empname
        self.leaves = leaves


class Company:
    def __init__(self, cname, emps):
        self.cname = cname
        self.emps = emps

    def display_leaves(self, empno, leave_type):
        pass

    def leave_application(self, empno, leave_type, no_of_leaves):
        pass


emp1 = Employee(1, 'Rajesh', {'Cl': 5, 'El': 10, 'SL': 3})
