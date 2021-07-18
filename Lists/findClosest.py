'''
	Find three closest elements from given three sorted arrays
	Given three sorted arrays A[], B[] and C[], find 3 elements i, j and k from A, B and C respectively such that max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized. Here abs() indicates absolute value.
	
	Input: A[] = {1, 4, 10}
       B[] = {2, 15, 20}
       C[] = {10, 12}
Output: 10 15 10
10 from A, 15 from B and 10 from C
'''
import sys
def findClosest(A, B, C, p, q, r):
 
    # Initialize min diff
    diff = sys.maxsize
 
    res_i = 0
    res_j = 0
    res_k = 0

    # Travesre Array
    i = 0
    j = 0
    k = 0
    while(i < p and j < q and k < r):
 
        # Find minimum and maximum of
        # current three elements
        minimum = min(A[i], min(B[j], C[k]))
        maximum = max(A[i], max(B[j], C[k]))
 
        # Update result if current diff is
        # less than the min diff so far
        if maximum-minimum < diff:
            res_i = i
            res_j = j
            res_k = k
            diff = maximum - minimum
 
        # We can 't get less than 0 as
        # values are absolute
        if diff == 0:
            break
 
 
        # Increment index of array with
        # smallest value
        if A[i] == minimum:
            i = i+1
        elif B[j] == minimum:
            j = j+1
        else:
            k = k+1
 
    # Print result
    print(A[res_i], " ", B[res_j], " ", C[res_k])
 
# Driver Program
A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
 
p = len(A)
q = len(B)
r = len(C)
 
findClosest(A,B,C,p,q,r)
