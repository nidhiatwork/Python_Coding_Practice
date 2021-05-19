'''Search element within a linearly sorted two dimensional array'''

def searchInMatrix(arr, key, low, high):
    while low<=high:
        mid = low+high//2
        mid_element = arr[mid//len(arr[0])][mid%len(arr[0])]
        if key==mid_element:
            return mid
        elif key<mid_element:
            high = mid-1
        else:
            low = mid+1
    return -1

arr = [
    [4,6,8],
    [9,14,16],
    [17,19,21],
    [22,25,29]
]
print(searchInMatrix(arr, 25, 0, (len(arr) * len(arr[0]))-1))