'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''

def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    ans = set()
    for item in nums1:
        if item in nums2:
            ans.add(item)
    return ans

print(intersection([4,9,5], [9,4,9,8,4]))