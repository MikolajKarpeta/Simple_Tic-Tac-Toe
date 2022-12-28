# the list "students" is already defined
new_list = []
for i in range(len(students)):
    if students[i][1] == "A":
        new_list.append(students[i][0])

print(new_list)