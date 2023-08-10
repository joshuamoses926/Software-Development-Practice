"""
Breaking Free from the Loop
Consider the following program. It aims to print all odd numbers from 1 to 99. However, due to an error, it ends up in an infinite loop. Can you spot and correct the issue?
"""

# def print_odd_numbers():
#     i = 1
#    while i != 100: # i will never equal 100
#        print(i)
#        i += 2
 
#print_odd_numbers()

def print_odd_numbers():
    i = 1
    while i != 100:
        print(i)
        i += 2
        if i > 100:
            break

print_odd_numbers()