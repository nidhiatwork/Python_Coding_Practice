"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
def get_sum(nums):
        if len(nums)<3:
                return []
        ans=[]
        n = len(nums)
        for i in range(n-1):
                comps = set()
                for j in range(i+1,n):
                        comp = -(nums[i]+nums[j])
                        comps.add(comp)
                        if nums[j] in comps:
                                if sorted([nums[i],nums[j],comp]) not in ans:
                                        ans.append(sorted([nums[i],nums[j],comp]))
        return ans

arr = [2,-1,0,1,-1,0]
print(get_sum(arr))