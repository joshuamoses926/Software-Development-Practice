"""
Spotting the Invisible Performance Killer
Can you detect what part of the code is unnecessary in the  circle_area() function for calculating the area of the circle?

Refactor the function by removing the unnecessary operation while ensuring the function's result remains the same.
"""

#def circle_area(radius):
#    pi = math.pi
#    sqrt_radius = math.sqrt(radius)
#    squared_radius = radius ** 2
#    area = pi * squared_radius
#    return area
    
#print(circle_area(5))

import math

def circle_area(radius):
    pi = math.pi
    squared_radius = radius ** 2
    area = pi * squared_radius
    return area
    
print(circle_area(5))
