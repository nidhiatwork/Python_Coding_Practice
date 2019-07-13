'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
Input: nums = [1,2,3,1], k = 3
Output: true
'''
def containsNearbyDuplicate(nums,k):
    dic = dict()
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False
nums = [1,2,4,9,1,1]
k = 3
print(containsNearbyDuplicate(nums,k))