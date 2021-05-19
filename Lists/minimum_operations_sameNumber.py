'''
minimum operations to convert all items in an array as same number

'''
def operations(mat,k):
    arr = [item for row in mat for item in row]
    arr.sort()
    median = None
    if len(arr)%2:
        median = arr[len(arr)//2]
    else:
        median = (arr[len(arr)//2]+ arr[(len(arr)//2)+1])/2
    
    ans=0
    for item in arr:
        ans+=abs(item-median)//k
    return ans
mat = [
    [0, 2, 4],
    [0, 2, 4],
    [0, 2, 4]
    ]
print(operations(mat, 2))