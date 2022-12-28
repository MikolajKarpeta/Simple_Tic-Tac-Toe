name_and_surname = input().split()

if len(name_and_surname) != 2:
    print("You need to enter exactly 2 words. Try again!")
else: print(f"Welcome to our party, {name_and_surname[0]} {name_and_surname[1]}")