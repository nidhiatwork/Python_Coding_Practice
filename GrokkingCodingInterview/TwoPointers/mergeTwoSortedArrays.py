'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

'''
def do(nums1,nums2,m,n):
    l = m+n-1
    m-=1
    n-=1
    while m>=0 and n>=0:
        if nums1[m]>nums2[n]:
            nums1[l]=nums1[m]
            m-=1
        else:
            nums1[l]=nums2[n]
            n-=1
        l-=1
    while m>=0:
        nums1[l]=nums1[m]
        m-=1
        l-=1
    while n>=0:
        nums1[l]=nums2[n]
        n-=1
        l-=1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(do(nums1, nums2, m,n))