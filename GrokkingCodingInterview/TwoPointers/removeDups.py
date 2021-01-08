'''Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
nums = [1,1,2]
Output: 2, nums = [1,2]
'''
def do(arr):
    unique = 1
    for current in range(1,len(arr)):
        if arr[current]!=arr[current-1]:
            arr[unique]=arr[current]
            unique+=1
    return unique
            

print(do([2, 3, 3, 3, 6, 9, 9]))