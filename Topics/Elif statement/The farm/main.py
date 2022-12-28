prices = {"Chicken": 23, "Goat": 678, "Pig": 1296, "Cow": 3848, "Sheep": 6769}

money = int(input())

if money >= 6769:
    print(int(money/prices["Sheep"]), "sheep" if int(money/prices["Sheep"]) == 1 else "sheep")
elif money >= 3848:
    print(int(money/prices["Cow"]), "cow" if int(money/prices["Cow"]) == 1 else "cows")
elif money >= 1296:
    print(int(money/prices["Pig"]), "pig" if int(money/prices["Pig"]) == 1 else "pigs")
elif money >= 678:
    print(int(money/prices["Goat"]), "goat" if int(money/prices["Goat"]) == 1 else "goats")
elif money >= 23:
    print(int(money/prices["Chicken"]), "chicken" if int(money/prices["Chicken"]) == 1 else "chickens")
else: print("None")