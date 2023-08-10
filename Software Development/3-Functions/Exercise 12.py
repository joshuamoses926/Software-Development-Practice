"""
Travel Time Calculator
Consider you're planning a road trip and want to calculate how long it will take to travel a certain distance at a given speed. The following program is supposed to do this calculation, but it contains syntax errors. Can you spot and correct them?
"""

# function travel_time(distance speed):
#     time = distance / speed
#     returns time
 
# distance = 600  # distance in miles
# speed = 60  # speed in mph
 
# print(f"Travel time: {travel_time(distance speed)} hours")

distance = 600  # distance in miles
speed = 60  # speed in mph

def travel_time(distance, speed):
    time = distance / speed
    return time

print(f"Travel time: {travel_time(distance, speed)} hours")