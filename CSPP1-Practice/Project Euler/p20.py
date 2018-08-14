def factorial(n):
     if(n <= 1):
        return 1
     else:
        return(n*factorial(n-1))
def sum_dig(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    t = factorial(n)
    print(sum_dig(t))