'''
Given a rotated sorted array, return index around which the array is rotated
'''
def findRotation(arr):
    low = 0
    high = len(arr)-1
    while low<high:
        mid = low + (high-low)//2
        if arr[mid]>arr[high]:
            low = mid+1
        else:
            high = mid
    return low

arr = [80,10,20,30,40,50,60,70]
print(findRotation(arr))