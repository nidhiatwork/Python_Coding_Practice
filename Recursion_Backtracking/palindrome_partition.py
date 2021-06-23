class Solution:
    def partition(self, s):
        ans = []
        sub = []
        self.partition_helper(s, ans, sub)
        return ans
    
    def partition_helper(self, s, ans, sub, idx=0):
        if idx==len(s):
            ans.append(sub[:])
            return
        for i in range(idx,len(s)):
            cur=s[idx:i+1]
            if cur==cur[::-1]:
                sub.append(cur)
                self.partition_helper(s, ans, sub, i+1)
                sub.pop()

sol = Solution()
s = "aab"
print(sol.partition(s))
