'''
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
'''
def combinationSum(candidates, target):
    ans = []
    find_combs(candidates, target, [], ans)
    return ans

def find_combs(nums, target, path, ans):
    if target<0:
        return
    elif target==0:
        ans.append(path)
        return
    for i in range(len(nums)):
        find_combs(nums[i:], target-nums[i], path+[nums[i]], ans)
        
print(combinationSum([2,3,5],8))