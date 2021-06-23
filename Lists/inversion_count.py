def mergeSort(arr, ct=0):
	if len(arr)==1:
		return ct
	if len(arr) >1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		ct1= mergeSort(L, ct)
		ct2= mergeSort(R, ct)
		ct = ct1 + ct2
		return merge(L, R, arr, ct)

def merge(L, R, arr, ct):
	mid = len(L)
	i = j = k = 0
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i+=1
		else:
			ct += mid-i
			arr[k] = R[j]
			j+=1
		k+=1
	while i < len(L):
		arr[k] = L[i]
		i+=1
		k+=1
	while j < len(R):
		arr[k] = R[j]
		j+=1
		k+=1
	return ct

print(mergeSort([1, 20, 6, 4, 5])==5)
# print(mergeSort([3, 1, 2])==2)
# print(mergeSort([8,4,2,1])==6)
