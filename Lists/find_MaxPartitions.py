'''
In a given array, find the maximum number of partitions you have to make so that
all partitions when sorted and put together give the array in sorted format
[3,4,1,5, 6, 4, 7]
output: 3
Break as [3,4,1],[6,4],[7]
'''
# 2 1 0 3 1 6 4 7 5 6 
import sys
def find_MaxPartitions(arr):
	dec_arr = []
	sub = []
	range_arr = []
	l,h = arr[0],arr[0]
	for i in range(len(arr)):
		if not sub or h>=arr[i]:
			sub.append(arr[i]) 
		else:
			dec_arr.append(sub)   
			range_arr.append([l,h]) 
			sub=[arr[i]]					
			l,h = arr[i],arr[i]		
		l = min(l, arr[i]) 
		h = max(h, arr[i]) 
	dec_arr.append(sub)
	range_arr.append([l,h])
	range_arr.sort()
	merged = []
	for interval in range_arr:
		if not merged or merged[-1][1]<=interval[0]:
			merged.append(interval)
		else:
			merged[-1][1] = max(merged[-1][1], interval[1])
	return len(merged)

arr = [3,4,1,5, 6, 4, 7]
print(find_MaxPartitions(arr))