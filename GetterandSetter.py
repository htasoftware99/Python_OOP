class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self,age):
        self.__age = age

stud = Student("Hasan", 23)
print("Name: ", stud.name, stud.get_age())

stud.set_age(16)
print("Name: ", stud.name, stud.get_age())