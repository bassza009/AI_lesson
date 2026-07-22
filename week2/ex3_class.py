import numpy as np

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def set_name(self,name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def display_info(self):
        print(f"Name : {self.name} age {self.age}")

#Example
person1 = Person("Pawat",21)

print("Initial Information")
person1.display_info()