'''Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

from collections import Counter
import math
def minSubArrayLen(s, nums):
    ws=0
    sum=0
    ans = math.inf
    for we in range(len(nums)):
        sum+=nums[we]
        while sum>=s:
            ans = min(ans, we-ws+1)
            sum-=nums[ws]
            ws+=1
    return 0 if ans==math.inf else ans

s = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(s, nums))