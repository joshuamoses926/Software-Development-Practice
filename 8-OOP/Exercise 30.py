"""
Barking up the Inheritance Tree
You have been given a simple Python program that includes two classes: Animal and Dog. The Dog class seems to be repeating a lot of information already provided by the Animal class.


Your task is to add and modify code in the Dog class so that it properly inherits from the Animal class. You'll also need to override the description method to add breed information for the Dog class.
"""

#class Animal:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
 
#    def description(self):
#        return f"I'm {self.name}, a {self.age} year old animal."
 
#class Dog(Animal):
#    def __init__(self, name, age, breed):
#        self.name = name
#        self.age = age
#        self.breed = breed
 
#    def description(self):
#        return f"Woof! I'm {self.name}, a {self.age} year old {self.breed}."

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def description(self):
        return f"I'm {self.name}, a {self.age} year old animal."
 
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
 
    def description(self):
        return f"Woof! I'm {self.name}, a {self.age} year old {self.breed}."