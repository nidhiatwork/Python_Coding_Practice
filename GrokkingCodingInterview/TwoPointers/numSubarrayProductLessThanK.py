'''Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
'''

from collections import Counter
def numSubarrayProductLessThanK(nums, k):
    if k<=1:
        return 0
    ws = 0
    counter = 0
    product = 1
    for we in range(len(nums)):
        product*=nums[we]
        while product>=k:
            product/=nums[ws]
            ws+=1
        print(we-ws+1)
        counter+=we-ws+1
    return counter
                
nums = [100,102,2,3,1,5,3,1,105]
k = 100
print(numSubarrayProductLessThanK(nums, k))