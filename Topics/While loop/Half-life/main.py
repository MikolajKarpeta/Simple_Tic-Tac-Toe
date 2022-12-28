number_of_atoms = int(input())
goal = int(input())
curent = number_of_atoms
days = 0
while curent > goal:
    curent = int(curent/2)
    days += 12

print(days)