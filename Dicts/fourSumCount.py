'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
'''
import collections

def fourSumCount(A, B, C, D):
    hashtable = {}
    for a in A:
        for b in B :
            hashtable[a+b] = hashtable.get(a+b,0)+1
    count = 0         
    for c in C :
        for d in D :
            count +=hashtable.get(-(c+d),0)
    return count
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(fourSumCount(A,B,C,D))