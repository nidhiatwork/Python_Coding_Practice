'''Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

'''

from collections import Counter
def find_smallest_positive(nums,k):
    i = 0
    n=len(nums)
    while i<len(nums):
        j = nums[i]-1
        if nums[i]>0 and nums[i]<=n and nums[i]!=nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            i+=1

    missing_nums = []
    extraNums = set()
    for i in range(len(nums)):
        if len(missing_nums)<k:
            if nums[i]!=i+1:
                missing_nums.append(i+1)
                extraNums.add(nums[i])
    i=1
    while len(missing_nums)<k:
        candidate = i+n
        if candidate not in extraNums:
            missing_nums.append(candidate)
        i+=1
    return missing_nums
nums = [3,-1,4,5,5]
print(find_smallest_positive(nums, 3))
