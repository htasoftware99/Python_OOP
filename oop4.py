class Company:
    def __init__(self):
        self._project = "Nlp"

class Employee(Company):
    def __init__(self,name):
        self.name = name
        Company.__init__(self)
    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class 
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show() # Direct access protected data member
print('Project:', c._project)