'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2

Input: [0,1,0]
Output: 2
'''

def findMaxLength_bruteForce(nums):
    max_len = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            subarray = nums[i:j]
            c_1 = sum(subarray)
            c_0 = sum([1 for idx in range(len(subarray)) if subarray[idx]==0])
            if c_1 == c_0 and len(subarray)>max_len:
                max_len = len(subarray)
    return max_len

def findMaxLength_usingHashMap(nums):
    m = dict()
    m[0] = -1
    maxlen = 0
    count = 0
    for i in range(len(nums)):
        count = count + (1 if nums[i] == 1 else -1)
        if (count in m):
            maxlen = max(maxlen, i - m[count])
        else:
            m[count]= i
    return maxlen


nums = [1,1,0,0,1,1,1,0,0,1]
print(findMaxLength_usingHashMap(nums))