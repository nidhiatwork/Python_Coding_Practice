'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Input: nums = [8,2,4,7], limit = 4
Output: 2 
'''
import collections
def longestSubarray(nums, limit):
    maxLen, ws = 0, 0
    minQueue, maxQueue = collections.deque([]), collections.deque([])
    for we in range(len(nums)):
        while minQueue and minQueue[-1] > nums[we]:
            minQueue.pop()
        minQueue.append(nums[we])
        while maxQueue and maxQueue[-1] < nums[we]:
            maxQueue.pop()
        maxQueue.append(nums[we])
        
        if maxQueue[0] - minQueue[0] <= limit:
            maxLen = max(maxLen, we-ws+1)
        else:
            if maxQueue[0] == nums[ws]:
                maxQueue.popleft()
            if minQueue[0] == nums[ws]:
                minQueue.popleft()
            ws += 1
    return maxLen

print(longestSubarray([8,6,3,2,4,7],4))