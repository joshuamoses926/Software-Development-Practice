"""
Safe Division
Here's an example function that tries to divide two numbers. However, it's not prepared for the case when the divisor is zero. Your task is to fix this problem. When division by zero occurs, your function should handle the exception and return "Cannot divide by zero." instead of crashing.
"""

#def safe_division(numerator, divisor):
#    try:
#        result = numerator / divisor
#        return result

#print(safe_division(5, 0))

def safe_division(numerator, divisor):
    try:
        result = numerator / divisor
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

print(safe_division(5, 0))