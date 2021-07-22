n = int(input())
count = 0

for i in range(n):
    while count!=n:
        if count==0 :
            print("     #")
        if count==1 :
            print("    ##")
        if count==2 :
            print("   ###")
        if count==3 :
            print("  ####")
        if count==4 :
            print(" #####")
        if count==5 :
            print("######")  
        count+=1      
#the bottom one is the real one
n = int(input())
for i in range(n):
    print(' '*(n-i-1), end="")
    print('#'*(i+1))