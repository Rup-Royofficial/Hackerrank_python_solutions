n,k = map(int,input().split())
x = list(map(int,input().split()))
y = int(input())

if k!=0:
    x.pop(k)
    x_1 = int(sum(x)/2)
    if y>x_1:
        print(y-x_1)
    else:
        print("Bon Appetit")