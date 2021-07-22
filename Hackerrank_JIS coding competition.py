
for i in range(int(input())):
    x,y,z,f1,f2 = list(map(int,input().split()))
    m = max(x,y,z)
    if m == x:
        divide = x / 5
        multiply = (y + z) * f2
        print(round(divide + multiply))
    elif m == y:
        divide = y / 5
        multiply = (x + z) * f2
        print(round(divide + multiply))
    else:
        divide = z / 5
        multiply = (x + y) * f2
        print(round(divide + multiply))
    """
    if x >= y and x >= z:
        divide = x/5
        multiply = (y + z)*f2
        print(round(divide+multiply))
    elif y >= x and y >= z:
        divide = y / 5
        multiply = (x + z )* f2
        print(round(divide + multiply))

    else:
        divide = z / 5
        multiply = (x + y) * f2
        print(round(divide + multiply))
    """

"""
import random

n,k = map(int,input().split())
a = map(int,input().split())
l=[]

l_5=[]
for i in range(n):
    l.append(a)

for j in range(n*n):
    l_3 = []
    l_4 = []
    l_1 = random.sample(l,k)
    for num in l_1:
        if num%2==0:
            l_3.append(num)
        else:
            l_4.append(num)

    ma_1 = max(l_3)
    ma_2 = max(l_4)
    ma_x = min(ma_2,ma_1)
    l_5.append(ma_x)

print(min(l_5))
"""