'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''

def searchInRotatedArray(nums, target):
    lo,hi = 0,len(nums)-1
    while lo <=hi:
        mid = (lo +hi)//2
        if (nums[mid] == target): 
            return mid
        if nums[lo]<=target<nums[mid] or target<nums[mid]<nums[lo] or nums[mid]<nums[lo]<=target:
               hi = mid - 1
        else:
               lo = mid + 1
    
    return -1


nums = [3,4,5,1,2]
target = 1
print(searchInRotatedArray(nums, target))

#Hints:
'''
for array [1,2,3,4,5], write all possible values

[5,1,2,3,4]
[4,5,1,2,3]
[3,4,5,1,2]
[2,3,4,5,1]
notice that if you want to stay in range lo - mid, there are three possibilities only:
if nums[lo]<=target<nums[mid] 
or 
target<nums[mid]<nums[lo] 
or 
nums[mid]<nums[lo]<=target:
otherwise, go to next half i.e. mid to hi
'''