'''
n = int(input())
x = list(map(int,input().split()))
y = min(x)
count =0
cnt =0
n_1 = n-1
for i in x[n_1]:
    if x[i]<x[i+1]:
        count+=1
    else:
        continue
    if x[i]<y:
        cnt+=1
        
print(f"{count} {cnt}")        
'''