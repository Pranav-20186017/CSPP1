def main():
	n = input()
	l = []
	for i in range(int(n)):
		l.append(input())
	adict = {}
	for i in l:
		l2 = i.split(":")
		print(l2[1])		
		if l2[0] in adict:
			l2[1] = l2[1].split(',')
			for j in l2[1]:
				adict[l2[0]].append(int(j))
		else:
			l2[1] = l2[1].split(',')
			adict[l2[0]] = l2[1]
		for k in range(len(l2[1])):
			adict[l2[0]][k] = int(adict[l2[0]][k])

		
	print(adict)

if __name__ == "__main__":
	main()