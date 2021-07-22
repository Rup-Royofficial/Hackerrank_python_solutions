a, b, c, d = map(int, input().split(' '))
if a-c==0:
    print("YES")
    quit()
if d-b==0:
    print("NO")
    quit()
if ((a-c)%(d-b)==0 and (a-c)//(d-b)>=0):
    print("YES")
    quit()
print("NO")    