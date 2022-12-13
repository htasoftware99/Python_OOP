class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee("Hasan", 10000)
print("Name: ", emp.name)
# direct access to private member using name mangling
print("Name: ", emp.name, "Salary: ", emp._Employee__salary)
