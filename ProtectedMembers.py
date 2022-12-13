#base class
class Company:
    def __init__(self):
        self._project = "NLP"

#child class
class Employee:
    def __init__(self,name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Name: ", self.name)
        print("Work on: ", self._project)

emp = Employee("Hasan")
emp.show()
print("Project Name: ", emp._project)