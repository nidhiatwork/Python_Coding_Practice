'''We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]

'''

from collections import Counter
def find_dup_num(nums):
    i = 0
    while i<len(nums):
        j = nums[i]-1
        if nums[i]!=nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            i+=1
    dup_nums = []
    for i in range(len(nums)):
        if nums[i]!=i+1:
            dup_nums.append(nums[i])        
    return dup_nums
nums = [1, 4, 4, 3, 2]
print(find_dup_num(nums))
