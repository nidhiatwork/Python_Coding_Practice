

'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''
import collections

#this one ignores duplicates
def intersection_i(nums1, nums2):
    return list(set(nums1) & set(nums2))

#this one does not ignore duplicates

def intersection_ii(nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())


def intersection_iii(nums1,nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    pt1 = pt2 = 0
    res = []

    while True:
        try:
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                res.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
        except IndexError:
            break

    return res

def intersection_iv(nums1, nums2):
        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res


nums1 = [3,1,2]
nums2 = [4,1]
print(intersection_i(nums1,nums2))
print(intersection_ii(nums1,nums2))
print(intersection_iii(nums1,nums2))
print(intersection_iv(nums1,nums2))