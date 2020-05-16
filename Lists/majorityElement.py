'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

def majorityElement(nums, lo=0, hi=None):
    def majority_element_rec(lo, hi):
        
        # base case; the only element in an array of size 1 is the majority
        # element.
        if lo == hi:
            return nums[lo]

        # recurse on left and right halves of this slice.
        mid = (hi-lo)//2 + lo
        v_l = nums[lo:mid+1]
        v_r = nums[mid+1:hi+1]
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid+1, hi)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

        # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums)-1)



def majorityElement_1(nums):
    import collections
    import sys

    d = collections.Counter(nums)
    max = -sys.maxsize
    for k,v in d.items():
        if v > max:
            max = v
            key = k
    return key

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
