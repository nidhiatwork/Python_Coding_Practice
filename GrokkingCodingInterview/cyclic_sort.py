'''Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
'''

from collections import Counter
def cyclic_sort(nums):
    i = 0
    while i<len(nums):
        j = nums[i]-1
        if nums[i]!=nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            i+=1
    return nums
nums = [3, 1, 5, 4, 2]
print(cyclic_sort(nums))
