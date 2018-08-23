def isprime(n):
	flag = 0
	for i in range(1, n+1,1):
		if (n%i==0):
			flag += 1
	if flag == 2:
		return True
	return False

def factors(n):
	f= []
	p=[]
	for i in range(1, n+1):
		if n%i==0 and isprime(i):
			p.append(i)
	print(max(p))
n = int(input())
factors(n)