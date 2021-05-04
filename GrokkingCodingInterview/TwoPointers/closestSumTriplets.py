'''
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the diff of the triplet. If there are more than one such triplet, return the diff of the triplet with the smallest sum.
Input: [-2, 0, 1, 2], target=2
Output: 1'''

import math
def closestSumTriplets(arr, target):
    arr.sort()
    min_diff = math.inf
    for f in range(len(arr)-2):
        s,t=f+1,len(arr)-1
        while s<t:
            sum = arr[f]+arr[s]+arr[t]
            diff = abs(sum-target)
            if diff<min_diff:
                min_diff=diff
                ans = sum
            if sum>target:
                t-=1
            elif sum<target:
                s+=1
            else:
                t-=1
                s+=1
    return ans

print(closestSumTriplets([1, 0, 1, 1],100))

