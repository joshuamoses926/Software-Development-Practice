"""
Consider the following program. It aims to print the numbers 0 through 4 using a while loop. This method works, but it requires keeping track of an index and manually updating it in each iteration.

Can you rewrite the function using a for-in loop instead to simplify the code and remove the manual index handling?
"""

#def print_numbers():
#    i = 0
#    while i < 5:
#        print(i)
#        i += 1
 
#print_numbers()

def print_numbers():
    i = 0
    for i in range(5):
        print(i)
        i += 1

print_numbers()