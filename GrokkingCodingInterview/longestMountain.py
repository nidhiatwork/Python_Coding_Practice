'''You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
'''

from collections import Counter
def longestMountain(A):
    i = ans = 0
    while i < len(A):
        base = i
        # walk up
        while i + 1 < len(A) and A[i] < A[i+1]:
            i += 1
        
        # check if peak is valid
        if i == base: 
            i += 1
            continue
        peak = i
        
        # walk down
        while i + 1 < len(A) and A[i] > A[i+1]:
            i += 1
        
        # check if end is valid
        if i == peak: 
            i += 1
            continue
        
        # update answer
        ans = max(ans, i - base + 1)
    
    return ans

arr = [2,1,4,7,3,2,5]
print(longestMountain(arr))