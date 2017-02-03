A = [67, 45, 2, 13, 1, 998]

B = [89, 23, 33, 45, 10, 12, 45, 45, 45]

def numSort(x):
	arr = []
	j = True
	
	while j:
		for k in x:
			if (len(arr) == 0):
				arr.append(k)
			else:
				goThruTwoSets(k, arr)
		j = False

	return arr

def goThruTwoSets(k, arr):
	i = 0
	n = len(arr)
	for m in arr:	
		if (m < k):
			i += 1
			if (i == n):
				arr.append(k)
				break
		else:
			arr.insert(i, k)
			i += 1
			break

q = numSort(A)
print(q)

s = numSort(B)
print(s)