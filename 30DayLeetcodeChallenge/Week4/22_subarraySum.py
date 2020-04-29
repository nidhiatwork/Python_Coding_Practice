'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''

def subarraySum_usingDict(nums, k):
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums-k,0)
        d[sums] = d.get(sums,0) + 1
    
    return(count)



def subarraySum_1(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            s=sum([nums[k] for k in range(i,j+1)])
            if s==k:
                count+=1
    return count

def subarraySum_2(nums,k):
    count = 0
    s=list()
    s.append(0)
    for i in range(len(nums)):
        s.append(s[-1] + nums[i])
    
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[j]-s[i]==k:
                count+=1
    return count

def subarraySum_3(nums,k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum==k:
                count+=1
    return count



nums,k = [1,2,1,3,5,2,3],7
print(subarraySum_usingDict(nums,k))