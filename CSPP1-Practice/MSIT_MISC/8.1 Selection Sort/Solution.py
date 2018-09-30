def selection_sort(array):
	b = []
	st = "["
	for i in range(0, len(array)):
		temp = min(array)
		ind = array.index(temp)
		b.append(temp)
		del array[ind]
	for i in range(0,len(b)):
		st = st + b[i] + ", "
	res = st[:-2] + "]"
	return res
def main():
	n = int(input())
	for i in range(n):
		a = input().split(" ")
		result = selection_sort(a)
		print(result)
if __name__ == "__main__":
	main()