class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee("Hasan", 20000)
print("Name: ", emp.name, "Salary: ", emp._Employee__salary)