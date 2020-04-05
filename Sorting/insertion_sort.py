def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j >0 and arr[j-1]>arr[j] :
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1
    return arr
    
print(insertionSort([4,8,2,6,7,0]))