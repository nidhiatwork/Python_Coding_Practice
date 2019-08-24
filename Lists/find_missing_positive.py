'''
Given an unsorted array with both positive and negative elements. Find the smallest positive number missing from the array in O(n) time using constant extra space. It is allowed to modify the original array.

Examples:

Input:  {2, 3, 7, 6, 8, -1, -10, 15}
Output: 1
'''
def find_missing_positive(nums):
    nums.sort()
    i=0
    while i <len(nums):
        if nums[i]>0 and nums[i]!=1:
            ans = nums[i]-1
            break
        i+=1
    return ans


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

# if all indices are marked, then
# smallest missing positive
# number is array_size + 1.
    return n + 1

arr = [ 2, 3, 7, 6, 8, -1, -10, 15 ]
arr_size = len(arr)
missing = findMissingNo(arr, arr_size)
print(missing)
# This code is contributed
# by ChitraNayal
