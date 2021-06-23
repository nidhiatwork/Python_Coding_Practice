class Solution:
    def permuteUnique(self, nums):
        ans = []
        sub = []
        options = set(nums)
        self.permuteUnique_helper(nums, ans, sub, options)
        return ans
    
    def permuteUnique_helper(self, nums, ans, sub, options):
        if len(sub)==len(nums):
            ans.append(list(sub))
            return
        for num in nums:
            if num in options:
                sub.append(num)
                options.remove(num)
                self.permuteUnique_helper(nums, ans, sub, options)
                sub.pop()
                options.add(num)

s = Solution()
print(s.permuteUnique([1,2,3]))