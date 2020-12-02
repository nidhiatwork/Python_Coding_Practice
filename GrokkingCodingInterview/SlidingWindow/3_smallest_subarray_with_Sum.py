import math
def do(s,arr):
    window_start,window_end=0,0
    min_l=math.inf
    sm=0
    for window_end in range(len(arr)):
        sm+=arr[window_end]
        while sm>=s:
            min_l=min(min_l,window_end-window_start+1)
            sm-=arr[window_start]
            window_start+=1
    return 0 if min_l==math.inf else min_l

print(do(7,[2, 1,5,2,3,2]))
