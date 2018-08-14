#!/bin/python3
def sum_dig(n):
    n = 2 ** n
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_dig(n))