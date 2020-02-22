'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [9,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):
    if not nums:
        return 0
    maximum = nums[0]
    sum = nums[0]
    for i in range(1,len(nums)):
        if sum < 0:
            sum = nums[i]
        else:
            sum += nums[i]
        maximum = max(maximum, sum)
    return maximum

# nums = [9,1,-3,4,-1,12,1,-5,4]
nums = [5,7,2,-1,6]
print(maxSubArray(nums))