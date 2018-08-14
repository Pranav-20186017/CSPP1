#https://www.hackerrank.com/contests/projecteuler/challenges/euler001
#!/bin/python3
def sum_3_5(n):
    sum_temp =0
    for i in range(1, n):
        if i % 3 ==0 or i%5==0:
            sum_temp += i
    return sum_temp
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = sum_3_5(n)
    print(ans)