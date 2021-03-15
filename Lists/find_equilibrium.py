'''
Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Example 1:

Input:
n = 1
A[] = {1}
Output: 1
Explanation: Since its the only 
element hence its the only equilibrium 
point. 
'''
def equilibrium(arr):

    # finding the sum of whole array
    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):
        
        # total_sum is now right sum
        # for index i
        total_sum -= num
        
        if leftsum == total_sum:
            return i
        leftsum += num
     
      # If no equilibrium index found, 
      # then return -1
    return -1
    
arr = [1,3,5,2,2]
n = len(arr)
print(equilibrium(arr))