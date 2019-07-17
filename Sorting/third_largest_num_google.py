'''
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 
Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
'''
def pick_third_largest(A):
    n = len(A)
    if n<3:
        return None
    mergeSort(A)
    return A[2]
	
def mergeSort(A):
    n = len(A)
    if n>1:
        mid = n//2 
        L = A[:mid] 
        R = A[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] > R[j]:
                A[k]=L[i]
                i+=1
                k+=1
            else:
                A[k]=R[j]
                j+=1
                k+=1

        while i<len(L):
            A[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            A[k]=R[j]
            j+=1
            k+=1

a = [4,2,7,0,23,199,543]
print(pick_third_largest(a))