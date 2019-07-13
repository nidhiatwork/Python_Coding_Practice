'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. 

It doesn't matter what you leave beyond the returned length.
'''

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
        
    return i + 1

A = [1,1,2,2,3,3]
print(removeDuplicates(A))
print(A)
