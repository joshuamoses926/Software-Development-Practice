# Program to calculate the area of various shapes

# Calculates the area of a shape
def calculate_area(shape):
    area = 0

    if shape == 'C':
        radius = input("Enter the radius: ")
        area = calculate_circle_area(float(radius))
    elif shape == 'S':
        side = input("Enter the side: ")
        area = calculate_square_area(float(side))
    elif shape == 'R':
        length = input("Enter the length: ")
        width = input("Enter the width: ")        
        area = calculate_rectangle_area(float(length), float(width))
    elif shape == 'O':
        p = input("Enter the value of P: ")
        q = input("Enter the value of q: ")
        area = calculate_rhombus_area(float(p), float(q))
    else:
        print("Invalid selection. Choose 'C', 'S', 'R', or 'O'.")

    return area

# Calculates the area of a square
def calculate_square_area(side: float):
    area = side * side
    return area

# Calculates the area of a rectangle with given length and width
def calculate_rectangle_area(length: float, width: float):
    area = length * width
    return area

# Calculates the area of a circle
def calculate_circle_area(radius: float):
    pi = 3.14
    area = pi * radius ** 2
    return area

# Calculates the area of a rhombus
def calculate_rhombus_area(p: float, q: float):
    area = (p * q) / 2
    return area

# Returns the name of the shape matching the selection
def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'C':
        shape = "circle"        
    elif tag == 'S':
        shape = "square"
    elif tag == 'R':
        shape = "rectangle"
    elif tag == 'O':
        shape = 'rhombus'
    return shape

# Testing
print("""
---------------
Area calculator
---------------
Select a shape:
""")

# Prompt the user to select a shape and wait
selection = input("""\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
\t'O' - Rhombus
""")

area = calculate_area(selection)

print(f"The area of the {get_shape_name(selection)} is {area}")