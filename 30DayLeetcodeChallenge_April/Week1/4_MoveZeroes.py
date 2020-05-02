'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


def moveZeroes(nums):
    n = len(nums)
    i=0
    while i<n:
        if nums[i]==0:
            pos = i+1
            while pos<n:
                if nums[pos]!=0:
                    nums[pos],nums[i]=nums[i], nums[pos]
                    break
                pos+=1
        i+=1
    return nums

def moveZeroes_2(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums
nums = [0,1,0,3,12]
print(moveZeroes_2(nums))