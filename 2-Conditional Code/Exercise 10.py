"""
A Day at the Zoo
You are visiting a zoo and want to know what animals you can see depending on the time and day of your visit. The zoo has the following rules:

On weekdays:

In the morning, you can see the lions.

In the afternoon, you can see the elephants.

At night, the zoo is closed.

On weekends:

In the morning, you can see the pandas.

In the afternoon, you can see the penguins.

At night, the zoo is closed.

Unfortunately, the zoo's program is not working. Can you make the necessary changes to fix it?
"""
# day = "weekday"
# time = "morning"
# animals = "unknown"
# zoo_closed = False

# if day == "weekday":
    # Check time
#     if time == "morning":
#         animals = "unknown"
#     elif time == "afternoon":
#         animals = "unknown"
#     else:
#         zoo_closed = True
# elif day == "weekend":
    # Check time
#     if time == "morning":
#        animals = "unknown"
#    elif time == "afternoon":
#        animals = "unknown"
#    else:
#        zoo_closed = True

#if zoo_closed:
#    print("The Zoo is closed.")
#else:
#    print(f"You can see the {animals}.")

day = "weekday"
time = "morning"
animals = "unknown"
zoo_closed = False

if day == "weekday":
    # Check time
    if time == "morning":
        animals = "lions"
    elif time == "afternoon":
        animals = "elephants"
    else:
        zoo_closed = True
elif day == "weekend":
    # Check time
    if time == "morning":
        animals = "pandas"
    elif time == "afternoon":
        animals = "penguins"
    else:
        zoo_closed = True

if zoo_closed:
    print("The Zoo is closed.")
else:
    print(f"You can see the {animals}.")