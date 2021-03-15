def mergeSortAndCount(arr,l,r):
    count = 0
    if l<r:
        mid = (l+r)//2 #Finding the mid of the array 
        count+=mergeSortAndCount(arr,l,mid)
        count+=mergeSortAndCount(arr,mid+1,r) # Sorting the second half
        count+=mergeAndCount(arr,l,mid,r)
    return count
def mergeAndCount(arr,l,m,r):
    L = arr[l:m]
    R = arr[m:r]
    i = j = k = swaps = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
            swaps += (m + 1) - (l + i)
        k+=1
    return swaps

arr = [1, 9, 6, 4, 5]
print(mergeSortAndCount(arr,0,len(arr)))
