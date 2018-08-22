#define the gen_primes function here
def genPrimes():
    pass

def main():
	data=input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.next()
	    if(i%b==0):
	        print p
	
if __name__== "__main__":
	main()
