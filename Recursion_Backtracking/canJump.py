'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
#To do

def canJump(nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

def canJump_GreedyApproach(nums):
    lastPos = len(nums) - 1
    for i in range(len(nums)-1,-1,-1):
            if (i + nums[i] >= lastPos) :
                lastPos = i
    return lastPos == 0

def canJump_Backtracking(nums):
    return canJumpFromPosition(0, nums)

def canJumpFromPosition(position, nums) :
        if (position == len(nums) - 1) :
            return True

        furthestJump = min(position + nums[position], nums.length - 1)
        for nextPosition in range(position+1,furthestJump+1):
            if (canJumpFromPosition(nextPosition, nums)) :
                return True
        return False

nums = [2,3,1,1,4]
print(canJump(nums))