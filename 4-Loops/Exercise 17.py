"""
Control the Flow - Break and Continue
The following program aims to print numbers 1 to 10 but skips 5 and stops after 7. However, there's an issue in the loop control statements that causes it not to work as expected. Can you find the problem and correct it?
"""

#for i in range(1, 11):
#    if i == 5:
#        break
#    elif i > 7:
#        continue
#    print(i)

for i in range(1, 11):
    if i > 7:
        break
    elif i == 5 :
        continue
    print(i)
