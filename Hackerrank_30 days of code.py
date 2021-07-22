"""
x = int(input())
y = float(input())
z = str(input())

print(int(x+y))
print(y+y)
print(f"Hackerrank {z}")
"""
"""
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

tip_percentage = meal_cost*(tip_percent/100)
tax_percentage = meal_cost*(tax_percent/100)

total_cost = meal_cost+tip_percentage+tax_percentage
print(round(total_cost))
"""
"""
n = int(input())

if n%2!=0:
    print("Weird")
elif n%2==0 and 2<=n<=5:
    print("Not Weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")
"""
"""
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if ( self.age < 13 ):
            print("You are young.")
        elif ( self.age >= 13 and self.age < 18 ):
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
"""
"""
n=int(input())
print(f"{n} x 1 = {n*1}")
print(f"{n} x 2 = {n*2}")
print(f"{n} x 3 = {n*3}")
print(f"{n} x 4 = {n*4}")
print(f"{n} x 5 = {n*5}")
print(f"{n} x 6 = {n*6}")
print(f"{n} x 7 = {n*7}")
print(f"{n} x 8 = {n*8}")
print(f"{n} x 9 = {n*9}")
print(f"{n} x 10 = {n*10}")
"""

#the below one didn't work unexpectedly   ,,,,,,,so follow the next one
#for i in range(int(input())):
#    strings = input("")
#    count=0
#    cnt=0
#    l_1 = []
#    l_2 = []
#    for string in strings:
#        ind = strings.index(string)
#        if  ind%2==0:
#            l_1.append(string)
#        else:
#            l_2.append(string)
#
#    print(f'{"".join(l_1)} {"".join(l_2)}')


"""

N = int(input())

for i in range(0, N):

    string = input()

    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end='')

    print("")


"""
"""
length_of_array=int(input())
arr_1 = input().split()
for j in arr_1[::-1]:
    print(j,end=" ")
"""
"""
x = int(input())

dictt = {}

for i in range(x):
    text = input().split()
    dictt[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in dictt:
            print(inpt+"="+dictt[inpt])
        else:
            print("Not found")
    except EOFError:
        break
"""
"""
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    rmd = []

    while n > 0:
        rm = n % 2
        n = n//2
        rmd.append(rm)

    count,result = 0,0

    for i in range(0,len(rmd)):
        if rmd[i] == 0:
            count = 0
        else:
            count +=1
            result = max(result,count)

    print(result)
"""
strings = input('')
s = strings.isnumeric()
if s == True :
    print(strings)
else:
    print("Bad String")