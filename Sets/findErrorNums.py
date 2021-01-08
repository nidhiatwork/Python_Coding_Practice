'''
The set S originally contains random numbers from 1 to n. But one of the numbers in the set got duplicated to another number in the set.

Given the array nums, find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Input: nums = [1,2,2,4]
Output: [2,3]

'''
def findErrorNums(nums):
    n=len(nums)
    duplicate = sum(nums)-sum(set(nums))
    missing = n*(n+1)//2-sum(set(nums))
    return [duplicate,missing]

nums = [1,1]
print(findErrorNums(nums)) #[2,3]

