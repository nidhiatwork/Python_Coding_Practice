'''
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
Input: [0,1,0]
Output: 1
'''

def peakIndexInMountainArray(A):
    if len(A)<3:
        return -1
    i,j,n=0,len(A)-1,len(A)
    while i+1<n and A[i+1]>A[i]:
        i+=1
    while j>0 and A[j]<A[j-1]:
        j-=1
    
    return i if i==j and i>0 and j<n-1 else -1

A = [0,1,0]
print(peakIndexInMountainArray(A))
