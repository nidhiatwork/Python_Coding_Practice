'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''


def maxCoins(iNums):
    nums = [1] + [i for i in iNums if i > 0] + [1] 
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    for k in range(2, n):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1,right):
                print("k:{}, i:{}, left:{}, right:{}".format(k,i,left,right))
                dp[left][right] = max(dp[left][right],
                       nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

nums = [3,1,5,8] 
print(maxCoins(nums))