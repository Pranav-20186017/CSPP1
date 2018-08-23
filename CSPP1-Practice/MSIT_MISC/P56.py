def sum_dig(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot
def powr(n):
    return sum_dig((n-1)**(n-1))
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(powr(n))