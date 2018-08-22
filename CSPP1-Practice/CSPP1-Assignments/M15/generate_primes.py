#define the gen_primes function here
def genPrimes(a):
    j = 2
    count = 0
    while count < a:
        f = 0
        for k in range(1, j):
            if j%k == 0:
                f += 1
        if f == 1:
            yield k
            count += 1
        j += 1

def main():
    data = input()
    l = data.split()
    a = int(l[0])
    b = int(l[1])
    primeGenerator = genPrimes(a)
    for i in range(a):
        p=primeGenerator.__next__()
        if(i%b==0):
            print (p)
if __name__== "__main__":
    main()
