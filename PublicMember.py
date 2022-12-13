class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name: ", self.name, "Salary: ", self.salary)

emp = Employee("Hasan", 15000)

print("Name: ", emp.name, "Salary", emp.salary)
emp.show()