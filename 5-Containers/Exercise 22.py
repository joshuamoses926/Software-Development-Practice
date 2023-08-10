"""
Expanding the Dessert Menu
A restaurant manager is trying to expand the dessert menu, but he's running into some trouble. The menu is represented as a tuple, and he's attempting to add a new item "Carrot Cake" at the end.

His code, however, is throwing an error. Can you help him understand what's going wrong and how to set up the menu correctly?
"""

#desserts = ('Cheesecake', 'Apple Pie', 'Chocolate Cake')
# The manager tries to add "Carrot Cake" to the menu
#desserts.append('Carrot Cake') # Error! Cannot use append with a tuple.
#print(desserts)

desserts = ('Cheesecake', 'Apple Pie', 'Chocolate Cake')
# The manager tries to add "Carrot Cake" to the menu
new_desserts = ('Carrot Cake',)
updated_desserts = desserts + new_desserts
print(updated_desserts)