'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 2, 3]
nums2 = [2]
The median is 2.0
'''
def findMedianSortedArrays(nums1, nums2):
    nums_sorted = []
    i,j = 0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            nums_sorted.append(nums1[i])
            i+=1
        else:
            nums_sorted.append(nums2[j])
            j+=1
    if i!=len(nums1):
        while i<len(nums1):
            nums_sorted.append(nums1[i])
            i+=1
    if j!=len(nums2):
        while j<len(nums2):
            nums_sorted.append(nums2[j])
            j+=1

    length = len(nums_sorted)
    if length%2:
        print("Odd numbers list: ", nums_sorted)
        return float(nums_sorted[length//2])
    else:
        print("Even numbers list: ", nums_sorted)
        return (nums_sorted[length//2 -1] + nums_sorted[length//2])/2

nums1 = [1,2,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))