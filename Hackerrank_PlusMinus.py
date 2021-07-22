n = int(input())
a = input().split()
d = 0
e = 0
f = 0

if len(a) == n:
    print("a")
    for i in range(n):
        if i >= 0:
            d += 1
        if i == 0:
            e += 1
        if i >= 0:
            f += 1    



g = d/n
print(g) 
h = e/n
print(h)
r = f/n
print(r)          