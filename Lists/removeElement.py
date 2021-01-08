'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. 
It doesn't matter what you leave beyond the returned length.
'''

def removeElement(nums, val):
    n = len(nums)
    if n == 0:
        return 0
    i = 0
    while i<n:
        if nums[i]==val:
            nums[i]=nums[n-1]
            n-=1
        else:
            i+=1
    return n

A = [1,2,3,4,5,2,4]
val = 4
print(removeElement(A,val))
print(A)
