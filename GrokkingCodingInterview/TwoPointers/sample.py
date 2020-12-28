'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
'''

def numberOfSubarrays(nums):
    slow =nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast =  nums[nums[fast]]

    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

nums = [6, 2, 4, 1, 3, 2, 5, 2]    
print(numberOfSubarrays(nums))
