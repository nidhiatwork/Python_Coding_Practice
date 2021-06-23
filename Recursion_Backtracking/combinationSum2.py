class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()
        sub = []
        idx = 0
        self.combinationSum2_helper(candidates, target, sub, ans, idx)
        return list(ans)
    
    def combinationSum2_helper(self, candidates, target, sub, ans, idx):
        if target==0:
            ans.append(sub[:])
            return
        for i in range(idx, len(candidates)):
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            sub.append(candidates[i])
            if target<candidates[i]:
                sub.pop()
                break
            self.combinationSum2_helper(candidates, target-candidates[i], sub, ans, i+1)
            sub.pop()

candidates = [10,1,2,7,6,1,2,5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))