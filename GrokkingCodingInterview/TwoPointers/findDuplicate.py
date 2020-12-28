'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

'''

def findDuplicate(nums):
    slow =nums[0]
    fast = nums[nums[0]]
    print('slow',slow)
    print('fast',fast)
    while slow != fast:
        slow = nums[slow]
        print('slow',slow)
        fast =  nums[nums[fast]]
        print('fast',fast)

    fast = 0
    while slow != fast:
        print('slow',slow)
        print('fast',fast)
        slow = nums[slow]
        fast = nums[fast]
    return slow

nums = [2,5,9,6,9,3,8,9,7,1]    
print(findDuplicate(nums))
