class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def show(self):
        print("Name: ", emp.name, "Salary: ", emp.__salary)

emp = Employee("Hasan", 10000)
# print("Salary: ", emp.__salary)
emp.show()