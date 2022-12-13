class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    #getter method
    def get_age(self):
        return self.__age
    
    #setter method
    def set_age(self, age):
        self.__age = age
    
stu = Student("Jessa", 14)

print("Name: ", stu.name, "Age: ", stu.get_age())

#changing age using setter
stu.set_age(16)
print("Name: ", stu.name, "Age: ", stu.get_age())