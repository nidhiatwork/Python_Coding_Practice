'''
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
'''
import math

def do(arr):
    low,high=0,len(arr)-1
    while low<len(arr)-1 and arr[low+1]>=arr[low]:
        low+=1
    if low==len(arr)-1:
        return 0
    while high>0 and arr[high]>=arr[high-1]:
        high-=1
    
    subarray_min,subarray_max = math.inf,-math.inf
    
    for i in range(low,high+1):
        subarray_min = min(subarray_min,arr[i])
        subarray_max = max(subarray_max,arr[i])
    
    while low>0 and arr[low-1]>subarray_min:
        low-=1
        
    while high<len(arr)-1 and arr[high+1]<subarray_max:
        high+=1
    
    return high-low+1
        
print(do([1, 2, 5, 3, 7, 10, 9, 12]))