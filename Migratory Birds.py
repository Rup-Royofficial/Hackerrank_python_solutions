import sys


n = int(input().strip())
l =list( map(int, input().strip().split(' ')))
l.sort()
ans=l[0]
count=1
max=1
for i in range(1,n):
    if l[i]==l[i-1]:
        count+=1
    else:
        count=1
    if count>max:
        max=count
        ans=l[i]
print(ans)
