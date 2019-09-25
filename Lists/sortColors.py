'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''

def sortColors_1(nums):
    num0 = 0
    num1 = 0
    num2 = 0
    for i in range(len(nums)):
        if (nums[i] == 0): num0+=1
        elif (nums[i] == 1): num1+=1
        elif (nums[i] == 2): num2+=1
    for i in range(num0):
        nums[i] = 0
    for i in range(num1):
        nums[num0+i] = 1
    for i in range(num2):
        nums[num0+num1+i] = 2
    return nums


def sortColors_2(nums):
    j = 0
    k = len(nums) - 1
    i=0
    while i<=k:
        if nums[i] == 0 and i != j:
            nums[i],nums[j] = nums[j],nums[i]
            i-=1
            j+=1
        elif nums[i] == 2 and i != k:
            nums[i],nums[k] = nums[k],nums[i]
            i-=1
            k-=1
        i+=1
    return nums

nums = [2,0,2,1,1,0]
print(sortColors_2(nums))
