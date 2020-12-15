'''Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
nums = [1,1,2]
Output: 2, nums = [1,2]
'''
def do(arr, key):
    keyP = 0
    for current in range(len(arr)):
        if arr[current]!=key:
            arr[keyP]=arr[current]
            keyP+=1
    return keyP
print(do([3,2,3,6,3,10,9,3], 3))