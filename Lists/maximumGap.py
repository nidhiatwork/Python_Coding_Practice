'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
'''
import math
def maximumGap(arr):
    if len(arr) < 2 or min(arr) == max(arr):
        return 0
    a, b = min(arr), max(arr)
    delta = math.ceil((b-a)/(len(arr)-1))
    bucket = [[None, None] for _ in range((b-a)//delta+1)]
    for n in arr:
        b = bucket[(n-a)//delta]
        b[0] = n if b[0] is None else min(b[0], n)
        b[1] = n if b[1] is None else max(b[1], n)
    bucket = [b for b in bucket if b[0] is not None]
    return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))

# Driver Code
if __name__ == "__main__":

	arr = [3,6,2,10,8,1,3]
	n = len(arr)
	INT_MIN, INT_MAX = float('-inf'), float('inf')
	
	print(maximumGap(arr))

# This code is contributed by Rituraj Jain
