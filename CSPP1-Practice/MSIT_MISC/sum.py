def count_factors(n,val):
	count = 0
	for i in range(1,n):
		if i % val == 0:
			count += 1
	return count
tf = count_factors(100000000,3)
ff = count_factors(100000000,5)
fif = count_factors(100000000,15)
ts = 3*((tf*(tf+1))//2)
fs = 5*((ff*(ff+1))//2)
fifs = 15*((fif*(fif+1))//2)
ans = (ts + fs) - fifs
print(ans)