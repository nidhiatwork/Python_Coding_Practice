'''
Break Arr into  𝑛5  (actually it is  ⌈𝑛5⌉ ) groups, namely  𝐺1,𝐺2,𝐺3...𝐺𝑛5 
For each group  𝐺𝑖,∀1≤𝑖≤𝑛5 , do the following:
Sort the group  𝐺𝑖 
Find the middle position i.e., median  𝑚𝑖  of group  𝐺𝑖 
Add  𝑚𝑖  to the set of medians  𝑆 
The set of medians  𝑆  will become as  𝑆={𝑚1,𝑚2,𝑚3...𝑚𝑛5} . The "good" pivot element will be the median of the set  𝑆 . We can find it as  𝑝𝑖𝑣𝑜𝑡=𝑓𝑎𝑠𝑡𝑆𝑒𝑙𝑒𝑐𝑡(𝑆,𝑛10) .
Partition the original Arr into three sub-arrays - Arr_Less_P, Arr_Equal_P, and Arr_More_P having elements less than pivot, equal to pivot, and bigger than pivot respectively.
Recurse based on the sizes of the three sub-arrays, we will either recursively search in the small set, or the big set, as defined in the following conditions:

If k <= length(Arr_Less_P), then return fastSelect(Arr_Less_P, k). This means that if the size of the "small" sub-array is at least as large as k, then we know that our desired  𝑘𝑡ℎ  smallest element lies in this sub-array. Therefore recursively call the same function on the "small" sub-array.


If k > (length(Arr_Less_P) + length(Arr_Equal_P)), then return fastSelect(Arr_More_P, (k - length(Arr_Less_P) - length(Arr_Equal_P))). This means that if k is more than the size of "small" and "equal" sub-arrays, then our desired  𝑘𝑡ℎ  smallest element lies in "bigger" sub-array.


Return pivot otherwise. This means that if the above two cases do not hold true, then we know that  𝑘𝑡ℎ  smallest element lies in the "equal" sub-array.
'''
def fastSelect(arr, k):
	if k==0:
		return arr[0]
	subs = []
	for j in range(0,len(arr),5):
		subs.append(arr[j:j+5])
	S = []
	for sub in subs:
		sub.sort()
		S.append(sub[len(sub)//2])
	pivot = fastSelect(S, len(S)//2)
	Arr_Less_P =  [item for item in arr if item<pivot]
	Arr_Equal_P = [item for item in arr if item==pivot]
	Arr_More_P =  [item for item in arr if item>pivot]
	if k<=len(Arr_Less_P):
		return fastSelect(Arr_Less_P, k)
	elif k>len(Arr_Less_P)+len(Arr_Equal_P):
		return fastSelect(Arr_More_P, k-len(Arr_Less_P)-len(Arr_Equal_P))
	return pivot

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12