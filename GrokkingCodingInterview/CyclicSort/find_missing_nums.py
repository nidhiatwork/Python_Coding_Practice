'''We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
'''

from collections import Counter
def find_missing_nums(nums):
    i = 0
    while i<len(nums):
        j = nums[i]-1
        if nums[i]!=nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            i+=1
    missing_nums = []
    for i in range(len(nums)):
        if nums[i]!=i+1:
            missing_nums.append(i+1)

    return missing_nums
nums = [2, 3, 1, 8, 2, 3, 5, 1]
print(find_missing_nums(nums))
