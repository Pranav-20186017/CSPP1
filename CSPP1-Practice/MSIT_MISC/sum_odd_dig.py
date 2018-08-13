def sum_digits( n , sum):
	temp = 0
	temp_num = n
	while(n!=0):
		rem = n % 10
		temp += rem
		n = n // 10
	if temp == sum:
		return temp_num
	else:
		return 0
l = []
for i in range(101,1000,2):
	t = sum_digits(i, 12)
	l.append(t)
for i in l:
	if i==0:
		l.remove(i)
print(l)