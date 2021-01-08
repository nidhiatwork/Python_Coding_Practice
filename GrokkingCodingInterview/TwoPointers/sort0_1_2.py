'''
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
'''

def do(arr):
    i,low,high=0,0,len(arr)-1
    while i<=high:
        if arr[i]==0:
            arr[low],arr[i]=arr[i], arr[low]
            i+=1
            low+=1
        elif arr[i]==1:
            i+=1
        else:
            arr[high],arr[i]=arr[i], arr[high]
            high-=1
    return arr 

print(do([2,2,0,1,2,0]))