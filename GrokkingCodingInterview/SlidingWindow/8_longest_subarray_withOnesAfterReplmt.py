from collections import defaultdict
def do(s,k):
    window_start,window_end=0,0
    max_len=0
    maxOnesCount=0
    for window_end in range(len(s)):
        if s[window_end]==1:
            maxOnesCount+=1
        if window_end-window_start+1-maxOnesCount>k:
            if s[window_start]==1:
                maxOnesCount-=1
            window_start+=1
        max_len=max(max_len, window_end-window_start+1)
    return max_len

print(do([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
