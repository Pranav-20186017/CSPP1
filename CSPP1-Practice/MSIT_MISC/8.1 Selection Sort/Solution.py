def selection_sort(array):
	b = []
	for i in range(0, len(array)):
		temp = min(array)
		ind = array.index(temp)
		b.append(temp)
		del array[ind]
	return b
def main():
	n = int(input())
	for i in range(n):
		a = input().split(" ")
		result = selection_sort(a)
		print(result)
if __name__ == "__main__":
	main()