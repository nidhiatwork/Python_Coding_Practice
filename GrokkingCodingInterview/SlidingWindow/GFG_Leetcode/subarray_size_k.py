'''
Given an array arr[] and two integers K and X, the task is to find the maximum sum among all subarrays of size K with the sum less than X.

Examples:

Input: arr[] = {20, 2, 3, 10, 5}, K = 3, X = 20
Output: 18
'''


from collections import defaultdict
from collections import Counter
import math
import math
def do(arr,K,X):
    sm,max_sm=0,-math.inf
    ws=0
    for we in range(len(arr)):
        sm+=arr[we]     
        if we-ws+1==K:
            if sm<X:
                max_sm=max(sm,max_sm)
            sm-=arr[ws]
            ws+=1
    return max_sm        
    
print(do([-5, 8, 7, 2, 10, 1, 20, -4, 6, 9], 5,30))
