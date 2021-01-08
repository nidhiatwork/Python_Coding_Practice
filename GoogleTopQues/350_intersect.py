'''
Given two arrays, write a function to compute their intersection.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9,9]
'''

import collections
def intersect(nums1, nums2):
    counts = collections.Counter(nums1)
    res = []
    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res

nums1 = [9,4,9,8,4]
nums2 = [4,9,9]
print(intersect(nums1, nums2))
