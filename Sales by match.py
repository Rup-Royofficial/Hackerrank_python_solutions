n=int(input())
l=[int(x) for x in input().split()]
q=[0 for x in range(101)]
for i in l:
    q[i]+=1
ans=0
for i in q:
    if i>1:
        ans+=int(i/2)
print(ans)