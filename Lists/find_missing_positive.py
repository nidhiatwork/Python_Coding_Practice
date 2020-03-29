'''
Given an unsorted array with both positive and negative elements. Find the smallest positive number missing from the array in O(n) time using constant extra space. It is allowed to modify the original array.

Examples:

Input:  {2, 3, 7, 6, 8, -1, -10, 15}
Output: 1
'''
#O(NLogN)
def find_missing_positive(nums):
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res += 1
    return res


def findMissingNo(arr, n):
    for i in range(n):
        if (arr[i] <= 0 or arr[i] > n):
            continue
        val = arr[i]
    while arr[val-1]!=val:
        nextval = arr[val-1]
        arr[val-1] = val
        val = nextval
        if (val <= 0 or val > n):
            break
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
def find_missing_positive_2(nums):
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        n_idx = nums[i]%n
        nums[n_idx]=nums[n_idx]+n
    for i in range(1,len(nums)):
        if nums[i]//n==0:
            return i
    return n
    
# if all indices are marked, then
# smallest missing positive
# number is array_size + 1.
    return n + 1

arr = [ 1,2,0 ]
arr_size = len(arr)
missing = findMissingNo(arr, arr_size)
print(missing)
# This code is contributed
# by ChitraNayal
