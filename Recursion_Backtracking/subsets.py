'''
Given a set of distinct integers, nums, return all possible subsets (the power set). No duplicates.
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    def subsets(self, nums):
        ans = []
        sub = []
        self.subsets_helper(nums, sub, ans)
        return ans
    
    def subsets_helper(self, nums, sub, ans, idx=0):
        ans.append(list(sub))
        for i in range(idx, len(nums)):
            sub.append(nums[i])
            self.subsets_helper(nums, sub, ans, i+1)
            sub.pop()

nums = [1,2,3]
s=Solution()
print(s.subsets(nums))