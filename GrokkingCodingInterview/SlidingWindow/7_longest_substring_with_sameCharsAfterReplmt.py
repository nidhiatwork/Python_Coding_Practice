from collections import defaultdict
def do(s,k):
    window_start,window_end=0,0
    max_len=0
    frequency=defaultdict(int)
    count=0
    for window_end in range(len(s)):
        frequency[s[window_end]]+=1
        count=max(count, frequency[s[window_end]])
        if window_end-window_start+1-count>k:
            frequency[s[window_start]]-=1
            window_start+=1
        max_len=max(max_len, window_end-window_start+1)
    return max_len

print(do("aabccbb",2))
