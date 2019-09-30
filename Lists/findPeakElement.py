'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
'''
def findPeakElement_brute_force(nums):
    if len(nums)==1:
        return 0
    if  len(nums)==2:
        return 0 if nums[0]>nums[1] else 1
    for i in range(1, len(nums)-1):
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            return i
    if nums[0]>nums[1]:
        return 0
    if nums[-1]>nums[-2]:
        return len(nums-1)

def findPeakElement_binarySearch(nums):
    if len(nums) <= 1: return 0
    mid = 0
    l = 0
    h = len(nums) - 1
    while (l < h):
        mid = (l + h)//2
        if (nums[mid] > nums[mid + 1]):
            h = mid
        elif (nums[mid] < nums[mid + 1]):
            l = mid + 1
    return l


nums = [6,5,4,3,2,3]
print(findPeakElement_binarySearch(nums))