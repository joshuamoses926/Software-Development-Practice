"""
Define a Class with Methods
Can you create a class that represents a rectangle, with methods to calculate its area and perimeter? Here's the initial code, but it has some issues.
"""

#class Rectangle:
#    def __init__(self, length, width):
#        self.length = length
#        self.width = width

#    def area(self):
#        return length * width

#    def perimeter(self):
#        return 2 * (self.length + self.width)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)