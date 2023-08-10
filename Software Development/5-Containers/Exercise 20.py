"""
Expanding the Circle of Friends
Your circle of friends is growing! You've been asked to add two new friends, Ella and Fiona, to the existing friends list.

Ella is supposed to be added at the end of the list, and Fiona in the third position.
However, the following program doesn't work as expected. Can you fix it?
"""

#friends = ['Alice', 'Bob', 'Charlie', 'Danny']
#friends[3] = 'Fiona'
#friends[5] = 'Ella'
#print(friends)

friends = ['Alice', 'Bob', 'Charlie', 'Danny']
friends.insert(2, 'Fiona')
friends.append('Ella')
print(friends)