'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Input: nums = [-3,2,-3,4,2]
Output: 5
'''

def minStartValue_1(nums):
    num = 1
    sum = num
    for i in range(len(nums)):
        if nums[i]+sum<1:
            diff = 1-(nums[i]+sum)
            num = num+diff
            sum = sum+nums[i]+diff
        else:
            sum+=nums[i]
    return num

def minStartValue_2(nums):
        prefix_sum = 0
        min_start_value = 1
        
        for num in nums:
            prefix_sum += num
            min_start_value = max(min_start_value, 1 - prefix_sum)
        
        return min_start_value

nums = [-3,2,-3,4,2]
print(minStartValue_2(nums))