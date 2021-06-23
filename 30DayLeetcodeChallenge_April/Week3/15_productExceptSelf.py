'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
You cannot use division.

Input:  [1,2,3,4]
Output: [24,12,8,6]
'''
def productExceptSelf(nums):
    p=1
    A=[]
    for i in range(len(nums)):
        A.append(p)
        p=p*nums[i]
    p=1
    B=[]
    n=len(nums)-1
    for i in range(len(nums)):
        B.append(p)
        p=p*nums[n-i]
    B.reverse()
    for i in range(len(nums)):
        nums[i]=A[i]*B[i]
    return nums

def productExceptSelf_constantSpace(nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
class Solution:
    def productExceptSelf(self, nums):
        ans = [1 for _ in nums]
        
        left = 1
        right = 1
        
        for i in range(len(nums)):
            ans[i] *= left  
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        
        return ans
nums = [1,2,3,4,5]
print(productExceptSelf(nums))