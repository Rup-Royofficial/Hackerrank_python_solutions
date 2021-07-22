n = int(input())
x = 0

a = list(map(int,input().split()))
b= max(a)
for i in range(len(a)):
    if a[i] == b:
        x+=1    
print(x)

#i did this