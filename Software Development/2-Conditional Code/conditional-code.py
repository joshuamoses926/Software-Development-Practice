balance = 5000
money = 5000
if balance >= money:
    balance -= money
    print(f"Current balance is {balance}")
    print("Transaction complete. Don't forget your card.")
else:
    print("Insufficient funds")
    print(f"Current balance is {balance}")

is_raining = True

if is_raining:
    print("Take your umbrella.")

number = 12

if number % 2 == 0:
    print("The number is even")
if number > 10:
    print("The number is greater than ten")
if number == 12:
    print("A dozen")

traffic_light = "blue"

if traffic_light == "green":
    print("Go!")
elif traffic_light == "yellow":
    print("Slow down and prepare to stop.")
elif traffic_light == "red":
    print("Stop!")
elif traffic_light == "blinking":
    print("Proceed with caution.")
else:
    print("Invalid state.")

traffic_light = "green"
is_blinking = True

if traffic_light == "red":
    if is_blinking:
        print("Stop! Proceed when safe.")    
    else:
        print("Stop!")