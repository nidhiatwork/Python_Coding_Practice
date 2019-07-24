def findMedianSortedArrays(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    start, end = 0, m
    while start <= end:
        Px = (start + end) // 2
        Py = ((m + n + 1) // 2) - Px
        print(Px,Py)
        if Px < m and B[Py-1] > A[Px]:
            print(B[Py-1],"> ", A[Px])
            print("Px is too small, must increase it")
            start = Px + 1
        elif Px > 0 and A[Px-1] > B[Py]:
            print(A[Px-1],"> ", B[Py])
            print("Px is too big, must decrease it")
            end = Px - 1
        else:
            # Px is perfect
            if Px == 0: 
                max_of_left = B[Py-1]
            elif Py == 0: 
                max_of_left = A[Px-1]
            else: 
                max_of_left = max(A[Px-1], B[Py-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if Px == m: 
                min_of_right = B[Py]
            elif Py == n: 
                min_of_right = A[Px]
            else: 
                min_of_right = min(A[Px], B[Py])

            return (max_of_left + min_of_right) / 2.0
    
A = [1,3,8,9,15]
B = [7,11,18,19,21,25]
print(findMedianSortedArrays(A,B))