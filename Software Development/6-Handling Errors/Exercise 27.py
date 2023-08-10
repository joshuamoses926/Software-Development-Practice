"""
Unusual Birthdays
Your task is to enhance the unusual_birthday(birth_year: int) -> int function that takes a person's birth year as an integer and returns their age.

If the birth year is less than 1900 or more than the current year, raise a ValueError with the message "Invalid birth year".
"""

#def unusual_birthday(birth_year):
    # raise ValueError is birth_year < 1900 or birth_year > current year
#    current_year = date.today().year
    # Calculate the age
#    age = current_year - birth_year
#    return age

from datetime import date

def unusual_birthday(birth_year):
    current_year = date.today().year

    if birth_year < 1900 or birth_year > current_year:
        raise ValueError("Invalid birth year")

    # Calculate the age
    today = date.today()
    birth_date = date(birth_year, today.month, today.day)
    age = current_year - birth_year

    # Adjust age if birthday hasn't occurred yet this year
    if today < birth_date:
        age -= 1

    return age
