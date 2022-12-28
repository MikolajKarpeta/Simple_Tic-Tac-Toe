n = int(input())
victories = 0

win_list = []
victories_list = []
for i in range(n):
    win_list.append(input().split())

for i in range(n):
    if win_list[i][1] == "win":
        victories_list.append(win_list[i][0])
        victories += 1


print(victories_list)
print(victories)