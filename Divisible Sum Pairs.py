#!/bin/python3

import sys

count = 0
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j])%k == 0:
            count += 1
print(count)