'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''
import collections

def missingNumber_1(nums):
    actual_sum = sum(nums)
    expected_sum = (len(nums)+1)*len(nums)//2
    return expected_sum-actual_sum   

def missingNumber_2(nums):
    if not nums:
        return -1
    nums.sort()
    if nums[0]!=0:
        return 0
    if nums[-1]!=len(nums):
        return len(nums)
    for i in range(1,len(nums)):
        if nums[i] - nums[i-1]!=1:
            return nums[i]-1

    

nums= [9,6,4,2,3,5,7,0,1]
print(missingNumber_2(nums))