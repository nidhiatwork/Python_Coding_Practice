'''Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'


'''

from collections import Counter
def find_smallest_positive(nums):
    i = 0
    n=len(nums)
    while i<len(nums):
        j = nums[i]-1
        if nums[i]>0 and nums[i]<=n and nums[i]!=nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            i+=1
    for i in range(len(nums)):
        if nums[i]!=i+1:
           return i+1
    
nums = [-6, 3, 8, 2, 4]
print(find_smallest_positive(nums))
