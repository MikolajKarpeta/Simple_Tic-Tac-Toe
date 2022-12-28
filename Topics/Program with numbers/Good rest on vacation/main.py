# put your python code here

days = int(input())
food_cost = int(input())
one_way_flight = int(input())
one_night_cost = int(input())

total = ((days-1) * one_night_cost) + (food_cost * days) + (one_way_flight * 2)
print(total)