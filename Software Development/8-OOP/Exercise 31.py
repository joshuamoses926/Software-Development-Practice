"""
Polymorphism at the Zoo
You are given classes Animal, Lion, and Elephant. Your task is to complete the function visit_zoo() that takes a list of animals and prints their sounds.



The Lion class has a make_sound() method that returns "Roar", and the Elephant class has a make_sound() method that returns "Trumpet".

You should call these methods in your visit_zoo() function to print the correct sounds for each animal.
"""

#class Animal:
#    def make_sound(self):
#        return "Animal Sound"
 
#class Lion(Animal):
#    def make_sound(self):
#        return "Roar"
 
#class Elephant(Animal):
#    def make_sound(self):
#        return "Trumpet"
 
#def visit_zoo(zoo):
#        print(animal)
 
#zoo = [Lion(), Elephant(), Lion()]
#visit_zoo(zoo)

class Animal:
    def make_sound(self):
        return "Animal Sound"
 
class Lion(Animal):
    def make_sound(self):
        return "Roar"
 
class Elephant(Animal):
    def make_sound(self):
        return "Trumpet"
 
def visit_zoo(zoo):
    for animal in zoo:
        print(animal.make_sound())
 
zoo = [Lion(), Elephant(), Lion()]
visit_zoo(zoo)