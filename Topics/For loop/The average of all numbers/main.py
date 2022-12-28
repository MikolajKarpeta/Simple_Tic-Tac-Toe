# put your python code here

a = int(input())
b = int(input())
c = 0
d = 0
for n in range (a,b+1):
    if n % 3 == 0:
        c += n
        d += 1

print(c/d)