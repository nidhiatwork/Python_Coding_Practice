'''
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
 

Example 1:

Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
'''

def merge(arr1,arr2,n,m):
    i,j=0,0
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            i+=1
        else:
            arr1[i],arr2[j] = arr2[j],arr1[i]
            i+=1
            insertionSort(arr2,j)
    print(arr1,arr2)

def insertionSort(arr,j):
    item = arr[j]
    while j+1<len(arr) and item>arr[j+1]:
        arr[j]=arr[j+1]
        j+=1
    arr[j]=item

n = 4
arr1 = [1,3,5,7] 
m = 5
arr2 = [0,2,6,8,9]
merge(arr1,arr2,n,m)