'''
GGiven an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]'''
'''
Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).
'''

import math
def TripletsLessThanSum(arr, target):
    arr.sort()
    count=0
    for i in range(len(arr)-2):
        left,right=i+1,len(arr)-1
        while left<right:
            sum = arr[i]+arr[left]+arr[right]
            if sum>=target:
                right-=1
            else:
                count+=(right-left) #since all elements between left and right will satisfy
                left+=1
            
    return count


print(TripletsLessThanSum([5,1,3,4,7],12))

