# nums1 = [1,3,8,9,15]
# nums2 = [7,11,18,19,21,25]
def findMedianSortedArrays1(nums1, nums2):
    C = []
    i,j=0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i]<nums2[j]:
            C.append(nums1[i])
            i+=1
        else:
            C.append(nums2[j])
            j+=1
    C.extend(nums1[i:] or nums2[j:])
    if not C:
        return None
    if len(C)%2:
        return C[len(C)//2]
    return (C[(len(C)//2)-1]+C[len(C)//2])/2

def findMedianSortedArrays2(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    if n == 0:
        raise ValueError

    start, end = 0, m
    while start <= end:
        Px = (start + end) // 2
        Py = ((m + n + 1) // 2) - Px
        print(Px,Py)
        if Px < m and nums2[Py-1] > nums1[Px]:
            print(nums2[Py-1],"> ", nums1[Px])
            print("Px is too small, must increase it")
            start = Px + 1
        elif Px > 0 and nums1[Px-1] > nums2[Py]:
            print(nums1[Px-1],"> ", nums2[Py])
            print("Px is too big, must decrease it")
            end = Px - 1
        else:
            # Px is perfect
            if Px == 0: 
                max_of_left = nums2[Py-1]
            elif Py == 0: 
                max_of_left = nums1[Px-1]
            else: 
                max_of_left = max(nums1[Px-1], nums2[Py-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if Px == m: 
                min_of_right = nums2[Py]
            elif Py == n: 
                min_of_right = nums1[Px]
            else: 
                min_of_right = min(nums1[Px], nums2[Py])

            return (max_of_left + min_of_right) / 2.0
    
nums1 = [1,3,8,9,15]
nums2 = [7,11,18,19,21,25]
print(findMedianSortedArrays1(nums1,nums2))