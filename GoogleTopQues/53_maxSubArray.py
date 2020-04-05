'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,-1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray_1(nums):
    
    maximum = nums[0]
    sum = nums[0]
    for i in range(1,len(nums)):
        if sum < 0:
            sum = nums[i]
        else:
            sum += nums[i]
        maximum = max(maximum, sum)
    return maximum

def maxSubArray_2(nums):
    for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
    return max(nums)
    
nums = [-2,-1,-3,4,-1,2,1,-5,4]
print(maxSubArray_2(nums))