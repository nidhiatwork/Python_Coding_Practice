import collections 
import heapq

def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    i=0
    while i<n:
        if arr[i] == 0:
            arr.insert(i+1,0)
            arr.pop()
            i+=1
        i+=1

arr = [1,0,2,4,0,4,5,9]
duplicateZeros(arr)
print(arr)