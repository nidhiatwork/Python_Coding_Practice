'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''

def sortColors_1(arr):
    num0,num1,num2 = 0,0,0
    for i in range(len(arr)):
    	num0+=1 if arr[i]==0 else 0
    	num1+=1 if arr[i]==1 else 0
    	num2+=1 if arr[i]==2 else 0
    for i in range(num0):
    	arr[i]=0
    for i in range(num1):
    	arr[num0+i]=1
    for i in range(num2):
    	arr[num0+num1+i]=2
    return arr
	

def sortColors(arr):
    low, high = 0, len(arr)-1
    i=0
    while i <= high:
        if arr[i] == 0:
            arr[i],arr[low]=arr[low],arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
    return arr
nums = [0,2,1,2,2,1,1,0,2]

print(sortColors_1(nums))
