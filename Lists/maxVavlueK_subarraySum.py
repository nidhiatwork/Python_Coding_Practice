'''Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.
A = [1, 2, 3, 4, 5] B = 10

o/p - 2
'''
from collections import deque
def findMaxK(arr, B):
    L = []
    val = 0
    for i in range(len(arr)):
        L.append(val)
        val+= arr[i]
    R = deque()
    val = 0
    for i in reversed(range(len(arr))):
        R.appendleft(val)
        val+= arr[i]
    sum_arr = sum(arr)
    k = len(arr)
    while k>0:
        i=0
        while i+k-1<len(arr):
            sum_sub_arr = sum_arr - L[i] - R[i+k-1]
            if sum_sub_arr>B:
                break
            i+=1
        if i+k-1>=len(arr):
            break
        k-=1
    return k


arr = [1,2,3,4,5]
B = 12
print(findMaxK(arr,B))