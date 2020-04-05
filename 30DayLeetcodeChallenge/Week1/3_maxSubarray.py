'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.'''

class Solution(object):
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        sum = nums[0]
        for i in range(1,len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            maximum = max(maximum, sum)
        return maximum
        

a = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(a))
