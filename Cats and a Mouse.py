import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    d1 = abs(x-z)
    d2 = abs(y-z)
    if d1 == d2:
        print('Mouse C')
    elif d1 < d2:
        print('Cat A')
    elif d1 > d2:
        print('Cat B')
