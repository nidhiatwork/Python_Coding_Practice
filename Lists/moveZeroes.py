# Move all zeroes of a list towards the end, while maintaining order of other elements.
def moveZeroes(nums):
    j = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

# nums = [4,2,4,0,0,3,0,5,1,0]
nums = [0,1,0,3,12]
print(moveZeroes(nums))