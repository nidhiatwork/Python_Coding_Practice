'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
'''

def validMountainArray_1(A):
    i=1
    ascent,descent=0,0
    while i < len(A):
        if A[i]>A[i-1]:
            ascent=1
        else:
            break
        i+=1

    while i < len(A):
        if A[i] <A[i-1]:
            descent=1
        else:
            descent=0
            break
        i+=1
    return bool(ascent and descent)

def validMountainArray_2(A):
        i, j, n = 0, len(A) - 1, len(A)
        while i < n - 1 and A[i] < A[i + 1]: 
            i += 1
        while j > 0 and A[j - 1] > A[j]: 
            j -= 1
        return 0 < i and j < n - 1 and i==j


A = [1,2]
print(validMountainArray_2(A))