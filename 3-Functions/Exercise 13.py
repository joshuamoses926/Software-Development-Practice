"""
Scope It Out
Consider the following program that calculates the area of a rectangle. However, something doesn't seem right. Can you find the issue and correct it?
"""

# def calculate_area(length, width):
#     area = length * width
 
# calculate_area(10, 5)
# print(f"The area of the rectangle is {area} square units.")

def calculate_area(length, width):
    area = length * width
    return area

area = calculate_area(10, 5)
print(f"The area of the rectangle is {area} square units.")