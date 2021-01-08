'''Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.'''

def findDuplicate_set(nums):
    s = set()
    for n in nums:
        if n in s:
            return n
        s.add(n)

def findDuplicate_sort(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

def findDuplicate_TortoiseHare_cycledetection(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Find the "entrance" to the cycle.
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1
    
nums = [1, 4, 6, 6, 6, 2, 3]
print(findDuplicate_TortoiseHare_cycledetection(nums))