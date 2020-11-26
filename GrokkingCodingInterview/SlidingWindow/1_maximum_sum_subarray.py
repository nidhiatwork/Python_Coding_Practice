def do(arr,k):
    window_start,window_end=0,0
    max_sm = 0
    sm=0
    while window_end<len(arr):
        sm+=arr[window_end]
        max_sm=max(max_sm,sm)
        window_end+=1
        if window_end-window_start==k:
            sm-=arr[window_start]
            window_start+=1
    return max_sm

print(do([2, 3,4,1,5],2))
