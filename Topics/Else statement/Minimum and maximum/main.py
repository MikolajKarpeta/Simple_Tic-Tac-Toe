biggest = int(input())
smalest = int(input())


if biggest < smalest:
    biggest, smalest = smalest, biggest


print(biggest, "\n" ,smalest)