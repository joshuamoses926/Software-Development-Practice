"""
Cleaning Up the Lab Inventory
You are working in a laboratory, and your task is to clear the inventory of the chemical substances that are no longer needed.
You have a Python dictionary, where each key is a chemical substance, and its value is the quantity in the inventory.

You've been instructed to remove "Hydrogen Peroxide" from the inventory. Can you modify the dictionary to reflect this change?
"""

#inventory = {"Hydrochloric Acid": 10, "Sodium Hydroxide": 5, "Hydrogen Peroxide": 3, "Ethanol": 15}
#print(inventory)

inventory = {"Hydrochloric Acid": 10, "Sodium Hydroxide": 5, "Hydrogen Peroxide": 3, "Ethanol": 15}

del inventory["Hydrogen Peroxide"]
print(inventory)