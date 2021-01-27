'''We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4

'''

from collections import Counter
def find_dup_num(nums):
    i = 0
    while i<len(nums):
        if nums[i]!=i+1:    
            j = nums[i]-1
            if nums[i]!=nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                return nums[i]
        else:
            i+=1
            
    
nums = [1, 4, 4, 3, 2]
print(find_dup_num(nums))
