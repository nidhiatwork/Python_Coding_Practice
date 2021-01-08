'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
'''
def lengthOfLIS(nums):
    if not nums: 
        return 0
    maxans = 1
    dp = dict()
    dp[0]=1
    for i in range(1,len(nums)):
        maxval = 0
        for j in range(i):
            if nums[i] > nums[j]:
                maxval = max(maxval,dp[j])
        dp[i]= maxval+1
        maxans = max(maxans, dp[i])
    return maxans

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))