class Employee:
    #constructor
    def __init__(self, name, salary, project):
        #data members
        self.name = name
        self.salary = salary
        self.project = project

    #method
    #to display employee's details
    def show(self):
        print("Name: ", self.name, ", Salary: ", self.salary)
    def work(self):
        print(self.name, "is working on", self.project)

emp = Employee("Hasan", 10000, "Nlp")

emp.show()
emp.work()