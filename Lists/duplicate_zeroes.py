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
def duplicateZeros_1(arr):
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n-1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0: 
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0

arr = [1,0,2,4,0,4,5,9]
duplicateZeros_1(arr)
print(arr)