import math
def do(arr,S):
    window_start,window_end=0,0
    sm=0
    length, min_length=0,math.inf
    for window_end in range(len(arr)):
        sm+=arr[window_end]
        while sm>=S:
            length = window_end-window_start+1
            min_length=min(min_length, length)
            sm-=arr[window_start]
            window_start+=1
    return 0 if min_length==math.inf else min_length

print(do([2,1,5,2,8],7))
