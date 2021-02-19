'''
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is the same. 

Examples: 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}
'''

def isSubsetSum(arr, n, target):
    if target==0:
        return True
    if n==0:
        return False
    if arr[n-1]>target:
        return isSubsetSum(arr,n-1,target)
    return isSubsetSum(arr,n-1,target) or isSubsetSum(arr,n-1,target-arr[n-1])

def isSubsetSum_dp(arr, n):
    sum = 0
    i, j = 0, 0
 
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return False
 
    dp = [[False for i in range(sum // 2 + 1)]
            for j in range(n+1)]

    for i in range(n + 1):
        dp[i][0] = True
 
    for i in range(1, n+1):
        for j in range(1, sum // 2 + 1):
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][sum // 2]

arr = [3,3,3,4,5]
n = len(arr)
print(isSubsetSum_dp(arr, n))