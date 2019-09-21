'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Input:  [1,2,3,4]
Output: [24,12,8,6]
'''
def productExceptSelf_TimeExceeded(nums):
    ans=[]
    for i in range(len(nums)):
        prod = 1
        j,k=i-1,i+1
        while j>=0:
            prod *= nums[j]
            j-=1
        while k<len(nums):
            prod *= nums[k]
            k+=1
        ans.append(prod)
    return ans

def productExceptSelf_LeftRightLogic(nums):
    n = len(nums)
    L,R,ans=[0]*n,[0]*n,[0]*n
    L[0]=1
    for i in range(1,n):
        L[i]=nums[i-1]*L[i-1]
    R[n-1]=1
    for i in range(n-2,-1,-1):
        R[i]=nums[i+1]*R[i+1]
    for i in range(n):
        ans[i]=L[i]*R[i]
    return ans

nums = [1,2,3,4]
print(productExceptSelf_LeftRightLogic(nums))