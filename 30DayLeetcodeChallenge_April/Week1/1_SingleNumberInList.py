
'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
from collections import Counter
def singleNumber_usingXOR(nums):

        result = 0
        for n in nums:
                result^=n
        return result
        ''' if the array was allowed to contain an arbitrary number of duplicates (ie. the same number appears 3 or 5 times), then this solution breaks down. This solution works if the duplicates always appear an even number of times (2x, 4x, 6x, etc.). And the time complexity is still O(N)
        '''

def singleNumber_usingDict(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        for k,v in c.items():
            if v==1:
                return k
        return -1

nums = [4,1,2,1,2]
print(singleNumber_usingXOR(nums))