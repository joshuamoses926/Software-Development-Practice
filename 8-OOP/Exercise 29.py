"""
Keep Your Bank Account Safe - Encapsulation and Data Hiding in Python
In this exercise, you will practice the principles of encapsulation and data hiding in Python.
Your task is to refactor the  BankAccount class to make its instance variables and the update_balance() method private.
"""

#class BankAccount:
#    def __init__(self, account_number, balance):
#        self._account_number = account_number
#        self._balance = balance

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
 
    def _update_balance(self, new_balance):
        self._balance = new_balance