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

def search(nums, target):
    low,high = 0,len(nums)-1
    while low<=high:
        mid = low + (high-low)//2
        if nums[mid]==target:
            return mid
        if nums[low]<=target<nums[mid] or target<nums[mid]<nums[low] or nums[mid]<nums[low]<target:
            high = mid-1
        else:
            low = mid+1
    return -1

nums = [5,1,3]
target = 5
print(search(nums, target))