'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
You cannot use division.

Input:  [1,2,3,4]
Output: [24,12,8,6]
'''
def productExceptSelf(nums):
    A = [None]*len(nums)
    A[0]=1
    for i in range(1,len(nums)):
        A[i]=nums[i-1]*A[i-1]
    B = [None]*len(nums)
    B[-1]=1
    for i in range(len(nums)-2,-1,-1):
        B[i]=nums[i+1]*B[i+1]
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
nums = [1,2,3,4]
print(productExceptSelf_constantSpace(nums))