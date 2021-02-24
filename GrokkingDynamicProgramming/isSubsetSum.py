'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.
'''

def isSubsetSum(arr, n, target):
    if target==0:
        return True
    if n==0:
        return False
    if arr[n-1]>target:
        return isSubsetSum(arr,n-1,target)
    return isSubsetSum(arr,n-1,target) or isSubsetSum(arr,n-1,target-arr[n-1])

def isSubsetSum_dp(arr, n, sum):
    dp = [[False for i in range(sum+1)]
            for j in range(n+1)]

    for i in range(n + 1):
        dp[i][0] = True
 
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][sum]

arr = [3, 34, 4, 12, 5, 2]
n = len(arr)
print(isSubsetSum_dp(arr, n, 9))