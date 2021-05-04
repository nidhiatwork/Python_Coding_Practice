'''Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First grou
'''
def reverseInGroups(arr, n, k):
    i = 0
    while(i<n): 
        left = i  
        right = min(i + k - 1, n - 1)    
        while (left < right): 
            arr[left], arr[right] = arr[right], arr[left] 
            left+= 1
            right-=1
        i+= k 
    return arr
N = 5
K = 3
arr = [1,2,3,4,5]

print(reverseInGroups(arr,len(arr),K))