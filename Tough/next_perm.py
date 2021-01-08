"""
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""
def nextPermutation(nums):
    n= len(nums)
    i=n-2
    while(i>0) and nums[i]>=nums[i+1]:
        i-=1
    if (i >= 0):
            j = n- 1
            while j >= 0 and nums[j] <= nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
    
    last = nums[i+1:]
    nums = nums[:i+1]
    last.reverse()
    for i in last:
        nums.append(i)
    print(nums)
nextPermutation([1,3,2])