'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''
import sys
def maxProduct_1(A):
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(A + B)

def maxProduct_2(nums):
    product = 1
    maxi = -sys.maxsize
    for i in range(len(nums)):
        product*=nums[i]
        maxi = max(product, maxi)
        if (nums[i] == 0): 
            product = 1

    product = 1
    for i in range(len(nums)-1,-1,-1):
        product *= nums[i]
        maxi = max(product, maxi)
        if (nums[i] == 0): 
            product = 1

    return maxi


nums = [2,3,5,0,-2,4]
print(maxProduct_2(nums))
