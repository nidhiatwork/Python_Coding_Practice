class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        sub = []
        self.subsetsWithDup_helper(nums, sub, ans)
        return ans
    
    def subsetsWithDup_helper(self, nums, sub, ans, idx=0):
        ans.append(sub[:])
        for i in range(idx, len(nums)):
            if i>idx and nums[i]==nums[i-1]:
                continue
            sub.append(nums[i])
            self.subsetsWithDup_helper(nums, sub, ans, i+1)
            sub.pop()

s = Solution()
nums = [1,1,2,3]
print(s.subsetsWithDup(nums))