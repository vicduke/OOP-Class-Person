class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayinfo(self):
        return f"Hello! Your name is {self.name}. You are {self.age} years old. Your gender is {self.gender}"
    
    def __str__(self):
        return self.displayinfo()

# Creating an instance of the Person class
person1 = Person("John",19 ,"male")
# Printing the object 
print(person1)      