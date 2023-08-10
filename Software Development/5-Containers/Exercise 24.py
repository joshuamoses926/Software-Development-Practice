"""
Updating the Shopping List
You're helping out in a grocery store, and there's a shopping list stored in a Python dictionary. Each key represents an item, and each value is the quantity needed.
However, the manager just told you that they need more oranges. The quantity for oranges in the list should be updated to 15. Can you modify the dictionary to reflect this change?
"""

#shopping_list = {"apples": 10, "bananas": 5, "oranges": 10, "kiwis": 3}
#print(shopping_list["oranges"])

shopping_list = {"apples": 10, "bananas": 5, "oranges": 10, "kiwis": 3}
shopping_list["oranges"] = 15

print(shopping_list["oranges"])