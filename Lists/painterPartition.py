'''Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board.
NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. Which means a configuration where painter 1 paints board 1 and 3 but not 2 is invalid.
'''
def findPaintingTime(arr, A, B):
    high = sum(arr)
    low = max(arr)
    minTime = minTime_helper(arr, A, low, high)
    return B * minTime

def minTime_helper(arr, A, low, high):
    while low <= high:
        mid = (low + high)//2
        if timePossible(arr, A, mid):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

#[1, 8, 5, 11] A = 2
# loops: 1 
def timePossible(arr, A, t):
    val = t
    i = 0
    for i in range(len(arr)):
        if val-arr[i]<0:
            A-=1
            val = t-arr[i]
            if A==0:
                return False
        else:
            val-=arr[i]
    return True

A = 2
B = 1
arr = [1, 8, 11, 3, 5]
print(findPaintingTime(arr, A, B))