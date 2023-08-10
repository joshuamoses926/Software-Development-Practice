"""
Counting Down
In this challenge, you're supposed to write a simple countdown program. The following code is meant to print the countdown from a given positive integer, but something seems to be off. Can you spot and correct the error?
"""

# def countdown(n):
#     while n > 0:
#         print(n)
#         n + 1
 
# countdown(5)

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        
        if n < 0: 
            break
        

countdown(5)