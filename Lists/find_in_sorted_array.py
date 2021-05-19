
def find_in_array(arr, target):
    i = 0
    j = len(arr[0])-1
    found = False
    
    while i<len(arr) and j>=0:
        if target<arr[i][j]:
            j-=1
        elif target > arr[i][j]:
            i+=1
        else:
            found = True
            while j>0 and arr[i][j-1]==target:
                j-=1
            break
    
    if found:
        return (i+1)*1009 + (j+1)
    return -1        

arr = [
	[1,3,4],
	[5,5,7],
	[5,11,12]
]
print(find_in_array(arr, 5))