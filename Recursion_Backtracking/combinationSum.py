class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        sub = []
        idx,end = 0,len(candidates)
        candidates.sort()
        self.combinationSum_helper(candidates, target, sub, ans, idx)
        return ans
    
    def combinationSum_helper(self, candidates, target, sub, ans, start):
        if target==0:
            ans.append(sub[:])
            return
        for i in range(start, len(candidates)):
            sub.append(candidates[i])
            if target<candidates[i]:
                sub.pop()
                break
            self.combinationSum_helper(candidates, target-candidates[i], sub, ans, i)
            sub.pop()

candidates = [2,3,6,7]
target = 7
s = Solution()
print(s.combinationSum(candidates, target))