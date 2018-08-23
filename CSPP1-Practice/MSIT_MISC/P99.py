n = int(input())
j = []
for i in range(0,n):
	t = (input())
	t.split("\n")
	j.append(t)
dicta ={}
for i in j:
	l = i.split(" ")
	dicta[l[0]] = (l[1])
print(dicta)
d_k = list(dicta.keys())
d_v = list(dicta.values())
for i in d_k:
	i = int(i)
for i in d_v:
	i = int(i)
print(d_k)
print(d_v)