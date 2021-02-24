'''
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11
'''
import sys
def findMin(arr,n,curSum,totalSum):
    if n==0:
        return abs((totalSum-curSum)-curSum)
    return min(findMin(arr,n-1,curSum,totalSum), findMin(arr,n-1,curSum+arr[n-1],totalSum))


def findMin_dp(arr):
    total = sum(arr)
    n = len(arr)
    dp = [[False for i in range(total+1)] for j in range(n+1)]
    
    for i in range(len(dp[0])):
        dp[0][i] = 0
    
    for i in range(len(dp)):
        dp[i][0] = 1
    
    for i in range(n+1):
        for j in range(total+1):
            if j<=arr[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    diff = sys.maxsize

    for j in range(total//2,-1,-1):
        if dp[n][j]==1:
            diff = total-2*j
    return diff

arr = [1,6,11,5]
curSum = 0
totalSum = sum(arr)
print(findMin(arr,(len(arr)),curSum,totalSum))