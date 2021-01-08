'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
'''

def increasingTriplet(nums):
    first = second = float('inf') # Initialize two variables to infinite
    for n in nums: # Loop through all numbers
        if n <= first: # If it is less then infinite you know you got the first triplet
            first = n
        elif n <= second: # If it is less then infinite you know you got the second triplet
            second = n
        else: # If its not less then the first and second then you know its the last value your looking for.
            return True
    return False

nums = [1,1,1,1,1,1,1,1]
print(increasingTriplet(nums))