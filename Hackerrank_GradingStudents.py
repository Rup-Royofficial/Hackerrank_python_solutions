a = int(input())


for i in range(a):
    x = int(input())
    if x>=38 :
        a = 5 - (x%5)
        if a<3:
            x_1 = x+a
            print(x_1)

        if a>=3:
            print(x)    


    if x<38:
        print(x)        


#bhehenchod nije