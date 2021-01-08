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
def subsets(nums):
    all_subsets = [[]]
    if not nums:
        return all_subsets
    for num in nums:
        for idx in range(len(all_subsets)):
            all_subsets.append(all_subsets[idx]+[num])
    return all_subsets
    
nums = [1,2,3]
print(subsets(nums))