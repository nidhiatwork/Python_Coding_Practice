'''You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the cur_sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
'''

def maximumUniqueSubarray(nums):
    seen = set()
    ws = 0
    cur_sum, max_sum = 0,0
    for we in range(len(nums)):
        while nums[we] in seen:
            cur_sum-=nums[ws]
            seen.remove(nums[ws])
            ws+=1
        cur_sum+=nums[we]
        max_sum = max(max_sum, cur_sum)
        seen.add(nums[we])
    return max_sum

nums = [5,2,1,2,5,2,1,2,5]
print(maximumUniqueSubarray(nums))