# Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

# Examples : 

#   Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
#   Output: 6  (j = 7, i = 1)
import collections
def FindMaxIdxDiff(arr):
    n = len(arr)
    result = 0
    maxFromEnd = collections.deque()
    val = -float("inf")
    for num in reversed(arr):
        val = max(num, val)
        maxFromEnd.appendleft(val)

    for i in range(0, n):
        low = i + 1
        high = n - 1
        ans = i
 
        while (low <= high):
            mid = int((low + high) / 2)
 
            if (arr[i] <= maxFromEnd[mid]):
               
                # We store this as current
                # answer and look for further
                # larger number to the right side
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1       
 
        # Keeping a track of the
        # maximum difference in indices
        result = max(result, ans - i)
     
    print(result)

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
FindMaxIdxDiff(arr)