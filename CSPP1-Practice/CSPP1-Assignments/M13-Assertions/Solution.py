#define the simple_divide function here
def simple_divide(item, denom):
    try:
    	value = item/denom
    	return value
    except ZeroDivisionError:
    	return 0
def fancy_divide(list_of_numbers, index):
	ans=[]
	index = list_of_numbers[index]
	for i in list_of_numbers:
		ans.append(simple_divide(i,index))
	return ans
def main():
	data = input()
	l=data.split()
	l1=[]
	for j in l:
		l1.append(float(j))
	s=input()
	index=int(s)
	print(fancy_divide(l1,index))
	

if __name__== "__main__":
	main()
