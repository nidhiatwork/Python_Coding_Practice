from collections import defaultdict
def do(arr):
    window_start,window_end=0,0
    l,max_l=0,0
    mp=dict()
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char in mp:
            window_start = max(window_start, mp[right_char]+1)
        mp[right_char]=window_end
        l = window_end-window_start+1
        max_l = max(max_l, l)
    return max_l

print(do("aabcbb"))
